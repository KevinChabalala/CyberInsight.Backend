import socket


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

            return {
                "success": True,
                "hostname": hostname,
                "ip_address": ip,
            }

        except socket.gaierror:

            return {
                "success": False,
                "hostname": hostname,
                "ip_address": None,
            }