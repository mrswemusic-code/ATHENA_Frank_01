from datetime import datetime


class BrainContextManager:


    def __init__(self):

        self.context = {

            "user": None,

            "language": "es",

            "state": "IDLE",

            "last_input": None,

            "last_intent": None,

            "history": []

        }


    def update(
        self,
        text,
        intent,
        language="es",
        response=None
    ):


        self.context["last_input"] = text

        self.context["last_intent"] = intent

        self.context["language"] = language

        self.context["state"] = "READY"


        self.context["history"].append(

            {

                "timestamp":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "input":
                    text,

                "intent":
                    intent,

                "language":
                    language,

                "response":
                    response

            }

        )


    def get(
        self,
        key,
        default=None
    ):

        return self.context.get(
            key,
            default
        )


    def history(self):

        return self.context["history"]


    def snapshot(self):

        return self.context.copy()


    def clear(self):

        self.__init__()
