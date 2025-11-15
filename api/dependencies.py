"""
Dependency injection for database session.
"""
from database import SessionLocal

def get_db():
    """Yield a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
