from collections import deque


class TaskQueue:

    def __init__(self):
        self.queue = deque()

    def add(self, task):
        self.queue.append(task)

    def run_pending(self):
        while self.queue:
            task = self.queue.popleft()

            if callable(task):
                task()
            elif hasattr(task, "run"):
                task.run()
