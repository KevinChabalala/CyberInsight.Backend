import json
from pathlib import Path
from cyberinsight.engines.reporting.findings_engine import FindingsEngine
from cyberinsight.engines.reporting.recommendations_engine import RecommendationsEngine
from cyberinsight.engines.scoring.models import SecurityScore
from cyberinsight.engines.scoring.calculators import (
    URLScoreCalculator,
    DNSScoreCalculator,
    DNSIntelligenceScoreCalculator,
    DomainScoreCalculator,
    SSLScoreCalculator,
    HeaderScoreCalculator,
    HTTPScoreCalculator,
    TechnologyScoreCalculator,
    PortScoreCalculator,
    TLSScoreCalculator,
)


class ScoreEngine:

    def __init__(self):

        rules_file = Path(__file__).parent / "scoring_rules.json"

        with open(
            rules_file,
            "r",
            encoding="utf-8",
        ) as file:

            self.rules = json.load(file)

    def calculate(
        self,
        url_result,
        dns_result,
        dns_intelligence_result,
        domain_result,
        ssl_result,
        header_result,
        http_result,
        technology_result,
        port_result,
        tls_result,
    ):

        total_score = 0

        calculators = [
            (
                URLScoreCalculator,
                url_result,
                self.rules["url"],
            ),
            (
                DNSScoreCalculator,
                dns_result,
                self.rules["dns"],
            ),
            (
                DNSIntelligenceScoreCalculator,
                dns_intelligence_result,
                self.rules["dns_intelligence"],
            ),
            (
                DomainScoreCalculator,
                domain_result,
                self.rules["domain"],
            ),
            (
                SSLScoreCalculator,
                ssl_result,
                self.rules["ssl"],
            ),
            (
                TLSScoreCalculator,
                tls_result,
                self.rules["tls"],
            ),
            (
                HeaderScoreCalculator,
                header_result,
                self.rules["headers"],
            ),
            (
                HTTPScoreCalculator,
                http_result,
                self.rules["http"],
            ),
            (
                PortScoreCalculator,
                port_result,
                self.rules["ports"],
            ),
            (
                TechnologyScoreCalculator,
                technology_result,
                self.rules["technology"],
            ),
        ]

        for calculator, result, rules in calculators:

            score, _ = calculator.calculate(
                result,
                rules,
            )

            total_score += score

        total_score = min(total_score, 100)

        rating, risk = self.calculate_rating(total_score)

        findings = FindingsEngine.generate(
            url_result,
            dns_result,
            dns_intelligence_result,
            domain_result,
            ssl_result,
            tls_result,
            header_result,
            http_result,
            technology_result,
            port_result,
        )

        recommendations = RecommendationsEngine.generate(
            url_result,
            dns_result,
            dns_intelligence_result,
            domain_result,
            ssl_result,
            tls_result,
            header_result,
            http_result,
            technology_result,
            port_result,
        )

        return SecurityScore(
            score=total_score,
            rating=rating,
            risk=risk,
            findings=findings,
            recommendations=recommendations,
        )

    @staticmethod
    def calculate_rating(score: int):

        if score >= 90:
           return "Excellent", "Very Low"

        if score >= 80:
           return "Good", "Low"

        if score >= 70:
            return "Fair", "Medium"

        if score >= 60:
            return "Poor", "High"

        return "Critical", "Critical"
