from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from cyberinsight.core.base import Base
from sqlalchemy.dialects.postgresql import UUID


class QRScanHistory(Base):
    __tablename__ = "qr_scan_history"

    id = Column(Integer, primary_key=True, index=True)

    decoded_content = Column(Text, nullable=False)

    url = Column(String(500), nullable=True)

    is_url = Column(Boolean, default=False)

    user_id = Column(
    UUID(as_uuid=True),
    ForeignKey("users.id"),
    nullable=True
)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )