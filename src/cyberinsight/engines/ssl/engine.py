import socket
import ssl
from datetime import datetime, timezone
from urllib.parse import urlparse
from cyberinsight.engines.ssl.models import SslScanResult

class SslEngine:

    @staticmethod
    def analyze(url: str):
        try:
            hostname = urlparse(url).hostname

            context = ssl.create_default_context()

            with socket.create_connection((hostname, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as secure_socket:

                    certificate = secure_socket.getpeercert()

                    issuer = dict(
                        x[0]
                        for x in certificate["issuer"]
                    )

                    expires = datetime.strptime(
                        certificate["notAfter"],
                        "%b %d %H:%M:%S %Y %Z",
                    ).replace(tzinfo=timezone.utc)

                    now = datetime.now(timezone.utc)

                    days_remaining = (expires - now).days

                    return SslScanResult(
    success=True,
    issuer=issuer.get("organizationName"),
    expires=expires.isoformat(),
    days_remaining=days_remaining,
    valid=days_remaining > 0,
)

        except Exception as e:
            return SslScanResult(
    success=False,
    error=str(e),
)