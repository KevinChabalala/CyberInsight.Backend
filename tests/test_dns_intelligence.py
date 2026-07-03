from cyberinsight.engines.dns_intelligence import DNSIntelligenceEngine


result = DNSIntelligenceEngine.analyze(
    "https://google.com"
)

print(result.model_dump())