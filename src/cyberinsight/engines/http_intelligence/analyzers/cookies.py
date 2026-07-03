from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import CookieInfo


class CookieAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> CookieInfo:

        cookies = context.response.cookies

        secure = 0
        httponly = 0
        samesite = []
        domains = []
        paths = []

        for cookie in cookies:

            if cookie.secure:
                secure += 1

            if "HttpOnly" in str(cookie._rest):
                httponly += 1

            if "SameSite" in cookie._rest:
                samesite.append(cookie._rest["SameSite"])

            if cookie.domain:
                domains.append(cookie.domain)

            if cookie.path:
                paths.append(cookie.path)

        return CookieInfo(
            count=len(cookies),
            secure=secure,
            http_only=httponly,
            same_site=list(set(samesite)),
            domains=list(set(domains)),
            paths=list(set(paths)),
        )