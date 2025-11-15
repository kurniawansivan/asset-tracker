"""
User router module.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies import get_db
from models import user_model
from schemas import user_schema
from security import get_password_hash

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"],
)

@router.post("/signup", response_model=user_schema.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    """Create a new user in the database."""
    hashed_password = get_password_hash(user.password)
    db_user = user_model.User(
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
