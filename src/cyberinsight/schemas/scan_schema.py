from pydantic import BaseModel, HttpUrl


class ScanRequest(BaseModel):

    url: HttpUrl


class ScanResponse(BaseModel):

    success: bool

    message: str