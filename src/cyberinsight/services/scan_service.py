from cyberinsight.engines.url_engine import UrlEngine
from cyberinsight.engines.dns_engine import DnsEngine
from cyberinsight.engines.ssl_engine import SslEngine
from cyberinsight.engines.header_engine import HeaderEngine
from cyberinsight.engines.technology_engine import TechnologyEngine
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

        technology_result = TechnologyEngine.analyze(url)

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