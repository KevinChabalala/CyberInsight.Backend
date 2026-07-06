from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ScanDetailResponse(BaseModel):
    id: UUID
    url: str
    security_score: int
    grade: str
    risk: str
    status: str
    report: dict | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }