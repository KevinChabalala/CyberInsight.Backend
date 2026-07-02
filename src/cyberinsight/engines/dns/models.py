from pydantic import BaseModel


class DnsScanResult(BaseModel):

    success: bool

    hostname: str

    ip_address: str | None = None