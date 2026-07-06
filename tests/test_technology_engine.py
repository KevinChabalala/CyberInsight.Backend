from cyberinsight.engines.technology.engine import TechnologyEngine

result = TechnologyEngine.analyze(
    "https://react.dev"
)

print(result.model_dump_json(indent=4))