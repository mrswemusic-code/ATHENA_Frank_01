class StatusIntent:


    def match(
        self,
        text
    ):

        return text.lower().strip() == "status"
