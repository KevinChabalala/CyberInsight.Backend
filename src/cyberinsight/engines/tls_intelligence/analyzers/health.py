from cyberinsight.engines.tls_intelligence.models import (
    TLSHealth,
)


class TLSHealthAnalyzer:

    @staticmethod
    def analyze(

        protocol,

        certificate,

        cipher,

        chain,

        ocsp,

    ):

        score = 100

        recommendations = []

        if not protocol.tls13:

            score -= 10

            recommendations.append(
                "Upgrade to TLS 1.3."
            )

        if certificate.self_signed:

            score -= 20

            recommendations.append(
                "Use a trusted Certificate Authority."
            )

        if not cipher.perfect_forward_secrecy:

            score -= 10

            recommendations.append(
                "Enable Perfect Forward Secrecy."
            )

        if not ocsp.stapled:

            score -= 5

            recommendations.append(
                "Enable OCSP Stapling."
            )

        score = max(
            score,
            0,
        )

        return TLSHealth(

            score=score,

            recommendations=recommendations,

        )