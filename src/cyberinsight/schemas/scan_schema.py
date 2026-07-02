from uuid import UUID

from pydantic import BaseModel, ConfigDict, HttpUrl


class ScanCreate(BaseModel):
    url: HttpUrl


class ScanResponse(BaseModel):
    id: UUID
    user_id: UUID
    url: str
    status: str
    security_score: int

    model_config = ConfigDict(from_attributes=True)