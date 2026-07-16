from src.core.telemetry.telemetry_manager import TelemetryManager



telemetry = TelemetryManager()



telemetry.update(
    "cpu",
    25.5
)


telemetry.update(
    "temperature",
    92
)



print(
    telemetry.snapshot()
)
