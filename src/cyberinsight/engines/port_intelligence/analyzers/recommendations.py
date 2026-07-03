class RecommendationAnalyzer:

    @staticmethod
    def summarize(results):

        recommendations = []

        for result in results:

            if result.open:

                recommendations.append(
                    result.recommendation
                )

        return list(
            dict.fromkeys(
                recommendations
            )
        )