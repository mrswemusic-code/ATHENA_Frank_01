from pprint import pprint

from src.core.kernel.kernel import AthenaKernel

from src.core.execution.execution_engine import ExecutionEngine
from src.core.execution.execution_context import ExecutionContext

from src.core.planner.planner import Planner


kernel = AthenaKernel()

kernel.boot()


planner = Planner()

plan = planner.create_plan(

    "status"

)


engine = ExecutionEngine(

    kernel.command_bus

)


context = ExecutionContext(

    kernel=kernel

)


result = engine.execute(

    plan,

    context

)


print()

print("EXECUTION RESULT")

print("----------------")

pprint(

    result
)
