from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import CacheInfo


class CacheAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> CacheInfo:

        headers = context.response.headers

        return CacheInfo(
            cache_control=headers.get("Cache-Control"),
            etag=headers.get("ETag"),
            last_modified=headers.get("Last-Modified"),
            expires=headers.get("Expires"),
            age=headers.get("Age"),
            vary=headers.get("Vary"),
        )