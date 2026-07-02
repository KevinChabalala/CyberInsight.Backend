import socket
from cyberinsight.engines.dns.models import DnsScanResult

class DnsEngine:

    @staticmethod
    def analyze(url: str):
        """
        Resolve a domain name to an IP address.
        """

        hostname = url.replace("https://", "").replace("http://", "")
        hostname = hostname.split("/")[0]

        try:
            ip = socket.gethostbyname(hostname)

            return DnsScanResult(
                   success=True,
                   hostname=hostname,
                   ip_address=ip,
)

        except socket.gaierror:

            return DnsScanResult(
    success=False,
    hostname=hostname,
    ip_address=None,
)