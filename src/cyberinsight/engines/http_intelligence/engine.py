import time

import requests

from cyberinsight.engines.http_intelligence.analyzers.cache import (
    CacheAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.connection import (
    ConnectionAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.content import (
    ContentAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.cookies import (
    CookieAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.performance import (
    PerformanceAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.protocol import (
    ProtocolAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.redirects import (
    RedirectAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.response import (
    ResponseAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.security import (
    SecurityAnalyzer,
)
from cyberinsight.engines.http_intelligence.analyzers.server import (
    ServerAnalyzer,
)
from cyberinsight.engines.http_intelligence.context import (
    HTTPScanContext,
)
from cyberinsight.engines.http_intelligence.models import (
    HTTPIntelligenceResult,
)


class HTTPIntelligenceEngine:

    @staticmethod
    def analyze(
        url: str,
    ) -> HTTPIntelligenceResult:

        try:

            start = time.perf_counter()

            response = requests.get(
                url,
                allow_redirects=True,
                timeout=15,
                headers={
                    "User-Agent": "CyberInsight Scanner",
                },
            )

            elapsed = (
                time.perf_counter()
                - start
            ) * 1000

            context = HTTPScanContext(
                response=response,
                response_time_ms=elapsed,
            )

            return HTTPIntelligenceResult(

                success=True,

                response=ResponseAnalyzer.analyze(
                    context
                ),

                redirects=RedirectAnalyzer.analyze(
                    context
                ),

                server=ServerAnalyzer.analyze(
                    context
                ),

                content=ContentAnalyzer.analyze(
                    context
                ),

                cache=CacheAnalyzer.analyze(
                    context
                ),

                connection=ConnectionAnalyzer.analyze(
                    context
                ),

                cookies=CookieAnalyzer.analyze(
                    context
                ),

                protocol=ProtocolAnalyzer.analyze(
                    context
                ),

                performance=PerformanceAnalyzer.analyze(
                    context
                ),

                security=SecurityAnalyzer.analyze(
                    context
                ),

                error=None,
            )

        except Exception as e:

            from cyberinsight.engines.http_intelligence.models import (
                CacheInfo,
                ConnectionInfo,
                ContentInfo,
                CookieInfo,
                HTTPSecurityInfo,
                HTTPResponseInfo,
                PerformanceInfo,
                ProtocolInfo,
                RedirectInfo,
                ServerInfo,
            )

            return HTTPIntelligenceResult(

                success=False,

                response=HTTPResponseInfo(),

                redirects=RedirectInfo(),

                server=ServerInfo(),

                content=ContentInfo(),

                cache=CacheInfo(),

                connection=ConnectionInfo(),

                cookies=CookieInfo(),

                protocol=ProtocolInfo(),

                performance=PerformanceInfo(),

                security=HTTPSecurityInfo(),

                error=str(e),
            )