from cyberinsight.engines.dns.engine import DnsEngine

result = DnsEngine.lookup("https://google.com")

print(result)