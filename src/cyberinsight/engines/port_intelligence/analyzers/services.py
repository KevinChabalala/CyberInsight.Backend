from cyberinsight.engines.port_intelligence.data.ports import (
    COMMON_PORTS,
)


class ServiceAnalyzer:

    @staticmethod
    def get(port: int):

        return COMMON_PORTS.get(
            port,
            {
                "service": "Unknown",
                "risk": "Unknown",
                "description": "Unknown service.",
                "recommendation": "Investigate the exposed service.",
            },
        )