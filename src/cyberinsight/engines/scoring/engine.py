import json
from pathlib import Path

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

        rules_file = (
            Path(__file__).parent
            / "scoring_rules.json"
        )

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
        breakdown = []

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

            score, items = calculator.calculate(
                result,
                rules,
            )

            total_score += score
            breakdown.extend(items)

        total_score = min(total_score, 100)

        grade, risk = self.calculate_grade(total_score)

        return SecurityScore(
            score=total_score,
            grade=grade,
            risk=risk,
            breakdown=breakdown,
        )

    @staticmethod
    def calculate_grade(score: int):

        if score >= 97:
            return "A+", "Excellent"

        if score >= 93:
            return "A", "Very Low"

        if score >= 90:
            return "A-", "Very Low"

        if score >= 87:
            return "B+", "Low"

        if score >= 83:
            return "B", "Low"

        if score >= 80:
            return "B-", "Low"

        if score >= 75:
            return "C+", "Medium"

        if score >= 70:
            return "C", "Medium"

        if score >= 65:
            return "C-", "Medium"

        if score >= 60:
            return "D", "High"

        return "F", "Critical"