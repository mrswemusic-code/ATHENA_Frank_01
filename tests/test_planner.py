from pprint import pprint

from src.core.planner.planner import Planner


planner = Planner()


plan = planner.create_plan(

    "status"

)


print()

print(plan)

print()

pprint(

    plan.to_dict()

)
