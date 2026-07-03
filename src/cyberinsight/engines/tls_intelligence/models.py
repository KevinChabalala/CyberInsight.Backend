from pydantic import BaseModel


class TLSProtocolInfo(BaseModel):
    tls10: bool = False
    tls11: bool = False
    tls12: bool = False
    tls13: bool = False
    ssl2: bool = False
    ssl3: bool = False


class CertificateInfo(BaseModel):
    subject: str | None = None
    issuer: str | None = None
    serial_number: str | None = None
    signature_algorithm: str | None = None
    public_key_algorithm: str | None = None
    key_size: int | None = None
    wildcard: bool = False
    self_signed: bool = False
    ev_certificate: bool = False


class CipherInfo(BaseModel):
    name: str | None = None
    protocol: str | None = None
    bits: int | None = None
    perfect_forward_secrecy: bool = False


class CertificateChainInfo(BaseModel):
    chain_length: int = 0
    trusted: bool = False


class OCSPInfo(BaseModel):
    stapled: bool = False


class TLSHealth(BaseModel):
    score: int
    recommendations: list[str]


class TLSIntelligenceResult(BaseModel):
    success: bool
    protocols: TLSProtocolInfo
    certificate: CertificateInfo
    cipher: CipherInfo
    chain: CertificateChainInfo
    ocsp: OCSPInfo
    health: TLSHealth
    error: str | None = None