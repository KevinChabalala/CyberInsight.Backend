from datetime import datetime
from uuid import UUID
from typing import Any

from pydantic import BaseModel


class ScanHistoryItem(BaseModel):
    id: UUID
    url: str
    security_score: int
    grade: str
    risk: str
    status: str
    created_at: datetime

    report: dict[str, Any] | None = None

    model_config = {
        "from_attributes": True
    }