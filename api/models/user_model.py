"""
User model definition.
"""

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    """User model representing a user in the system."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)