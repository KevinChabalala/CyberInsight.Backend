from pydantic import BaseModel


# --------------------------------------------------
# Response
# --------------------------------------------------

class HTTPResponseInfo(BaseModel):

    status_code: int | None = None

    reason: str | None = None

    http_version: str | None = None

    final_url: str | None = None


# --------------------------------------------------
# Redirects
# --------------------------------------------------

class RedirectInfo(BaseModel):

    count: int = 0

    chain: list[str] = []

    redirect_codes: list[int] = []

    https_upgrade: bool = False

    infinite_redirect: bool = False


# --------------------------------------------------
# Server
# --------------------------------------------------

class ServerInfo(BaseModel):

    server: str | None = None

    powered_by: str | None = None

    via: str | None = None

    alt_svc: str | None = None

    date: str | None = None


# --------------------------------------------------
# Content
# --------------------------------------------------

class ContentInfo(BaseModel):

    content_type: str | None = None

    charset: str | None = None

    content_length: int | None = None

    encoding: str | None = None

    transfer_encoding: str | None = None

    compression: str | None = None


# --------------------------------------------------
# Cache
# --------------------------------------------------

class CacheInfo(BaseModel):

    cache_control: str | None = None

    etag: str | None = None

    last_modified: str | None = None

    expires: str | None = None

    age: str | None = None

    vary: str | None = None


# --------------------------------------------------
# Connection
# --------------------------------------------------

class ConnectionInfo(BaseModel):

    connection: str | None = None

    keep_alive: str | None = None

    accept_ranges: str | None = None


# --------------------------------------------------
# Cookies
# --------------------------------------------------

class CookieInfo(BaseModel):

    count: int = 0

    secure: int = 0

    http_only: int = 0

    same_site: list[str] = []

    domains: list[str] = []

    paths: list[str] = []


# --------------------------------------------------
# Protocol
# --------------------------------------------------

class ProtocolInfo(BaseModel):

    https: bool = False

    http_version: str | None = None

    http2: bool = False

    http3: bool = False


# --------------------------------------------------
# Performance
# --------------------------------------------------

class PerformanceInfo(BaseModel):

    response_time_ms: float = 0

    rating: str | None = None


# --------------------------------------------------
# Security
# --------------------------------------------------

class HTTPSecurityInfo(BaseModel):

    hsts: bool = False

    csp: bool = False

    x_frame_options: bool = False

    x_content_type_options: bool = False

    referrer_policy: bool = False

    permissions_policy: bool = False


# --------------------------------------------------
# Final Result
# --------------------------------------------------

class HTTPIntelligenceResult(BaseModel):

    success: bool

    response: HTTPResponseInfo

    redirects: RedirectInfo

    server: ServerInfo

    content: ContentInfo

    cache: CacheInfo

    connection: ConnectionInfo

    cookies: CookieInfo

    protocol: ProtocolInfo

    performance: PerformanceInfo

    security: HTTPSecurityInfo

    error: str | None = None