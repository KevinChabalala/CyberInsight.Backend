from urllib.parse import urlparse

from cyberinsight.engines.dns_intelligence.analyzers.email_security import (
    EmailSecurityAnalyzer,
)
from cyberinsight.engines.dns_intelligence.analyzers.health import (
    DNSHealthAnalyzer,
)
from cyberinsight.engines.dns_intelligence.analyzers.records import (
    DNSRecordsAnalyzer,
)
from cyberinsight.engines.dns_intelligence.models import (
    DNSHealth,
    DNSIntelligenceResult,
    DNSRecords,
    EmailSecurity,
)


class DNSIntelligenceEngine:

    @staticmethod
    def analyze(url: str) -> DNSIntelligenceResult:

        try:

            domain = urlparse(url).hostname

            if not domain:
                raise ValueError("Invalid URL")

            records = DNSRecordsAnalyzer.get_records(
                domain
            )

            email = EmailSecurityAnalyzer.analyze(
                domain
            )

            # -------------------------
            # Determine if DNS data exists
            # -------------------------

            has_dns_data = any(
                [
                    records.a,
                    records.aaaa,
                    records.mx,
                    records.ns,
                    records.txt,
                    records.cname,
                    records.soa.primary_server,
                ]
            )

            # -------------------------
            # DNS Health
            # -------------------------

            if has_dns_data:

                health = DNSHealthAnalyzer.analyze(
                    records,
                    email,
                )

            else:

                health = DNSHealth(
                    score=0,
                    recommendations=[],
                )

            return DNSIntelligenceResult(
                success=has_dns_data,
                records=records,
                email_security=email,
                health=health,
                error=None if has_dns_data else "No DNS records were found.",
            )

        except Exception as e:

            return DNSIntelligenceResult(
                success=False,
                records=DNSRecords(),
                email_security=EmailSecurity(),
                health=DNSHealth(
                    score=0,
                    recommendations=[],
                ),
                error=str(e),
            )