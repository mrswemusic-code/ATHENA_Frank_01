from datetime import datetime


class Conversation:

    def __init__(self):

        self.messages = []


    def add(
        self,
        role,
        text,
        intent=None,
        language="es"
    ):

        self.messages.append({

            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "role": role,

            "text": text,

            "intent": intent,

            "language": language

        })


    def last(self):

        if self.messages:
            return self.messages[-1]

        return None


    def history(self):

        return self.messages


    def clear(self):

        self.messages.clear()
