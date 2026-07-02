from pydantic import BaseModel


class UrlScanResult(BaseModel):

    success: bool

    original_url: str

    normalized_url: str

    scheme: str

    domain: str