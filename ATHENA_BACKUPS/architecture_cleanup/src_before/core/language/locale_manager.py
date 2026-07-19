class LocaleManager:


    def detect(
        self,
        language
    ):

        supported = [

            "es",
            "en",
            "it"

        ]


        if language in supported:

            return language


        return "es"



    def default(self):

        return "es"
