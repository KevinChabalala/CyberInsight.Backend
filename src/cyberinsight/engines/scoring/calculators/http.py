class HTTPScoreCalculator:

    @staticmethod
    def calculate(result, rules):

        score = 0
        breakdown = []

        if not result.success:
            return score, breakdown

        if result.protocol.https:

            score += rules["https"]
            breakdown.append(f"+{rules['https']} HTTPS")

        if result.content.compression:

            score += rules["compression"]
            breakdown.append(f"+{rules['compression']} Compression enabled")

        if result.protocol.http2 or result.protocol.http3:

            score += rules["http2_or_http3"]
            breakdown.append(f"+{rules['http2_or_http3']} Modern HTTP protocol")

        if not result.redirects.infinite_redirect:

            score += rules["no_redirect_loop"]
            breakdown.append(f"+{rules['no_redirect_loop']} No redirect loop")

        if result.performance.response_time_ms <= 500:

            score += rules["fast_response"]
            breakdown.append(f"+{rules['fast_response']} Fast response")

        return score, breakdown