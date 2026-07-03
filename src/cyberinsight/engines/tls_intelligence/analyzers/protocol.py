import ssl

from cyberinsight.engines.tls_intelligence.models import (
    TLSProtocolInfo,
)


class ProtocolAnalyzer:

    @staticmethod
    def analyze(context):

        protocol = context.connection.version()

        return TLSProtocolInfo(

            tls10=protocol == "TLSv1",

            tls11=protocol == "TLSv1.1",

            tls12=protocol == "TLSv1.2",

            tls13=protocol == "TLSv1.3",

            ssl2=False,

            ssl3=False,

        )