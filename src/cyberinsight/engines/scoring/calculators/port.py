class PortScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0

        breakdown = []

        if not result.success:

            return score, breakdown

        if result.summary.open_ports:

            score += rules["scan"]

            breakdown.append(
                f"+{rules['scan']} Port scan completed"
            )

        if result.summary.high_risk_ports == 0:

            score += rules["safe"]

            breakdown.append(
                f"+{rules['safe']} No high-risk ports exposed"
            )

        return score, breakdown