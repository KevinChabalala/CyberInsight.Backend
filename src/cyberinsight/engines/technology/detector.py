import re
from typing import Any

import requests
from bs4 import BeautifulSoup

from cyberinsight.engines.technology.models import (
    DetectedTechnology,
    TechnologyScanResult,
)


class Detector:

    @staticmethod
    def detect(
        url: str,
        fingerprints: list[dict[str, Any]],
    ) -> TechnologyScanResult:

        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "CyberInsight Scanner",
                },
            )

            html = response.text

            soup = BeautifulSoup(
                html,
                "html.parser",
            )

            headers = response.headers
            cookies = response.cookies

            detected = []

            scripts = soup.find_all("script")

            for technology in fingerprints:

                matched_by = []
                confidence = 0

                # -------------------------
                # HTML
                # -------------------------

                for pattern in technology.get("html", []):

                    if pattern.lower() in html.lower():

                        matched_by.append("html")
                        confidence += technology.get(
                            "confidence", {}
                        ).get("html", 20)

                        break

                # -------------------------
                # Headers
                # -------------------------

                for pattern in technology.get("headers", []):

                    if pattern.lower() in str(headers).lower():

                        matched_by.append("headers")
                        confidence += technology.get(
                            "confidence", {}
                        ).get("headers", 25)

                        break

                # -------------------------
                # Cookies
                # -------------------------

                for pattern in technology.get("cookies", []):

                    if pattern.lower() in str(cookies).lower():

                        matched_by.append("cookies")
                        confidence += technology.get(
                            "confidence", {}
                        ).get("cookies", 15)

                        break

                # -------------------------
                # Scripts
                # -------------------------

                for script in scripts:

                    src = script.get("src")

                    if not src:
                        continue

                    for pattern in technology.get("scripts", []):

                        if re.search(
                            pattern,
                            src,
                            re.IGNORECASE,
                        ):

                            matched_by.append("scripts")
                            confidence += technology.get(
                                "confidence", {}
                            ).get("scripts", 20)

                            break

                if matched_by:

                    confidence = min(confidence, 100)

                    detected.append(
                        DetectedTechnology(
                            name=technology["name"],
                            category=technology["category"],
                            confidence=confidence,
                            matched_by=matched_by,
                            version=None,
                        )
                    )

            return TechnologyScanResult(
                success=True,
                technologies=detected,
                error=None,
            )

        except Exception as e:

            return TechnologyScanResult(
                success=False,
                technologies=[],
                error=str(e),
            )