class DNSScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if result.success:

            score += rules["resolved"]

            breakdown.append(
                f"+{rules['resolved']} DNS resolved"
            )

        return score, breakdown