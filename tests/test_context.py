from pprint import pprint

from src.core.kernel.kernel import AthenaKernel


kernel = AthenaKernel()

kernel.boot()


context = kernel.get(
    "context"
)


context.set(
    "current_project",
    "ATHENA"
)

context.set(
    "last_command",
    "status"
)

context.remember(
    "user",
    "status"
)

context.remember(
    "athena",
    "System online."
)


pprint(
    context.snapshot()
)
