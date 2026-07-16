import time
from collections import deque

from src.core.logger.logger import AthenaLogger


class AthenaTask:


    def __init__(
        self,
        name,
        callback,
        interval=1.0,
        repeat=True
    ):

        self.name = name
        self.callback = callback
        self.interval = interval
        self.repeat = repeat

        self.last_run = 0



    def ready(self):

        now = time.time()

        if now - self.last_run >= self.interval:

            return True

        return False



    def execute(self):

        self.last_run = time.time()

        self.callback()



class TaskQueue:


    def __init__(self):

        self.tasks = deque()



    def add(self, task):

        self.tasks.append(task)

        AthenaLogger.info(
            f"[TASK] Added {task.name}"
        )



    def run_pending(self):


        for task in list(self.tasks):


            if task.ready():

                task.execute()


                if not task.repeat:

                    self.tasks.remove(task)
