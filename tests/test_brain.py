from pprint import pprint

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

print("ATHENA RESPONSE")

print("----------------")

pprint(response)
