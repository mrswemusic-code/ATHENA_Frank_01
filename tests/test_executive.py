from src.core.kernel.kernel import AthenaKernel

kernel = AthenaKernel()

kernel.boot()

executive = kernel.get("executive")

print()

print(executive.cycle("estado"))
