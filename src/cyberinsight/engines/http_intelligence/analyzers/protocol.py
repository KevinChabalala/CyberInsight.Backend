from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import ProtocolInfo


class ProtocolAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> ProtocolInfo:

        response = context.response

        version = response.raw.version

        return ProtocolInfo(
            https=response.url.startswith("https://"),
            http_version=f"HTTP/{version}",
            http2=version == 20,
            http3="h3" in str(response.headers.get("Alt-Svc", "")).lower(),
        )