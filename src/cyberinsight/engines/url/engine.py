from urllib.parse import urlparse

from cyberinsight.engines.url.models import UrlScanResult


class UrlEngine:

    @staticmethod
    def analyze(url: str) -> UrlScanResult:

        normalized_url = UrlEngine.normalize(url)

        is_valid = UrlEngine.validate(normalized_url)

        parsed = urlparse(normalized_url)

        return UrlScanResult(
            success=is_valid,
            original_url=url,
            normalized_url=normalized_url,
            scheme=parsed.scheme,
            domain=parsed.netloc,
        )

    @staticmethod
    def validate(url: str) -> bool:

        parsed = urlparse(url)

        return all(
            [
                parsed.scheme in ("http", "https"),
                bool(parsed.netloc),
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