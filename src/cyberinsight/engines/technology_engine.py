from cyberinsight.engines.technology.fingerprint_engine import FingerprintEngine


class TechnologyEngine:

    @staticmethod
    def analyze(url: str):

        engine = FingerprintEngine()

        return engine.analyze(url)