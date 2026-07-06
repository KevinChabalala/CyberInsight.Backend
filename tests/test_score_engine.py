from cyberinsight.engines.scoring.engine import ScoreEngine

engine = ScoreEngine()

dns = {
    "success": True
}

ssl = {
    "success": True,
    "valid": True
}

headers = {
    "headers": {
        "Strict-Transport-Security": {
            "present": True
        },
        "Content-Security-Policy": {
            "present": False
        },
        "X-Frame-Options": {
            "present": True
        },
        "X-Content-Type-Options": {
            "present": False
        },
        "Referrer-Policy": {
            "present": False
        },
        "Permissions-Policy": {
            "present": False
        }
    }
}

technology = {
    "technologies": [
        {
            "name": "React"
        }
    ]
}

result = engine.calculate(
    dns,
    ssl,
    headers,
    technology,
)

print(result)