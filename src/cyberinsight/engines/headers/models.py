from pydantic import BaseModel


class SecurityHeader(BaseModel):

    present: bool

    value: str | None = None


class HeaderScanResult(BaseModel):

    success: bool

    headers: dict[str, SecurityHeader]

    error: str | None = None