from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import (
    HTTPResponseInfo,
)


class ResponseAnalyzer:

    @staticmethod
    def analyze(
        context: HTTPScanContext,
    ) -> HTTPResponseInfo:

        response = context.response

        version_map = {
            10: "HTTP/1.0",
            11: "HTTP/1.1",
            20: "HTTP/2",
            30: "HTTP/3",
        }

        http_version = version_map.get(
            response.raw.version,
            f"HTTP/{response.raw.version}",
        )

        return HTTPResponseInfo(

            status_code=response.status_code,

            reason=response.reason,

            http_version=http_version,

            final_url=response.url,
        )