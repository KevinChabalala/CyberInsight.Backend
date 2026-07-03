class URLScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if result.success:

            score += rules["valid"]

            breakdown.append(
                f"+{rules['valid']} Valid URL"
            )

        if result.scheme == "https":

            score += rules["https"]

            breakdown.append(
                f"+{rules['https']} HTTPS enabled"
            )

        return score, breakdown