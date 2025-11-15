"""
Asset model definition.
"""
from sqlalchemy import Column, Integer, String, Date
from database import Base

class Asset(Base):
    """Asset model representing an asset in the system."""
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    serial_number = Column(String, nullable=True)
    purchase_date = Column(Date, nullable=False)
    warranty_expires = Column(Date, nullable=True)
