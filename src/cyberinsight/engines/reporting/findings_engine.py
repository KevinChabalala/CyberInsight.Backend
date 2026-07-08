from cyberinsight.engines.scoring.models import Finding


class FindingsEngine:

    @staticmethod
    def generate(
        url_result,
        dns_result,
        dns_intelligence_result,
        domain_result,
        ssl_result,
        tls_result,
        header_result,
        http_result,
        technology_result,
        port_result,
    ):

        findings = []

        # URL
        if url_result.success:
            findings.append(
                Finding(
                    module="URL",
                    status="PASS",
                    message="The website URL is valid.",
                )
            )

        # DNS
        if dns_result.success:
            findings.append(
                Finding(
                    module="DNS",
                    status="PASS",
                    message="DNS records were successfully resolved.",
                )
            )

        # SSL
        if ssl_result.success and ssl_result.valid:
            findings.append(
                Finding(
                    module="SSL Certificate",
                    status="PASS",
                    message="A valid SSL certificate was detected.",
                )
            )

        # TLS
        if tls_result.success and tls_result.protocols.tls13:
            findings.append(
                Finding(
                    module="TLS",
                    status="PASS",
                    message="TLS 1.3 is supported.",
                )
            )

        # HTTP
        if http_result.success and http_result.protocol.https:
            findings.append(
                Finding(
                    module="HTTPS",
                    status="PASS",
                    message="HTTPS is enabled.",
                )
            )

        # Headers
        if header_result.success:
            findings.append(
                Finding(
                    module="Security Headers",
                    status="PASS",
                    message="Security headers were analyzed.",
                )
            )

        # Technologies
        if technology_result.success:
            findings.append(
                Finding(
                    module="Technologies",
                    status="PASS",
                    message=f"{len(technology_result.technologies)} technologies detected.",
                )
            )

        # Ports
        if (
            port_result.success
            and port_result.summary.high_risk_ports == 0
        ):
            findings.append(
                Finding(
                    module="Network Ports",
                    status="PASS",
                    message="No high-risk ports were detected.",
                )
            )

        return findings