from src.core.kernel.kernel import AthenaKernel
from src.core.brain.brain import AthenaBrain


kernel = AthenaKernel()

kernel.boot()


brain = AthenaBrain(
    kernel
)


response = brain.think(
    "status"
)


print()

print(
    "ATHENA RESPONSE"
)

print(
    "----------------"
)

print(
    response
)


print()

print(
    "CONTEXT"
)

print(
    brain.context()
)
