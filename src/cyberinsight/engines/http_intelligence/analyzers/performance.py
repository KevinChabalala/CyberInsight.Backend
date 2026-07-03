from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import PerformanceInfo


class PerformanceAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> PerformanceInfo:

        ms = context.response_time_ms

        if ms < 200:
            rating = "Excellent"
        elif ms < 500:
            rating = "Good"
        elif ms < 1000:
            rating = "Average"
        else:
            rating = "Poor"

        return PerformanceInfo(
            response_time_ms=round(ms, 2),
            rating=rating,
        )