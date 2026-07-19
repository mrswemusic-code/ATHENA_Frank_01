class WorkingMemory:

    def __init__(self):

        self.data = {}


    def set(
        self,
        key,
        value
    ):

        self.data[key] = value


    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )


    def delete(
        self,
        key
    ):

        if key in self.data:

            del self.data[key]


    def snapshot(self):

        return self.data.copy()


    def clear(self):

        self.data.clear()
