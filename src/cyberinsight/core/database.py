"""
Database configuration for CyberInsight.

This module creates:

- SQLAlchemy Engine
- Database Session
- Base Model
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from cyberinsight.config.settings import settings


# --------------------------------------------------
# Database Engine
# --------------------------------------------------

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
)


# --------------------------------------------------
# Database Session
# --------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# --------------------------------------------------
# Base Model
# --------------------------------------------------

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    """
    pass


# --------------------------------------------------
# Dependency
# --------------------------------------------------

def get_db():
    """
    Creates a database session for each request.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()