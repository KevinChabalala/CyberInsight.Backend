from pydantic import BaseModel


class SslScanResult(BaseModel):

    success: bool

    issuer: str | None = None

    expires: str | None = None

    days_remaining: int | None = None

    valid: bool | None = None

    error: str | None = None