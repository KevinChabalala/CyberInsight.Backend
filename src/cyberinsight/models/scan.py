import uuid

from sqlalchemy import DateTime, ForeignKey, Integer, String, func, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from cyberinsight.core.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )

    url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="PENDING",
    )

    security_score: Mapped[int] = mapped_column(
    Integer,
    default=0,
   )

    grade: Mapped[str] = mapped_column(
    String(5),
    default="N/A",
   )

    risk: Mapped[str] = mapped_column(
    String(30),
    default="Unknown",
)

    report: Mapped[dict] = mapped_column(
    JSON,
    nullable=True,
)

    created_at: Mapped[DateTime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
   )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )