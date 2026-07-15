# src/cyberinsight/models/qr_code.py
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from cyberinsight.core.base import Base
from sqlalchemy.dialects.postgresql import UUID

class QRCode(Base):
    __tablename__ = "qr_codes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), nullable=False)
    domain = Column(String(255), nullable=False)
    data_url = Column(Text, nullable=True)  # Base64 encoded QR code image
    user_id = Column(
    UUID(as_uuid=True),
    ForeignKey("users.id"),
    nullable=True
)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
    DateTime(timezone=True),
    server_default=func.now(),
    onupdate=func.now()
)
    
    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "domain": self.domain,
            "data_url": self.data_url,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }