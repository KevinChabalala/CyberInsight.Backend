from urllib.parse import urlparse

from cyberinsight.engines.tls_intelligence.context import (
    TLSContext,
)
from cyberinsight.engines.tls_intelligence.models import (
    TLSIntelligenceResult,
    TLSProtocolInfo,
    CertificateInfo,
    CipherInfo,
    CertificateChainInfo,
    OCSPInfo,
    TLSHealth,
)

from cyberinsight.engines.tls_intelligence.utils.ssl_client import (
    SSLClient,
)

from cyberinsight.engines.tls_intelligence.analyzers import (
    ProtocolAnalyzer,
    CertificateAnalyzer,
    CipherAnalyzer,
    ChainAnalyzer,
    OCSPAnalyzer,
    TLSHealthAnalyzer,
)


class TLSIntelligenceEngine:

    @staticmethod
    def analyze(url: str):

        try:

            hostname = urlparse(url).hostname

            if not hostname:
                raise ValueError("Invalid hostname.")

            connection, certificate = SSLClient.connect(
                hostname
            )

            context = TLSContext(
                hostname,
                connection,
                certificate,
            )

            protocol = ProtocolAnalyzer.analyze(
                context
            )

            cert = CertificateAnalyzer.analyze(
                context
            )

            cipher = CipherAnalyzer.analyze(
                context
            )

            chain = ChainAnalyzer.analyze(
                context
            )

            ocsp = OCSPAnalyzer.analyze(
                context
            )

            health = TLSHealthAnalyzer.analyze(
                protocol,
                cert,
                cipher,
                chain,
                ocsp,
            )

            connection.close()

            return TLSIntelligenceResult(

                success=True,

                protocols=protocol,

                certificate=cert,

                cipher=cipher,

                chain=chain,

                ocsp=ocsp,

                health=health,

                error=None,

            )

        except Exception as e:

            return TLSIntelligenceResult(

                success=False,

                protocols=TLSProtocolInfo(),

                certificate=CertificateInfo(),

                cipher=CipherInfo(),

                chain=CertificateChainInfo(),

                ocsp=OCSPInfo(),

                health=TLSHealth(
                    score=0,
                    recommendations=[],
                ),

                error=str(e),

            )