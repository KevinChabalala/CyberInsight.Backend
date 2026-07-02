from cyberinsight.engines.url_engine import UrlEngine

url = "Google.com"

normalized = UrlEngine.normalize(url)

print(normalized)

print(UrlEngine.validate(normalized))