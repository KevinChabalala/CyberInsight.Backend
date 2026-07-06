from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RecentScan(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    url: str
    security_score: int
    grade: str
    risk: str
    created_at: datetime


class DashboardResponse(BaseModel):
    total_scans: int
    average_score: int
    highest_score: int
    lowest_score: int
    critical_scans: int
    recent_scans: list[RecentScan]