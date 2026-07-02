from urllib.parse import urlparse


class UrlEngine:

    @staticmethod
    def validate(url: str) -> bool:
        parsed = urlparse(url)

        return all([
            parsed.scheme in ["http", "https"],
            parsed.netloc,
        ])

    @staticmethod
    def normalize(url: str) -> str:
        url = url.strip()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        return url.lower()