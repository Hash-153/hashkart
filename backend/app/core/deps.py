from datetime import datetime
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.core.security import decode_token
from app.models.user import User, Role
from app.models.security_models import UserSession

security_scheme = HTTPBearer(auto_error=False)


async def get_current_user_optional(
    auth: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    db: AsyncSession = Depends(get_db),
) -> Optional[User]:
    """Retrieve current user from JWT token if header present, verifying session revocation & account status."""
    if not auth or not auth.credentials:
        return None

    try:
        payload = decode_token(auth.credentials)
        user_id_str = payload.get("sub")
        jti = payload.get("jti")
        if not user_id_str:
            return None

        # Check session revocation if JTI is attached
        if jti:
            sess_res = await db.execute(select(UserSession).where(UserSession.token_jti == jti))
            session = sess_res.scalar_one_or_none()
            if session and session.is_revoked:
                return None

        user_id = int(user_id_str)
        result = await db.execute(
            select(User)
            .options(selectinload(User.roles).selectinload(Role.permissions))
            .where(User.id == user_id)
        )
        user = result.scalar_one_or_none()

        if not user or not user.is_active:
            return None

        # Check account lockout / suspension
        if user.account_status in ["LOCKED", "SUSPENDED"]:
            if user.locked_until and user.locked_until > datetime.utcnow():
                return None
            elif user.account_status == "SUSPENDED":
                return None

        return user
    except Exception:
        return None


async def get_current_user(
    user: Optional[User] = Depends(get_current_user_optional),
) -> User:
    """Require valid authenticated active user."""
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided, expired, or revoked.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


class RoleChecker:
    """Dependency validator enforcing Role-Based Access Control (RBAC)."""

    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(get_current_user)) -> User:
        user_role_names = [r.name for r in user.roles]
        has_permission = any(role in self.allowed_roles for role in user_role_names)
        if not has_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User role lacks permission. Required: {self.allowed_roles}",
            )
        return user


class PermissionChecker:
    """Dependency validator enforcing fine-grained permission codes."""

    def __init__(self, required_permission: str):
        self.required_permission = required_permission

    def __call__(self, user: User = Depends(get_current_user)) -> User:
        user_role_names = [r.name for r in user.roles]
        if "ADMIN" in user_role_names:
            return user

        # Collect all permission codes across roles
        user_permissions = set()
        for role in user.roles:
            for perm in getattr(role, "permissions", []):
                user_permissions.add(perm.code)

        if self.required_permission not in user_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User lacks required permission: '{self.required_permission}'",
            )
        return user


require_admin = RoleChecker(["ADMIN"])
require_manager = RoleChecker(["ADMIN", "MANAGER"])
require_staff = RoleChecker(["ADMIN", "MANAGER", "SUPPORT"])
require_customer = RoleChecker(["ADMIN", "MANAGER", "SUPPORT", "CUSTOMER"])


def require_role(roles: List[str]):
    return RoleChecker(roles)

