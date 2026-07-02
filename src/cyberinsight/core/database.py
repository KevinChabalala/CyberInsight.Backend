from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cyberinsight.config.settings import settings
from cyberinsight.core.base import Base


engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()