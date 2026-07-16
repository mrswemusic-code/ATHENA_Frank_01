from src.core.kernel.kernel import AthenaKernel
import time


kernel = AthenaKernel()


kernel.boot()


telemetry = kernel.get(
    "telemetry"
)


telemetry.update(
    "cpu",
    30
)


telemetry.update(
    "temperature",
    92
)



print()

print(
    "SNAPSHOT"
)

print(
    telemetry.snapshot()
)


print()

print(
    "EVENTS"
)

print(
    telemetry.events()
)
