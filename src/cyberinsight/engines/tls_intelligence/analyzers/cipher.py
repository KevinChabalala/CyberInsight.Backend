from cyberinsight.engines.tls_intelligence.models import (
    CipherInfo,
)


class CipherAnalyzer:

    @staticmethod
    def analyze(context):

        cipher = context.connection.cipher()

        if cipher:

            name = cipher[0]

            protocol = cipher[1]

            bits = cipher[2]

        else:

            name = None

            protocol = None

            bits = None

        pfs = False

        if name:

            upper = name.upper()

            pfs = (
                "ECDHE" in upper
                or "DHE" in upper
            )

        return CipherInfo(

            name=name,

            protocol=protocol,

            bits=bits,

            perfect_forward_secrecy=pfs,

        )