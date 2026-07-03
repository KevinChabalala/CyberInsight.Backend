class TLSScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        if result.protocols.tls13:
            score += rules["tls13"]
            breakdown.append(f"+{rules['tls13']} TLS 1.3")

        if result.cipher.perfect_forward_secrecy:
            score += rules["pfs"]
            breakdown.append(f"+{rules['pfs']} Perfect Forward Secrecy")

        if not result.certificate.self_signed:
            score += rules["trusted"]
            breakdown.append(f"+{rules['trusted']} Trusted Certificate")

        return score, breakdown