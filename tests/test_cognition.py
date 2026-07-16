from src.core.cognition.cognitive_engine import CognitiveEngine



engine = CognitiveEngine()



telemetry = {

    "temperature": 95,

    "cpu": 96

}



result = engine.analyze(
    telemetry
)



print()

print("DECISIONS")



for item in result:

    print(item)



print()

print("HISTORY")

print(
    engine.history()
)
