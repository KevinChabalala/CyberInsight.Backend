from cyberinsight.engines.tls_intelligence.models import (
    OCSPInfo,
)


class OCSPAnalyzer:

    @staticmethod
    def analyze(context):

        return OCSPInfo(

            stapled=False,

        )