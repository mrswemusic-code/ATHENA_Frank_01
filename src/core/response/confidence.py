class ResponseConfidence:


    def __init__(self):

        self.score = 1.0



    def evaluate(
        self,
        data
    ):


        if data is None:

            self.score = 0.0


        elif isinstance(
            data,
            dict
        ):

            self.score = 0.9


        else:

            self.score = 0.7



        return self.score



    def label(self):


        if self.score >= 0.9:

            return "high"


        if self.score >= 0.6:

            return "medium"


        return "low"
