from src.core.kernel.kernel import AthenaKernel



kernel = AthenaKernel()

kernel.boot()



bus = kernel.get(
    "command_bus"
)



result = bus.dispatch(
    "status"
)



print()

print(
    "COMMAND BUS RESULT"
)

print(
    result
)
