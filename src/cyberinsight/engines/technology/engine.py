from .detector import Detector
from .fingerprint_loader import FingerprintLoader


class TechnologyEngine:

    def __init__(self):
        self.loader = FingerprintLoader()

    def analyze(self, url: str):

        fingerprints = self.loader.load_fingerprints()

        return Detector.detect(
            url,
            fingerprints,
        )