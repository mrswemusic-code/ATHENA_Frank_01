from src.core.kernel.kernel import AthenaKernel

from src.core.brain.brain import AthenaBrain


kernel = AthenaKernel()

kernel.boot()

brain = AthenaBrain(kernel)

plan = brain.think("estado")

print()

print(plan)

print()

print(plan.to_dict())
