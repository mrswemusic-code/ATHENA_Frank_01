from datetime import datetime


class BrainContextManager:


    def __init__(self):

        self.context = {

            "user": None,

            "language": "es",

            "last_intent": None,

            "last_input": None,

            "history": []

        }



    def update(

        self,
        text,
        intent,
        language="es"

    ):


        self.context["last_input"] = text

        self.context["last_intent"] = intent

        self.context["language"] = language



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
                    language

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



    def snapshot(self):

        return self.context.copy()



    def clear(self):

        self.context = {

            "user": None,

            "language": "es",

            "last_intent": None,

            "last_input": None,

            "history": []

        }
