from urllib.parse import urlparse

from cyberinsight.engines.port_intelligence.analyzers.scanner import (
    PortScanner,
)
from cyberinsight.engines.port_intelligence.analyzers.services import (
    ServiceAnalyzer,
)
from cyberinsight.engines.port_intelligence.analyzers.risk import (
    RiskAnalyzer,
)
from cyberinsight.engines.port_intelligence.models import (
    PortIntelligenceResult,
    PortResult,
    PortSummary,
)
from cyberinsight.engines.port_intelligence.data.ports import (
    COMMON_PORTS,
)


class PortIntelligenceEngine:

    @staticmethod
    def analyze(url: str):

        try:

            host = urlparse(url).hostname

            if not host:
                raise ValueError("Invalid host.")

            ports = sorted(COMMON_PORTS.keys())

            scan = PortScanner.scan(
                host,
                ports,
            )

            results = []

            for port in ports:

                info = ServiceAnalyzer.get(port)

                results.append(

                    PortResult(

                        port=port,

                        open=scan[port],

                        service=info["service"],

                        risk=info["risk"],

                        description=info["description"],

                        recommendation=info["recommendation"],
                    )
                )

            risk = RiskAnalyzer.summarize(results)

            return PortIntelligenceResult(

                success=True,

                summary=PortSummary(

                    total_scanned=len(ports),

                    open_ports=sum(
                        r.open
                        for r in results
                    ),

                    high_risk_ports=(
                        risk["high"]
                        + risk["critical"]
                    ),
                ),

                ports=results,

                error=None,
            )

        except Exception as e:

            return PortIntelligenceResult(

                success=False,

                summary=PortSummary(

                    total_scanned=0,

                    open_ports=0,

                    high_risk_ports=0,
                ),

                ports=[],

                error=str(e),
            )