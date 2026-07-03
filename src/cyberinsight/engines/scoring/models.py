from pydantic import BaseModel


class SecurityScore(BaseModel):

    score: int

    grade: str

    risk: str

    breakdown: list[str]