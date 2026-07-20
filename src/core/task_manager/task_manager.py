import time

from src.core.logger.logger import AthenaLogger
from src.core.task_manager.task_queue import TaskQueue


class TaskManager:

    def __init__(self):

        self.queue = TaskQueue()

        self.history = []

        AthenaLogger.info(
            "[TASK MANAGER] Initialized"
        )

    def submit(self, task):

        task.status = "PENDING"

        self.queue.push(task)

        return task

    def execute_next(self):

        task = self.queue.pop()

        if not task:
            return None

        task.started = time.time()

        task.start()

        AthenaLogger.info(
            f"[TASK] Running -> {task.name}"
        )

        try:

            output = task.callback()

            task.finished = time.time()

            task.execution_time = (

                task.finished - task.started

            )

            task.complete(output)

        except Exception as error:

            task.finished = time.time()

            task.execution_time = (

                task.finished - task.started

            )

            task.fail(str(error))

            AthenaLogger.error(

                f"[TASK] Failed -> {task.name}: {error}"

            )

        self.history.append(task)

        return task

    def pending(self):

        return self.queue.size()

    def completed(self):

        return len(

            [

                t

                for t in self.history

                if t.status == "COMPLETED"

            ]

        )

    def failed(self):

        return len(

            [

                t

                for t in self.history

                if t.status == "FAILED"

            ]

        )

    def history_list(self):

        return self.history
