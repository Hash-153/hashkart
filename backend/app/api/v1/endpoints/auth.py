import uuid
from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User, Role, Address, Permission
from app.models.security_models import UserSession, PasswordResetToken
from app.models.system import AuditLog
from app.schemas.user import (
    UserRegister,
    UserLogin,
    UserResponse,
    Token,
    PasswordChangeRequest,
    PasswordResetRequest,
    PasswordResetConfirm,
    UserProfileUpdate,
    UserSessionResponse,
)
from app.core.security import (
    get_password_hash,
    verify_password,
    validate_password_strength,
    create_access_token,
    create_refresh_token,
    decode_token,
    generate_secure_token,
    hash_token,
)
from app.core.deps import get_current_user, security_scheme
from fastapi.security import HTTPAuthorizationCredentials

router = APIRouter()


def _get_user_permissions(user: User) -> List[str]:
    """Extract distinct permission codes across all user roles."""
    perms = set()
    for role in user.roles:
        for p in getattr(role, "permissions", []):
            perms.add(p.code)
    return sorted(list(perms))


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserRegister, db: AsyncSession = Depends(get_db)):
    """Register a new customer account with password strength enforcement."""
    # 1. Password Strength Validation
    is_valid_pw, msg = validate_password_strength(user_in.password)
    if not is_valid_pw:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

    # 2. Check Duplicate Email
    email_clean = user_in.email.strip().lower()
    existing_user = await db.execute(select(User).where(User.email == email_clean))
    if existing_user.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email address already exists.",
        )

    # 3. Get CUSTOMER role
    role_res = await db.execute(
        select(Role).options(selectinload(Role.permissions)).where(Role.name == "CUSTOMER")
    )
    customer_role = role_res.scalar_one_or_none()
    if not customer_role:
        customer_role = Role(name="CUSTOMER", description="Default Customer Role")
        db.add(customer_role)
        await db.flush()

    new_user = User(
        email=email_clean,
        password_hash=get_password_hash(user_in.password),
        full_name=user_in.full_name,
        phone_number=user_in.phone_number,
        account_status="ACTIVE",
        is_active=True,
        is_verified=True,
        roles=[customer_role],
    )
    db.add(new_user)
    await db.flush()

    # 4. Audit Log Entry
    audit = AuditLog(
        user_id=new_user.id,
        action="USER_REGISTERED",
        entity_type="User",
        entity_id=str(new_user.id),
        details=f"New user registered with email {email_clean}",
    )
    db.add(audit)
    await db.commit()

    # Re-fetch user with relations
    user_res = await db.execute(
        select(User)
        .options(selectinload(User.roles).selectinload(Role.permissions))
        .where(User.id == new_user.id)
    )
    user_db = user_res.scalar_one()

    return UserResponse(
        id=user_db.id,
        email=user_db.email,
        full_name=user_db.full_name,
        phone_number=user_db.phone_number,
        account_status=user_db.account_status,
        is_active=user_db.is_active,
        is_verified=user_db.is_verified,
        roles=[r.name for r in user_db.roles],
        permissions=_get_user_permissions(user_db),
        created_at=user_db.created_at,
        updated_at=user_db.updated_at,
    )


@router.post("/login", response_model=Token)
async def login(
    user_in: UserLogin,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    """Authenticate credentials with account lockout protection and session tracking."""
    email_clean = user_in.email.strip().lower()
    result = await db.execute(
        select(User)
        .options(selectinload(User.roles).selectinload(Role.permissions))
        .where(User.email == email_clean)
    )
    user = result.scalar_one_or_none()

    # Safe Generic Credential Error (Prevents Account Enumeration)
    cred_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password.",
    )

    if not user:
        raise cred_error

    # Check Lockout Status
    now = datetime.utcnow()
    if user.account_status == "LOCKED":
        if user.locked_until and user.locked_until > now:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Account is locked due to multiple failed login attempts. Try again after {user.locked_until.strftime('%H:%M UTC')}.",
            )
        else:
            # Unlock expired lockout
            user.account_status = "ACTIVE"
            user.failed_login_attempts = 0
            user.locked_until = None

    if not user.is_active or user.account_status == "SUSPENDED":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account has been suspended or deactivated. Contact support.",
        )

    # Verify Password
    if not verify_password(user_in.password, user.password_hash):
        user.failed_login_attempts += 1
        if user.failed_login_attempts >= 5:
            user.account_status = "LOCKED"
            user.locked_until = now + timedelta(minutes=15)
            audit_lock = AuditLog(
                user_id=user.id,
                action="ACCOUNT_LOCKED",
                entity_type="User",
                entity_id=str(user.id),
                details="Account locked after 5 consecutive failed login attempts.",
            )
            db.add(audit_lock)

        audit_fail = AuditLog(
            user_id=user.id,
            action="LOGIN_FAILED",
            entity_type="User",
            entity_id=str(user.id),
            details=f"Failed login attempt {user.failed_login_attempts}/5",
        )
        db.add(audit_fail)
        await db.commit()
        raise cred_error

    # Reset Failed Attempts & Record Login
    user.failed_login_attempts = 0
    user.locked_until = None
    user.last_login_at = now

    # Token & Session Generation
    token_jti = uuid.uuid4().hex
    role_names = [r.name for r in user.roles]
    permissions = _get_user_permissions(user)

    access_token = create_access_token(
        subject=user.id, roles=role_names, permissions=permissions, jti=token_jti
    )
    refresh_token = create_refresh_token(subject=user.id, jti=token_jti)

    # Track User Session
    ip_addr = request.client.host if request.client else "127.0.0.1"
    user_agent = request.headers.get("user-agent", "Unknown Client")
    device_type = "Mobile" if "Mobile" in user_agent else "Desktop"

    user_sess = UserSession(
        user_id=user.id,
        token_jti=token_jti,
        refresh_token_hash=hash_token(refresh_token),
        ip_address=ip_addr,
        user_agent=user_agent[:255],
        device_type=device_type,
        is_revoked=False,
        expires_at=now + timedelta(days=7),
    )
    db.add(user_sess)

    audit_success = AuditLog(
        user_id=user.id,
        action="LOGIN_SUCCESS",
        entity_type="User",
        entity_id=str(user.id),
        details=f"Login successful from IP {ip_addr}",
    )
    db.add(audit_success)
    await db.commit()

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        expires_in=3600,
    )


@router.post("/logout")
async def logout(
    auth: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Revoke current active session JWT."""
    if auth and auth.credentials:
        try:
            payload = decode_token(auth.credentials)
            jti = payload.get("jti")
            if jti:
                sess_res = await db.execute(
                    select(UserSession).where(UserSession.token_jti == jti)
                )
                session = sess_res.scalar_one_or_none()
                if session:
                    session.is_revoked = True
        except Exception:
            pass

    audit = AuditLog(
        user_id=current_user.id,
        action="LOGOUT",
        entity_type="User",
        entity_id=str(current_user.id),
        details="User logged out successfully.",
    )
    db.add(audit)
    await db.commit()

    return {"message": "Logged out successfully."}


@router.post("/refresh", response_model=Token)
async def refresh_tokens(
    refresh_token: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    """Execute Refresh Token Rotation and issue new Access/Refresh token pair."""
    try:
        payload = decode_token(refresh_token)
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type."
            )
        user_id = int(payload.get("sub", 0))
        old_jti = payload.get("jti")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired refresh token."
        )

    # Check Session Revocation
    sess_res = await db.execute(
        select(UserSession).where(UserSession.token_jti == old_jti, UserSession.user_id == user_id)
    )
    session = sess_res.scalar_one_or_none()
    if not session or session.is_revoked:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Session has been revoked."
        )

    # Revoke Old Session
    session.is_revoked = True

    # Query User
    user_res = await db.execute(
        select(User)
        .options(selectinload(User.roles).selectinload(Role.permissions))
        .where(User.id == user_id, User.is_active == True)
    )
    user = user_res.scalar_one_or_none()
    if not user or user.account_status in ["LOCKED", "SUSPENDED"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Account is disabled or locked."
        )

    # Generate New Pair with new JTI
    new_jti = uuid.uuid4().hex
    role_names = [r.name for r in user.roles]
    permissions = _get_user_permissions(user)

    new_access_token = create_access_token(
        subject=user.id, roles=role_names, permissions=permissions, jti=new_jti
    )
    new_refresh_token = create_refresh_token(subject=user.id, jti=new_jti)

    # Create New Active Session
    ip_addr = request.client.host if request.client else "127.0.0.1"
    user_agent = request.headers.get("user-agent", "Unknown Client")
    device_type = "Mobile" if "Mobile" in user_agent else "Desktop"

    new_sess = UserSession(
        user_id=user.id,
        token_jti=new_jti,
        refresh_token_hash=hash_token(new_refresh_token),
        ip_address=ip_addr,
        user_agent=user_agent[:255],
        device_type=device_type,
        is_revoked=False,
        expires_at=datetime.utcnow() + timedelta(days=7),
    )
    db.add(new_sess)
    await db.commit()

    return Token(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
        token_type="bearer",
        expires_in=3600,
    )


@router.post("/forgot-password")
async def forgot_password(
    request_in: PasswordResetRequest,
    db: AsyncSession = Depends(get_db),
):
    """Initiate password reset flow (generates synthetic dev token without external email API)."""
    email_clean = request_in.email.strip().lower()
    user_res = await db.execute(select(User).where(User.email == email_clean))
    user = user_res.scalar_one_or_none()

    # Always return standard safe message to prevent email enumeration
    safe_response = {
        "message": f"If an account with {email_clean} exists, password reset instructions have been generated."
    }

    if not user:
        return safe_response

    # Generate one-time reset token (15 minutes TTL)
    raw_token = generate_secure_token()
    token_h = hash_token(raw_token)
    expires_at = datetime.utcnow() + timedelta(minutes=15)

    reset_token_obj = PasswordResetToken(
        user_id=user.id,
        token_hash=token_h,
        is_used=False,
        expires_at=expires_at,
    )
    db.add(reset_token_obj)

    audit = AuditLog(
        user_id=user.id,
        action="PASSWORD_RESET_REQUESTED",
        entity_type="User",
        entity_id=str(user.id),
        details=f"Password reset requested for {email_clean}",
    )
    db.add(audit)
    await db.commit()

    # Attach development simulation token payload in dev/test mode
    safe_response["dev_simulation_reset_token"] = raw_token
    safe_response["dev_reset_url"] = f"/reset-password?token={raw_token}"
    return safe_response


@router.post("/reset-password")
async def reset_password(
    reset_in: PasswordResetConfirm,
    db: AsyncSession = Depends(get_db),
):
    """Validate one-time reset token, update password, and revoke all existing sessions."""
    is_valid_pw, msg = validate_password_strength(reset_in.new_password)
    if not is_valid_pw:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

    token_h = hash_token(reset_in.reset_token)
    token_res = await db.execute(
        select(PasswordResetToken).where(
            PasswordResetToken.token_hash == token_h,
            PasswordResetToken.is_used == False,
        )
    )
    reset_obj = token_res.scalar_one_or_none()

    if not reset_obj or reset_obj.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid, used, or expired password reset token.",
        )

    # Fetch User
    user_res = await db.execute(select(User).where(User.id == reset_obj.user_id))
    user = user_res.scalar_one()

    # Update Password & Reset Lockout
    user.password_hash = get_password_hash(reset_in.new_password)
    user.account_status = "ACTIVE"
    user.failed_login_attempts = 0
    user.locked_until = None
    reset_obj.is_used = True

    # Revoke All Active Sessions
    await db.execute(
        update(UserSession)
        .where(UserSession.user_id == user.id, UserSession.is_revoked == False)
        .values(is_revoked=True)
    )

    audit = AuditLog(
        user_id=user.id,
        action="PASSWORD_RESET_COMPLETED",
        entity_type="User",
        entity_id=str(user.id),
        details="Password reset completed successfully. Active sessions revoked.",
    )
    db.add(audit)
    await db.commit()

    return {"message": "Password reset successful. Please log in with your new password."}


@router.post("/change-password")
async def change_password(
    pw_in: PasswordChangeRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Change password for currently authenticated user."""
    if not verify_password(pw_in.current_password, current_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect current password."
        )

    is_valid_pw, msg = validate_password_strength(pw_in.new_password)
    if not is_valid_pw:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

    current_user.password_hash = get_password_hash(pw_in.new_password)

    if pw_in.logout_other_sessions:
        await db.execute(
            update(UserSession)
            .where(UserSession.user_id == current_user.id, UserSession.is_revoked == False)
            .values(is_revoked=True)
        )

    audit = AuditLog(
        user_id=current_user.id,
        action="PASSWORD_CHANGED",
        entity_type="User",
        entity_id=str(current_user.id),
        details="User changed password successfully.",
    )
    db.add(audit)
    await db.commit()

    return {"message": "Password updated successfully."}


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Fetch complete profile details for the currently authenticated user."""
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        phone_number=current_user.phone_number,
        profile_image_url=current_user.profile_image_url,
        account_status=current_user.account_status,
        is_active=current_user.is_active,
        is_verified=current_user.is_verified,
        preferred_language=current_user.preferred_language,
        preferred_currency=current_user.preferred_currency,
        last_login_at=current_user.last_login_at,
        roles=[r.name for r in current_user.roles],
        permissions=_get_user_permissions(current_user),
        created_at=current_user.created_at,
        updated_at=current_user.updated_at,
    )


@router.put("/profile", response_model=UserResponse)
async def update_profile(
    profile_in: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update profile information."""
    if profile_in.full_name is not None:
        current_user.full_name = profile_in.full_name
    if profile_in.first_name is not None:
        current_user.first_name = profile_in.first_name
    if profile_in.last_name is not None:
        current_user.last_name = profile_in.last_name
    if profile_in.phone_number is not None:
        current_user.phone_number = profile_in.phone_number
    if profile_in.profile_image_url is not None:
        current_user.profile_image_url = profile_in.profile_image_url
    if profile_in.preferred_language is not None:
        current_user.preferred_language = profile_in.preferred_language
    if profile_in.preferred_currency is not None:
        current_user.preferred_currency = profile_in.preferred_currency

    await db.commit()
    await db.refresh(current_user)

    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        phone_number=current_user.phone_number,
        profile_image_url=current_user.profile_image_url,
        account_status=current_user.account_status,
        is_active=current_user.is_active,
        is_verified=current_user.is_verified,
        preferred_language=current_user.preferred_language,
        preferred_currency=current_user.preferred_currency,
        last_login_at=current_user.last_login_at,
        roles=[r.name for r in current_user.roles],
        permissions=_get_user_permissions(current_user),
        created_at=current_user.created_at,
        updated_at=current_user.updated_at,
    )


@router.get("/sessions", response_model=List[UserSessionResponse])
async def list_active_sessions(
    auth: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List active authentication sessions for current user."""
    current_jti = None
    if auth and auth.credentials:
        try:
            payload = decode_token(auth.credentials)
            current_jti = payload.get("jti")
        except Exception:
            pass

    sess_res = await db.execute(
        select(UserSession)
        .where(UserSession.user_id == current_user.id, UserSession.is_revoked == False)
        .order_by(UserSession.last_active_at.desc())
    )
    sessions = sess_res.scalars().all()

    return [
        UserSessionResponse(
            id=s.id,
            token_jti=s.token_jti,
            ip_address=s.ip_address,
            user_agent=s.user_agent,
            device_type=s.device_type,
            is_revoked=s.is_revoked,
            is_current=(s.token_jti == current_jti),
            created_at=s.created_at,
            last_active_at=s.last_active_at,
            expires_at=s.expires_at,
        )
        for s in sessions
    ]


@router.delete("/sessions/{session_id}")
async def revoke_session(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Revoke a specific active session by ID."""
    sess_res = await db.execute(
        select(UserSession).where(
            UserSession.id == session_id, UserSession.user_id == current_user.id
        )
    )
    session = sess_res.scalar_one_or_none()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found.")

    session.is_revoked = True
    audit = AuditLog(
        user_id=current_user.id,
        action="SESSION_REVOKED",
        entity_type="UserSession",
        entity_id=str(session_id),
        details=f"Revoked session {session_id} ({session.ip_address})",
    )
    db.add(audit)
    await db.commit()
    return {"message": f"Session {session_id} revoked."}


@router.delete("/sessions/other/all")
async def revoke_other_sessions(
    auth: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Revoke all active sessions except the currently active token session."""
    current_jti = None
    if auth and auth.credentials:
        try:
            payload = decode_token(auth.credentials)
            current_jti = payload.get("jti")
        except Exception:
            pass

    if current_jti:
        await db.execute(
            update(UserSession)
            .where(
                UserSession.user_id == current_user.id,
                UserSession.token_jti != current_jti,
                UserSession.is_revoked == False,
            )
            .values(is_revoked=True)
        )
    else:
        await db.execute(
            update(UserSession)
            .where(UserSession.user_id == current_user.id, UserSession.is_revoked == False)
            .values(is_revoked=True)
        )

    audit = AuditLog(
        user_id=current_user.id,
        action="ALL_OTHER_SESSIONS_REVOKED",
        entity_type="User",
        entity_id=str(current_user.id),
        details="Revoked all other active user sessions.",
    )
    db.add(audit)
    await db.commit()
    return {"message": "All other active sessions have been revoked."}
