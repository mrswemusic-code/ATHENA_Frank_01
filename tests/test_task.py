from pprint import pprint

from src.core.planner.task import Task


task = Task(

    name="Open Spotify",

    action="open_application",

    target="spotify",

    priority=10

)


print()

print(task)

print()

pprint(

    task.to_dict()

)

print()


task.start()

print(task)

task.complete()

print(task)
