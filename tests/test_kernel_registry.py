from src.core.kernel.kernel import AthenaKernel



kernel = AthenaKernel()


kernel.boot()



print("\nATHENA REGISTRY TEST\n")


components = [

    "identity",
    "memory",
    "telemetry",
    "events",
    "commands",
    "command_bus",
    "runtime",
    "loop"

]


for component in components:


    result = kernel.get(
        component
    )


    print(
        component,
        ":",
        "ONLINE" if result else "MISSING"
    )
