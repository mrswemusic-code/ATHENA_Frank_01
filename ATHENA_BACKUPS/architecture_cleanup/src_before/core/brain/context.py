from datetime import datetime


class BrainContext:


    def __init__(self):

        self.history = []

        self.current_intent = None

        self.current_plan = None

        self.state = "IDLE"



    def update_state(
        self,
        state
    ):

        self.state = state



    def remember(
        self,
        user_input,
        intent,
        response
    ):


        self.history.append(

            {

                "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "input":
                user_input,

                "intent":
                intent,

                "response":
                response

            }

        )



    def last(self):

        if self.history:

            return self.history[-1]


        return None



    def snapshot(self):

        return {

            "state":
            self.state,

            "intent":
            self.current_intent,

            "history_size":
            len(self.history)

        }
