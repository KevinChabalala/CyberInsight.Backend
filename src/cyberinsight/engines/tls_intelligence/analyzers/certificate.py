from OpenSSL.crypto import TYPE_RSA
from OpenSSL.crypto import TYPE_DSA
from OpenSSL.crypto import TYPE_EC

from cyberinsight.engines.tls_intelligence.models import (
    CertificateInfo,
)


class CertificateAnalyzer:

    @staticmethod
    def analyze(context):

        cert = context.certificate

        subject = cert.get_subject()

        issuer = cert.get_issuer()

        pubkey = cert.get_pubkey()

        algorithm = "Unknown"

        if pubkey.type() == TYPE_RSA:
            algorithm = "RSA"

        elif pubkey.type() == TYPE_DSA:
            algorithm = "DSA"

        elif pubkey.type() == TYPE_EC:
            algorithm = "EC"

        common_name = getattr(
            subject,
            "CN",
            "",
        )

        return CertificateInfo(

            subject=common_name,

            issuer=getattr(
                issuer,
                "CN",
                "",
            ),

            serial_number=str(
                cert.get_serial_number()
            ),

            signature_algorithm=cert.get_signature_algorithm().decode(),

            public_key_algorithm=algorithm,

            key_size=pubkey.bits(),

            wildcard=common_name.startswith("*."),

            self_signed=subject.CN == issuer.CN,

            ev_certificate=False,

        )