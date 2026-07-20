from src.core.logger.logger import AthenaLogger


class TaskQueue:

    def __init__(self):

        self.queue = []

        AthenaLogger.info(
            "[TASK QUEUE] Initialized"
        )


    def push(self, task):

        self.queue.append(task)

        self.queue.sort(
            key=lambda t: t.priority
        )

        AthenaLogger.info(
            f"[TASK QUEUE] Added -> {task.name}"
        )


    def pop(self):

        if not self.queue:

            return None

        return self.queue.pop(0)


    def empty(self):

        return len(self.queue) == 0


    def size(self):

        return len(self.queue)


    def clear(self):

        self.queue.clear()
