from datetime import datetime
from pydantic import BaseModel


class RegistrarInfo(BaseModel):
    name: str | None = None
    iana_id: str | None = None
    url: str | None = None
    abuse_email: str | None = None
    abuse_phone: str | None = None


class RegistrationInfo(BaseModel):
    created: datetime | None = None
    updated: datetime | None = None
    expires: datetime | None = None
    domain_age_years: int | None = None
    days_until_expiry: int | None = None
    expired: bool = False


class OwnerInfo(BaseModel):
    organization: str | None = None
    country: str | None = None


class DNSInfo(BaseModel):
    dnssec: bool | None = None
    name_servers: list[str] = []


class DomainScanResult(BaseModel):
    success: bool

    domain: str

    registrar: RegistrarInfo

    registration: RegistrationInfo

    status: list[str] = []

    dns: DNSInfo

    owner: OwnerInfo

    error: str | None = None