from cyberinsight.engines.technology_engine import TechnologyEngine

result = TechnologyEngine.analyze(
    "https://react.dev"
)

print(result.model_dump_json(indent=4))