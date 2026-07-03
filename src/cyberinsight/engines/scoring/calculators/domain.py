class DomainScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        score += rules["registered"]
        breakdown.append(f"+{rules['registered']} Domain registered")

        if result.registration.domain_age_years is not None:

            if result.registration.domain_age_years >= 2:

                score += rules["age"]
                breakdown.append(f"+{rules['age']} Mature domain")

        if not result.registration.expired:

            score += rules["not_expired"]
            breakdown.append(f"+{rules['not_expired']} Domain active")

        if result.dns.dnssec:

            score += rules["dnssec"]
            breakdown.append(f"+{rules['dnssec']} DNSSEC enabled")

        if result.registrar.name:

            score += rules["registrar"]
            breakdown.append(f"+{rules['registrar']} Registrar available")

        return score, breakdown