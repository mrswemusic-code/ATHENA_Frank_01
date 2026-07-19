class PriorityEngine:

    def evaluate(self, objectives):

        return sorted(

            objectives,

            key=lambda o: o.priority

        )
