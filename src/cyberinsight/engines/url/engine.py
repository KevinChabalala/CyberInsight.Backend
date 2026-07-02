from urllib.parse import urlparse
from cyberinsight.engines.url.models import UrlScanResult

class UrlEngine:

    @staticmethod
    def analyze(url: str):

        normalized_url = UrlEngine.normalize(url)

        is_valid = UrlEngine.validate(normalized_url)

        return UrlScanResult(
               success=is_valid,
               original_url=url,
               normalized_url=normalized_url,
               scheme=urlparse(normalized_url).scheme,
               domain=urlparse(normalized_url).netloc,
)

    @staticmethod
    def validate(url: str) -> bool:

        parsed = urlparse(url)

        return all(
            [
                parsed.scheme in ["http", "https"],
                parsed.netloc,
            ]
        )

    @staticmethod
    def normalize(url: str) -> str:

        url = url.strip()

        if not url.startswith(
            (
                "http://",
                "https://",
            )
        ):
            url = "https://" + url

        return url.lower()