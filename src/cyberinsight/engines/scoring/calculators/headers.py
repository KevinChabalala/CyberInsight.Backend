class HeaderScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        for header, info in result.headers.items():

            if info.present:

                points = rules.get(header, 0)

                score += points

                breakdown.append(
                    f"+{points} {header}"
                )

        return score, breakdown