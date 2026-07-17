from pprint import pprint

from src.core.kernel.kernel import AthenaKernel

from src.core.brain.brain import AthenaBrain


kernel = AthenaKernel()

kernel.boot()

brain = AthenaBrain(kernel)

result = brain.think(
    "estado"
)

print()

print("RESULT")

print("----------------")

pprint(result)
