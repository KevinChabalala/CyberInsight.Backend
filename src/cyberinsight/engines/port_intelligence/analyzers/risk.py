class RiskAnalyzer:

    @staticmethod
    def summarize(results):

        high = 0

        critical = 0

        for result in results:

            if not result.open:
                continue

            if result.risk == "High":
                high += 1

            elif result.risk == "Critical":
                critical += 1

        return {

            "high": high,

            "critical": critical,

        }