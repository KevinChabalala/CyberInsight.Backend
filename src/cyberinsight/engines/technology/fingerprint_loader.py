import json
from pathlib import Path


class FingerprintLoader:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "fingerprints"
            / "technologies.json"
        )

    def load_fingerprints(self):

        with open(
            self.file,
            "r",
            encoding="utf-8",
        ) as f:

            return json.load(f)