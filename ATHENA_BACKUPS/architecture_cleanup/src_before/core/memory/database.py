import json
import os



class MemoryDatabase:



    def __init__(
        self,
        path="/opt/athena/system/data/memory.json"
    ):

        self.path = path

        self.data = {}

        self.load()



    def load(self):

        if os.path.exists(
            self.path
        ):

            try:

                with open(
                    self.path,
                    "r"
                ) as file:

                    self.data = json.load(
                        file
                    )

            except:

                self.data = {}



    def save(self):

        os.makedirs(
            os.path.dirname(
                self.path
            ),
            exist_ok=True
        )


        with open(
            self.path,
            "w"
        ) as file:

            json.dump(
                self.data,
                file,
                indent=4
            )



    def set(
        self,
        key,
        value
    ):

        self.data[key] = value

        self.save()



    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )



    def all(self):

        return self.data.copy()
