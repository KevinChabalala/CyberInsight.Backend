from cyberinsight.engines.scoring.models import Recommendation


class RecommendationsEngine:

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

        recommendations = []

        # SSL
        if not ssl_result.valid:
            recommendations.append(
                Recommendation(
                    priority="High",
                    title="Install a valid SSL certificate",
                    description="Your website should use a trusted SSL certificate to protect data transmitted between users and the server.",
                )
            )

        elif ssl_result.days_remaining is not None and ssl_result.days_remaining < 30:
            recommendations.append(
                Recommendation(
                    priority="Medium",
                    title="Renew SSL certificate",
                    description="Your SSL certificate is close to expiring. Renew it before expiration.",
                )
            )

        # TLS
        if not tls_result.protocols.tls13:
            recommendations.append(
                Recommendation(
                    priority="Medium",
                    title="Enable TLS 1.3",
                    description="Upgrade your server configuration to support TLS 1.3 for stronger encryption.",
                )
            )

        # HTTPS
        if not http_result.protocol.https:
            recommendations.append(
                Recommendation(
                    priority="High",
                    title="Enable HTTPS",
                    description="Redirect all HTTP traffic to HTTPS to protect users from interception attacks.",
                )
            )

        # DNSSEC
        if not domain_result.dns.dnssec:
            recommendations.append(
                Recommendation(
                    priority="Medium",
                    title="Enable DNSSEC",
                    description="DNSSEC protects your domain from DNS spoofing and cache poisoning attacks.",
                )
            )

        # Ports
        if port_result.summary.high_risk_ports > 0:
            recommendations.append(
                Recommendation(
                    priority="High",
                    title="Close high-risk ports",
                    description="Close or secure unnecessary open ports to reduce the attack surface.",
                )
            )

        # Technologies
        if technology_result.technologies:
            recommendations.append(
                Recommendation(
                    priority="Low",
                    title="Keep technologies updated",
                    description="Regularly update all detected frameworks, servers and libraries with the latest security patches.",
                )
            )

        # If everything looks good
        if len(recommendations) == 0:
            recommendations.append(
                Recommendation(
                    priority="Info",
                    title="No major security issues detected",
                    description="Continue monitoring your website and keep software updated.",
                )
            )

        return recommendations