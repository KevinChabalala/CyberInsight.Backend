from pydantic import BaseModel

from cyberinsight.engines.url.models import UrlScanResult
from cyberinsight.engines.dns.models import DnsScanResult
from cyberinsight.engines.ssl.models import SslScanResult
from cyberinsight.engines.headers.models import HeaderScanResult
from cyberinsight.engines.technology.models import TechnologyScanResult
from cyberinsight.engines.domain.models import DomainScanResult
from cyberinsight.engines.dns_intelligence.models import DNSIntelligenceResult
from cyberinsight.engines.scoring.models import SecurityScore
from cyberinsight.engines.http_intelligence.models import HTTPIntelligenceResult
from cyberinsight.engines.port_intelligence.models import (
    PortIntelligenceResult,
)
from cyberinsight.engines.tls_intelligence.models import (
    TLSIntelligenceResult,
)

class ScanReport(BaseModel):

    url: UrlScanResult

    dns: DnsScanResult

    dns_intelligence: DNSIntelligenceResult

    ssl: SslScanResult

    tls_intelligence: TLSIntelligenceResult

    headers: HeaderScanResult

    technology: TechnologyScanResult

    domain: DomainScanResult

    http_intelligence: HTTPIntelligenceResult

    port_intelligence: PortIntelligenceResult

    security: SecurityScore

   