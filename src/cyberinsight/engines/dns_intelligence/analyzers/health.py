from cyberinsight.engines.dns_intelligence.models import (
    DNSHealth,
    DNSRecords,
    EmailSecurity,
)


class DNSHealthAnalyzer:

    @staticmethod
    def analyze(
        records: DNSRecords,
        email: EmailSecurity,
    ) -> DNSHealth:

        score = 100

        recommendations = []

        # -------------------------
        # MX Records
        # -------------------------

        if not records.mx:

            score -= 15

            recommendations.append(
                "No MX records found."
            )

        # -------------------------
        # Name Servers
        # -------------------------

        if len(records.ns) < 2:

            score -= 10

            recommendations.append(
                "At least two authoritative name servers are recommended."
            )

        # -------------------------
        # SPF
        # -------------------------

        if not email.spf:

            score -= 20

            recommendations.append(
                "Publish an SPF record to help prevent email spoofing."
            )

        # -------------------------
        # DMARC
        # -------------------------

        if not email.dmarc:

            score -= 25

            recommendations.append(
                "Publish a DMARC policy."
            )

        # -------------------------
        # DKIM
        # -------------------------

        if not email.dkim:

            score -= 15

            recommendations.append(
                "Enable DKIM email signing."
            )

        score = max(0, score)

        return DNSHealth(
            score=score,
            recommendations=recommendations,
        )