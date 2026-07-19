import time

from src.core.logger.logger import AthenaLogger

from src.core.task_manager.task import Task
from src.core.task_manager.task_state import TaskState
from src.core.task_manager.task_queue import TaskQueue


class TaskManager:

    def __init__(self):

        self.queue = TaskQueue()

        self.history = []

        AthenaLogger.info(
            "[TASK MANAGER] Initialized"
        )


    def submit(

        self,

        name,

        callback,

        priority=5

    ):

        task = Task(

            name=name,

            callback=callback,

            priority=priority

        )

        self.queue.push(task)

        return task


    def execute_next(self):

        task = self.queue.pop()

        if not task:

            return None


        task.state = TaskState.RUNNING

        task.started = time.time()


        AthenaLogger.info(
            f"[TASK] Running -> {task.name}"
        )


        try:

            output = task.callback()

            task.finished = time.time()

            task.progress = 100

            task.state = TaskState.COMPLETED

            task.result.success = True

            task.result.output = output

            task.result.execution_time = (

                task.finished - task.started

            )


        except Exception as error:

            task.finished = time.time()

            task.state = TaskState.FAILED

            task.result.success = False

            task.result.error = str(error)


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

                if t.state == TaskState.COMPLETED

            ]

        )


    def failed(self):

        return len(

            [

                t

                for t in self.history

                if t.state == TaskState.FAILED

            ]

        )


    def history_list(self):

        return self.history
