import requests
from cyberinsight.engines.headers.models import (
    HeaderScanResult,
    SecurityHeader,
)

class HeaderEngine:

    SECURITY_HEADERS = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy",
    ]

    @staticmethod
    def analyze(url: str):

        try:

            response = requests.get(
                url,
                timeout=10,
            )

            headers = response.headers

            results = {}

            for header in HeaderEngine.SECURITY_HEADERS:
                results[header] = {
                    "present": header in headers,
                    "value": headers.get(header),
                }

            return HeaderScanResult(
    success=True,
    headers={
        key: SecurityHeader(**value)
        for key, value in results.items()
    },
)

        except Exception as e:
            return HeaderScanResult(
    success=False,
    headers={},
    error=str(e),
)