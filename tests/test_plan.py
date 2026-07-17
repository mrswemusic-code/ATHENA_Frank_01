from pprint import pprint

from src.core.planner.plan import Plan
from src.core.planner.task import Task


plan = Plan(

    "Launch Spotify"

)


plan.add(

    Task(

        name="Open Spotify",

        action="open"

    )

)


plan.add(

    Task(

        name="Wait",

        action="sleep"

    )

)


plan.add(

    Task(

        name="Play Playlist",

        action="play"

    )

)


print()

print(plan)

print()

pprint(

    plan.to_dict()

)

print()


plan.tasks[0].complete()

print(

    "Progress:",

    plan.progress(),

    "%"

)


plan.tasks[1].complete()

print(

    "Progress:",

    plan.progress(),

    "%"

)


plan.tasks[2].complete()

print(

    "Progress:",

    plan.progress(),

    "%"

)


print()

print(

    "Finished:",

    plan.finished()

)
