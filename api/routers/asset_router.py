"""
Asset router module for handling asset-related API endpoints."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from models import asset_model
from schemas import asset_schema
from dependencies import get_db

router = APIRouter(
    prefix="/api/assets",
    tags=["assets"],
)

@router.post("/", response_model=asset_schema.AssetRead, status_code=status.HTTP_201_CREATED)
def create_asset(asset: asset_schema.AssetCreate, db: Session = Depends(get_db)):
    """Create a new asset in the database."""
    db_asset = asset_model.Asset(**asset.model_dump())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.get("/", response_model=list[asset_schema.AssetRead])
def read_assets(db: Session = Depends(get_db)):
    """Retrieve all assets from the database."""
    assets = db.query(asset_model.Asset).all()
    return assets
