from cyberinsight.engines.technology.detector import Detector
from cyberinsight.engines.technology.fingerprint_loader import FingerprintLoader


class FingerprintEngine:

    def __init__(self):

        self.loader = FingerprintLoader()

    def analyze(self, url: str):

        fingerprints = self.loader.load_fingerprints()

        return Detector.detect(
            url,
            fingerprints,
        )