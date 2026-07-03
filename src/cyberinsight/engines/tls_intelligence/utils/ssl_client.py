import socket
import ssl

from OpenSSL import crypto


class SSLClient:

    @staticmethod
    def connect(hostname: str):

        context = ssl.create_default_context()

        sock = socket.create_connection(
            (hostname, 443),
            timeout=10,
        )

        ssl_socket = context.wrap_socket(
            sock,
            server_hostname=hostname,
        )

        certificate = ssl_socket.getpeercert(
            binary_form=True,
        )

        x509 = crypto.load_certificate(
            crypto.FILETYPE_ASN1,
            certificate,
        )

        return ssl_socket, x509