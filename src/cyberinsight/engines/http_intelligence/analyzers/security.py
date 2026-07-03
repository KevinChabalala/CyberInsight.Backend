from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import HTTPSecurityInfo


class SecurityAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> HTTPSecurityInfo:

        headers = context.response.headers

        return HTTPSecurityInfo(
            hsts="Strict-Transport-Security" in headers,
            csp="Content-Security-Policy" in headers,
            x_frame_options="X-Frame-Options" in headers,
            x_content_type_options="X-Content-Type-Options" in headers,
            referrer_policy="Referrer-Policy" in headers,
            permissions_policy="Permissions-Policy" in headers,
        )