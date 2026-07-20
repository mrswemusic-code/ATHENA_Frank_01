from src.core.planner.task import Task


class Plan:

    def __init__(self, name):

        self.name = name

        self.intent = name

        self.tasks = []


    def add(self, task: Task):

        self.tasks.append(task)


    def remove(self, task: Task):

        self.tasks.remove(task)


    def pending(self):

        return [

            task

            for task in self.tasks

            if task.status == "PENDING"

        ]


    def running(self):

        return [

            task

            for task in self.tasks

            if task.status == "RUNNING"

        ]


    def completed(self):

        return [

            task

            for task in self.tasks

            if task.status == "COMPLETED"

        ]


    def failed(self):

        return [

            task

            for task in self.tasks

            if task.status == "FAILED"

        ]


    def progress(self):

        total = len(self.tasks)

        if total == 0:

            return 0

        completed = len(self.completed())

        return round(

            completed / total * 100,

            1

        )


    def finished(self):

        return self.progress() == 100


    def to_dict(self):

        return {

            "name": self.name,

            "progress": self.progress(),

            "tasks": [

                task.to_dict()

                for task in self.tasks

            ]

        }


    def __repr__(self):

        return (

            f"Plan("

            f"{self.name}, "

            f"{len(self.tasks)} tasks, "

            f"{self.progress()}%"

            f")"

        )
