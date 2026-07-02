import json
from pathlib import Path


class ScoreEngine:

    def __init__(self):

        rules_file = (
            Path(__file__).parent
            / "scoring"
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
        dns_result,
        ssl_result,
        header_result,
        technology_result,
    ):

        score = 0
        breakdown = []

        # -------------------------
        # DNS
        # -------------------------

        if dns_result["success"]:

            points = self.rules["dns"]["resolved"]

            score += points

            breakdown.append(
                f"+{points} DNS resolved successfully"
            )

        # -------------------------
        # SSL
        # -------------------------

        if ssl_result["success"]:

            if ssl_result["valid"]:

                points = self.rules["ssl"]["valid_certificate"]

                score += points

                breakdown.append(
                    f"+{points} Valid SSL certificate"
                )

            else:

                points = self.rules["ssl"]["expired_certificate"]

                score += points

                breakdown.append(
                    f"{points} Expired SSL certificate"
                )

        # -------------------------
        # Headers
        # -------------------------

        for header, info in header_result["headers"].items():

            if info["present"]:

                points = self.rules["headers"].get(
                    header,
                    0,
                )

                score += points

                breakdown.append(
                    f"+{points} {header}"
                )

        # -------------------------
        # Technology
        # -------------------------

        if technology_result.technologies:

            points = self.rules["technology"]["detected"]

            score += points

            breakdown.append(
                f"+{points} Technology fingerprinting completed"
            )

        # -------------------------
        # Limit score
        # -------------------------

        score = max(0, min(score, 100))

        # -------------------------
        # Grade & Risk
        # -------------------------

        if score >= 90:
            grade = "A"
            risk = "Low"

        elif score >= 75:
            grade = "B"
            risk = "Low"

        elif score >= 60:
            grade = "C"
            risk = "Medium"

        elif score >= 40:
            grade = "D"
            risk = "High"

        else:
            grade = "F"
            risk = "Critical"

        return {
            "score": score,
            "grade": grade,
            "risk": risk,
            "breakdown": breakdown,
        }