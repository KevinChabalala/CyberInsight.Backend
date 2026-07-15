# src/cyberinsight/schemas/qr_code_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QRCodeBase(BaseModel):
    url: str
    domain: str
    data_url: Optional[str] = None
    user_id: Optional[int] = None

class QRCodeCreate(QRCodeBase):
    pass

class QRCodeUpdate(BaseModel):
    url: Optional[str] = None
    domain: Optional[str] = None
    data_url: Optional[str] = None

class QRCodeResponse(QRCodeBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True