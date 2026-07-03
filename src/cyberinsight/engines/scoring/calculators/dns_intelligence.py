class DNSIntelligenceScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        if result.records.mx:
            score += rules["mx"]
            breakdown.append(f"+{rules['mx']} MX records found")

        if result.email_security.spf:
            score += rules["spf"]
            breakdown.append(f"+{rules['spf']} SPF configured")

        if result.email_security.dmarc:
            score += rules["dmarc"]
            breakdown.append(f"+{rules['dmarc']} DMARC configured")

        if result.email_security.dkim:
            score += rules["dkim"]
            breakdown.append(f"+{rules['dkim']} DKIM configured")

        if len(result.records.ns) >= 2:
            score += rules["name_servers"]
            breakdown.append(f"+{rules['name_servers']} Multiple name servers")

        return score, breakdown