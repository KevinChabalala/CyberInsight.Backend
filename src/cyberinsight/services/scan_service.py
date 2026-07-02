from cyberinsight.engines.url import UrlEngine
from cyberinsight.engines.dns import DnsEngine
from cyberinsight.engines.ssl import SslEngine
from cyberinsight.engines.headers import HeaderEngine
from cyberinsight.engines.technology import TechnologyEngine
from cyberinsight.engines.score_engine import ScoreEngine


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

        # -------------------------
        # Calculate Security Score
        # -------------------------

        score_engine = ScoreEngine()

        security_result = score_engine.calculate(
            dns_result,
            ssl_result,
            header_result,
            technology_result,
        )

        # -------------------------
        # Return Complete Report
        # -------------------------

        return {
            "url": url_result,
            "dns": dns_result,
            "ssl": ssl_result,
            "headers": header_result,
            "technology": technology_result,
            "security": security_result,
        }