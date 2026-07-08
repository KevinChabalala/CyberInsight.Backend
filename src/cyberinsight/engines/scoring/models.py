from pydantic import BaseModel


class Finding(BaseModel):
    module: str
    status: str
    message: str


class Recommendation(BaseModel):
    priority: str
    title: str
    description: str


class SecurityScore(BaseModel):

    score: int

    rating: str

    risk: str

    findings: list[Finding]

    recommendations: list[Recommendation]