import time

from src.core.logger.logger import AthenaLogger
from src.core.scheduler.task import SchedulerTask


class Scheduler:


    def __init__(self):

        self.tasks = []

        AthenaLogger.info(
            "Scheduler initialized."
        )


    def register(

        self,

        name,

        callback,

        interval=1.0,

        priority=5,

        repeat=True

    ):

        task = SchedulerTask(

            name=name,

            callback=callback,

            interval=interval,

            priority=priority,

            repeat=repeat

        )

        self.tasks.append(task)

        self.tasks.sort(
            key=lambda t: t.priority
        )

        AthenaLogger.info(
            f"[SCHEDULER] Registered -> {name}"
        )


    def every(

        self,

        seconds,

        callback,

        name=None,

        priority=5

    ):

        self.register(

            name=name or callback.__name__,

            callback=callback,

            interval=seconds,

            priority=priority,

            repeat=True

        )


    def once(

        self,

        callback,

        name=None,

        priority=5

    ):

        self.register(

            name=name or callback.__name__,

            callback=callback,

            interval=0,

            priority=priority,

            repeat=False

        )


    def enable(self, name):

        for task in self.tasks:

            if task.name == name:

                task.enabled = True


    def disable(self, name):

        for task in self.tasks:

            if task.name == name:

                task.enabled = False


    def remove(self, name):

        self.tasks = [

            task

            for task in self.tasks

            if task.name != name

        ]


    def list(self):

        return [

            {

                "name": t.name,

                "priority": t.priority,

                "enabled": t.enabled,

                "interval": t.interval,

                "executions": t.executions

            }

            for t in self.tasks

        ]


    def run_pending(self):

        now = time.time()

        for task in self.tasks:

            if not task.enabled:

                continue

            if now < task.next_run:

                continue

            try:

                task.callback()

                task.executions += 1

                task.last_run = now

                task.next_run = now + task.interval

                AthenaLogger.info(

                    f"[SCHEDULER] {task.name}"

                )

                if not task.repeat:

                    task.enabled = False

            except Exception as error:

                AthenaLogger.error(

                    f"[SCHEDULER] {task.name}: {error}"

                )
