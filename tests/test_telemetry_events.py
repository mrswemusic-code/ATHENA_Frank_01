from src.core.telemetry.telemetry_manager import TelemetryManager



telemetry = TelemetryManager()



telemetry.update(
    "temperature",
    92
)


telemetry.update(
    "cpu",
    95
)



print("\nSNAPSHOT")

print(
    telemetry.snapshot()
)



print("\nEVENTS")


for event in telemetry.events():

    print(event)
