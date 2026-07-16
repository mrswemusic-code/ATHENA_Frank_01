import time

from src.core.tasks.task_queue import AthenaTask
from src.core.loop.event_loop import EventLoop



def hello():

    print(
        "ATHENA TASK EXECUTED"
    )



loop = EventLoop(
    rate=1
)



task = AthenaTask(
    "hello",
    hello,
    interval=2
)



loop.add_task(task)


loop.start()


time.sleep(7)


loop.stop()
