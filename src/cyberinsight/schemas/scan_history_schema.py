from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ScanHistoryItem(BaseModel):
    id: UUID
    url: str
    security_score: int
    grade: str
    risk: str
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }