import time



class SessionMemory:



    def __init__(self):

        self.created = time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.data = {}



    def remember(
        self,
        key,
        value
    ):

        self.data[key] = value



    def recall(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )



    def clear(self):

        self.data.clear()



    def snapshot(self):

        return {

            "created": self.created,

            "data": self.data.copy()

        }
