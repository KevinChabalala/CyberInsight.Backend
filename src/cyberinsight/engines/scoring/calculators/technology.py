class TechnologyScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        if result.technologies:

            score += rules["detected"]
            breakdown.append(
                f"+{rules['detected']} Technologies identified"
            )

            score += rules["modern"]
            breakdown.append(
                f"+{rules['modern']} Modern technologies"
            )

            score += rules["supported"]
            breakdown.append(
                f"+{rules['supported']} Supported technologies"
            )

        return score, breakdown