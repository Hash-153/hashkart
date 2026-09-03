from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator
import re


# Permission & Role Schemas
class PermissionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    name: str
    description: Optional[str] = None


class RoleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str] = None
    permissions: List[PermissionResponse] = []


# Token Schemas
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenPayload(BaseModel):
    sub: str  # User ID
    roles: List[str] = []
    permissions: List[str] = []
    jti: Optional[str] = None
    exp: Optional[int] = None


# User Login / Register Schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    full_name: str = Field(..., min_length=2, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=20)

    @field_validator("phone_number")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        if v:
            clean_v = re.sub(r"[\s\-\(\)\+]", "", v)
            if not clean_v.isdigit() or len(clean_v) < 10 or len(clean_v) > 12:
                raise ValueError("Invalid phone number format. Provide 10-12 digits.")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8, max_length=100)
    logout_other_sessions: bool = True


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    reset_token: str
    new_password: str = Field(..., min_length=8, max_length=100)


class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=20)
    profile_image_url: Optional[str] = Field(None, max_length=500)
    preferred_language: Optional[str] = Field(None, max_length=10)
    preferred_currency: Optional[str] = Field(None, max_length=10)


# Address Schemas
class AddressCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    phone_number: str = Field(..., min_length=10, max_length=20)
    address_line1: str = Field(..., min_length=5, max_length=255)
    address_line2: Optional[str] = Field(None, max_length=255)
    locality: Optional[str] = Field(None, max_length=100)
    city: str = Field(..., min_length=2, max_length=100)
    state: str = Field(..., min_length=2, max_length=100)
    postal_code: str = Field(..., min_length=6, max_length=10)
    country: str = Field(default="India", max_length=100)
    address_type: str = Field(default="HOME", max_length=20)  # HOME, WORK, OTHER
    is_default: bool = False
    is_default_shipping: bool = False
    is_default_billing: bool = False

    @field_validator("postal_code")
    @classmethod
    def validate_indian_pincode(cls, v: str) -> str:
        clean_code = v.strip().replace(" ", "")
        if not re.match(r"^\d{6}$", clean_code):
            raise ValueError("Postal code must be a valid 6-digit Indian PIN code.")
        return clean_code


class AddressUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)
    phone_number: Optional[str] = Field(None, min_length=10, max_length=20)
    address_line1: Optional[str] = Field(None, min_length=5, max_length=255)
    address_line2: Optional[str] = Field(None, max_length=255)
    locality: Optional[str] = Field(None, max_length=100)
    city: Optional[str] = Field(None, min_length=2, max_length=100)
    state: Optional[str] = Field(None, min_length=2, max_length=100)
    postal_code: Optional[str] = Field(None, min_length=6, max_length=10)
    country: Optional[str] = Field(None, max_length=100)
    address_type: Optional[str] = Field(None, max_length=20)
    is_default: Optional[bool] = None
    is_default_shipping: Optional[bool] = None
    is_default_billing: Optional[bool] = None


class AddressResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    full_name: str
    phone_number: str
    address_line1: str
    address_line2: Optional[str] = None
    locality: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str
    address_type: str
    is_default: bool
    is_default_shipping: bool
    is_default_billing: bool
    created_at: datetime


class UserSessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    token_jti: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    device_type: Optional[str] = "Desktop"
    is_revoked: bool
    is_current: bool = False
    created_at: datetime
    last_active_at: datetime
    expires_at: datetime


class SecurityAuditResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: Optional[int] = None
    action: str
    entity_type: Optional[str] = None
    entity_id: Optional[str] = None
    details: Optional[str] = None
    created_at: datetime


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    full_name: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    profile_image_url: Optional[str] = None
    account_status: str = "ACTIVE"
    is_active: bool
    is_verified: bool
    preferred_language: str = "en-IN"
    preferred_currency: str = "INR"
    last_login_at: Optional[datetime] = None
    roles: List[str] = []
    permissions: List[str] = []
    created_at: datetime
    updated_at: datetime
