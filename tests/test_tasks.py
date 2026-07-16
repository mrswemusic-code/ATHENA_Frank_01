from src.core.tasks.task_queue import TaskQueue

from src.core.tasks.task import AthenaTask


queue = TaskQueue()


def hello():

    print("ATHENA TASK EXECUTED")


queue.add(

    AthenaTask(

        "hello",

        hello

    )

)


task = queue.next()

task.callback()
