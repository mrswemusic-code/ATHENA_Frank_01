from src.core.kernel.kernel import AthenaKernel



kernel = AthenaKernel()


kernel.boot()



identity = kernel.get(
    "identity"
)



identity.display()
