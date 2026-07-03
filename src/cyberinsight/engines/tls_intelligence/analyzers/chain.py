from cyberinsight.engines.tls_intelligence.models import (
    CertificateChainInfo,
)


class ChainAnalyzer:

    @staticmethod
    def analyze(context):

        cert = context.certificate

        trusted = (
            cert.get_subject().CN
            != cert.get_issuer().CN
        )

        return CertificateChainInfo(

            chain_length=1,

            trusted=trusted,

        )