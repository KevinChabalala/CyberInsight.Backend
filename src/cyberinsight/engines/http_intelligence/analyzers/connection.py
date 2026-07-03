from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import ConnectionInfo


class ConnectionAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> ConnectionInfo:

        headers = context.response.headers

        return ConnectionInfo(
            connection=headers.get("Connection"),
            keep_alive=headers.get("Keep-Alive"),
            accept_ranges=headers.get("Accept-Ranges"),
        )