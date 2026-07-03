from cyberinsight.engines.http_intelligence.context import HTTPScanContext
from cyberinsight.engines.http_intelligence.models import RedirectInfo


class RedirectAnalyzer:

    @staticmethod
    def analyze(context: HTTPScanContext) -> RedirectInfo:

        response = context.response

        history = response.history

        chain = [r.url for r in history]
        chain.append(response.url)

        codes = [r.status_code for r in history]

        https_upgrade = (
            len(chain) >= 2
            and chain[0].startswith("http://")
            and chain[-1].startswith("https://")
        )

        return RedirectInfo(
            count=len(history),
            chain=chain,
            redirect_codes=codes,
            https_upgrade=https_upgrade,
            infinite_redirect=False,
        )