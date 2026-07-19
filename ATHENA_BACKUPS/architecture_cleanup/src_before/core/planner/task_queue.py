from collections import deque

from src.core.logger.logger import AthenaLogger



class TaskQueue:


    def __init__(self):

        self.queue = deque()



    def add(self, task):


        self.queue.append(
            task
        )


        AthenaLogger.info(
            "[TASK QUEUE] Task added"
        )



    def run_pending(self):


        while self.queue:


            task = self.queue.popleft()



            try:


                if callable(task):

                    task()


                elif hasattr(task, "run"):

                    task.run()



            except Exception as error:


                AthenaLogger.error(

                    f"[TASK QUEUE] Execution error -> {error}"

                )
