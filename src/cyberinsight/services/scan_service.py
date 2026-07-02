from cyberinsight.engines.url_engine import UrlEngine
from cyberinsight.engines.dns_engine import DnsEngine
from cyberinsight.engines.ssl_engine import SslEngine
from cyberinsight.engines.header_engine import HeaderEngine
from cyberinsight.engines.technology_engine import TechnologyEngine


class ScanService:

    def analyze(self, url: str):

        url_result = UrlEngine.analyze(url)

        dns_result = DnsEngine.analyze(url)

        ssl_result = SslEngine.analyze(url)

        header_result = HeaderEngine.analyze(url)

        technology_result = TechnologyEngine.analyze(url)

        return {
            "url": url_result,
            "dns": dns_result,
            "ssl": ssl_result,
            "headers": header_result,
            "technology": technology_result,
        }