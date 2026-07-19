from src.core.logger.logger import AthenaLogger


class GoalManager:

    def __init__(self):

        self.goals = []

        AthenaLogger.info(
            "Goal Manager initialized."
        )

    def add(self, objective):

        self.goals.append(objective)

        self.sort()

    def sort(self):

        self.goals.sort(
            key=lambda g: g.priority
        )

    def next(self):

        for goal in self.goals:

            if goal.status == "PENDING":

                return goal

        return None

    def completed(self):

        return [

            g

            for g in self.goals

            if g.status == "COMPLETED"

        ]

    def pending(self):

        return [

            g

            for g in self.goals

            if g.status == "PENDING"

        ]

    def snapshot(self):

        return [

            g.to_dict()

            for g in self.goals

        ]
