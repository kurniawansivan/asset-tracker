"""
User schema module.
"""

from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    """Base schema for a user."""
    email: str

class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str

class UserRead(UserBase):
    """Schema for reading a user."""
    id: int

    model_config = ConfigDict(from_attributes=True)
