from src.core.kernel.kernel import AthenaKernel

kernel = AthenaKernel()

kernel.boot()

engine = kernel.get("execution")

print()

print(engine)

print()

print("Execution Engine OK")
