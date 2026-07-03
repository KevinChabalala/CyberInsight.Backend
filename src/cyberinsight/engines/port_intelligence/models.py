from pydantic import BaseModel


class PortResult(BaseModel):

    port: int

    open: bool

    service: str | None = None

    risk: str | None = None

    description: str | None = None

    recommendation: str | None = None


class PortSummary(BaseModel):

    total_scanned: int

    open_ports: int

    high_risk_ports: int


class PortIntelligenceResult(BaseModel):

    success: bool

    summary: PortSummary

    ports: list[PortResult]

    error: str | None = None