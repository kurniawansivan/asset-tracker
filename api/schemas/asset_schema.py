"""
Asset schemas for Asset Tracker API.
"""
from datetime import date
from pydantic import BaseModel, ConfigDict

class AssetBase(BaseModel):
    """Base schema for an asset."""
    name: str
    serial_number: str | None = None
    purchase_date: date
    warranty_expires: date | None = None

class AssetCreate(AssetBase):
    """Schema for creating a new asset."""
    pass

class AssetRead(AssetBase):
    """Schema for reading an asset."""
    id: int

    model_config = ConfigDict(from_attributes=True)
