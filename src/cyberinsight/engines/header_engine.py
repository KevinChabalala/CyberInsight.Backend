import requests


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

            return {
                "success": True,
                "headers": results,
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }