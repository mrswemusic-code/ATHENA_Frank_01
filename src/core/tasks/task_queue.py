from queue import Queue

from src.core.logger.logger import AthenaLogger


class TaskQueue:

    def __init__(self):

        self.queue = Queue()


    def add(self, task):

        self.queue.put(task)

        AthenaLogger.info(

            f"[TASK] Added {task.name}"

        )


    def next(self):

        if self.queue.empty():

            return None

        return self.queue.get()


    def size(self):

        return self.queue.qsize()
