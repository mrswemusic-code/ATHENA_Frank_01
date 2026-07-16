class Planner:


    def create_plan(
        self,
        intent
    ):

        return {

            "intent": intent.name,

            "payload": intent.payload

        }
