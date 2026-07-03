from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import ContentInfo


class ContentAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> ContentInfo:

        headers = context.response.headers

        content_type = headers.get("Content-Type")

        charset = None

        if content_type and "charset=" in content_type:
            charset = content_type.split("charset=")[-1]

        return ContentInfo(
            content_type=content_type,
            charset=charset,
            content_length=headers.get("Content-Length"),
            encoding=headers.get("Content-Encoding"),
            transfer_encoding=headers.get("Transfer-Encoding"),
            compression=headers.get("Content-Encoding"),
        )