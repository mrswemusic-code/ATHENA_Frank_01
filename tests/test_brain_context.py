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



print("\nRESPONSE")
print(response)



print("\nBRAIN STATE")

print(
    brain.status()
)



print("\nLAST MEMORY")

print(
    brain.context.last()
)
