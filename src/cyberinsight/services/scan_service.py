from cyberinsight.engines.url import UrlEngine
from cyberinsight.engines.dns import DnsEngine
from cyberinsight.engines.ssl import SslEngine
from cyberinsight.engines.headers import HeaderEngine
from cyberinsight.engines.technology import TechnologyEngine
from cyberinsight.engines.scoring import ScoreEngine
from cyberinsight.engines.domain import DomainEngine
from cyberinsight.engines.dns_intelligence import DNSIntelligenceEngine
from cyberinsight.engines.http_intelligence import HTTPIntelligenceEngine
from cyberinsight.schemas.scan_report import ScanReport
from cyberinsight.engines.port_intelligence import (
    PortIntelligenceEngine,
)
from cyberinsight.engines.tls_intelligence import (
    TLSIntelligenceEngine,
)

class ScanService:

    def analyze(self, url: str):

        # -------------------------
        # Run Engines
        # -------------------------

        url_result = UrlEngine.analyze(url)

        dns_result = DnsEngine.analyze(url)

        ssl_result = SslEngine.analyze(url)

        header_result = HeaderEngine.analyze(url)

        technology_engine = TechnologyEngine()
        technology_result = technology_engine.analyze(url)

        domain_result = DomainEngine.analyze(url)

        dns_intelligence_result = DNSIntelligenceEngine.analyze(url)

        http_result = HTTPIntelligenceEngine.analyze(url)

        port_result = PortIntelligenceEngine.analyze(url)

        tls_result = TLSIntelligenceEngine.analyze(url)
    

        # -------------------------
        # Calculate Security Score
        # -------------------------

        score_engine = ScoreEngine()

        security_result = score_engine.calculate(
                url_result,
                dns_result,
                dns_intelligence_result,
                domain_result,
                ssl_result,
                header_result,
                http_result,
                technology_result,
                port_result,
                tls_result,
)

        # -------------------------
        # Return Complete Report
        # -------------------------

        return ScanReport(
            url=url_result,
            dns=dns_result,
            dns_intelligence=dns_intelligence_result,
            ssl=ssl_result,
            headers=header_result,
            technology=technology_result,
            domain=domain_result,
            http_intelligence=http_result,
            port_intelligence=port_result,
            security=security_result,
            tls_intelligence=tls_result,
        )