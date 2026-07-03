import dns.resolver

from cyberinsight.engines.dns_intelligence.models import EmailSecurity


class EmailSecurityAnalyzer:

    @staticmethod
    def analyze(domain: str) -> EmailSecurity:

        security = EmailSecurity()

        # -------------------------
        # SPF
        # -------------------------

        try:

            answers = dns.resolver.resolve(
                domain,
                "TXT",
            )

            txt_records = [

                "".join(
                    part.decode()
                    for part in answer.strings
                )

                for answer in answers

            ]

            security.spf = any(
                record.startswith("v=spf1")
                for record in txt_records
            )

        except Exception:
            pass

        # -------------------------
        # DMARC
        # -------------------------

        try:

            answers = dns.resolver.resolve(
                f"_dmarc.{domain}",
                "TXT",
            )

            txt_records = [

                "".join(
                    part.decode()
                    for part in answer.strings
                )

                for answer in answers

            ]

            security.dmarc = any(
                record.startswith("v=DMARC1")
                for record in txt_records
            )

        except Exception:
            pass

        # -------------------------
        # DKIM
        # -------------------------

        #
        # DKIM selectors are organization-specific.
        # Without knowing the selector (google, default,
        # selector1, etc.) we cannot reliably detect DKIM.
        #
        # For now we return False.
        # Later we'll implement selector discovery.
        #

        security.dkim = False

        return security