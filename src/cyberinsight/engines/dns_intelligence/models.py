from pydantic import BaseModel


class MXRecord(BaseModel):
    priority: int
    host: str


class SOARecord(BaseModel):
    primary_server: str | None = None
    admin_email: str | None = None
    serial: int | None = None


class DNSRecords(BaseModel):
    a: list[str] = []
    aaaa: list[str] = []
    mx: list[MXRecord] = []
    ns: list[str] = []
    txt: list[str] = []
    cname: list[str] = []
    soa: SOARecord = SOARecord()


class EmailSecurity(BaseModel):
    spf: bool = False
    dmarc: bool = False
    dkim: bool = False


class DNSHealth(BaseModel):
    score: int
    recommendations: list[str] = []


class DNSIntelligenceResult(BaseModel):
    success: bool
    records: DNSRecords
    email_security: EmailSecurity
    health: DNSHealth
    error: str | None = None