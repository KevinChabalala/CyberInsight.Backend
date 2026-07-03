class SSLScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        if result.valid:

            score += rules["valid_certificate"]

            breakdown.append(
                f"+{rules['valid_certificate']} Valid certificate"
            )

        if result.days_remaining and result.days_remaining > 90:

            score += rules["expires_90_days"]

            breakdown.append(
                f"+{rules['expires_90_days']} Certificate validity >90 days"
            )

        if result.issuer:

            score += rules["trusted_issuer"]

            breakdown.append(
                f"+{rules['trusted_issuer']} Trusted issuer"
            )

        return score, breakdown