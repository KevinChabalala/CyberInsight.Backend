from pydantic import BaseModel


class DetectedTechnology(BaseModel):

    name: str

    category: str

    confidence: int

    matched_by: list[str]

    version: str | None = None


class TechnologyScanResult(BaseModel):

    success: bool

    technologies: list[DetectedTechnology]

    error: str | None = None