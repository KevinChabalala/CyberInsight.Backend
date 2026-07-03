from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import ServerInfo


class ServerAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> ServerInfo:

        headers = context.response.headers

        return ServerInfo(
            server=headers.get("Server"),
            powered_by=headers.get("X-Powered-By"),
            via=headers.get("Via"),
            alt_svc=headers.get("Alt-Svc"),
            date=headers.get("Date"),
        )