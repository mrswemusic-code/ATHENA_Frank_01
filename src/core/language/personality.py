class AthenaPersonality:


    def __init__(self):

        self.name = "ATHENA"

        self.style = "professional"

        self.region = "latin-america"

        self.languages = [

            "es",
            "en",
            "it"

        ]


    def identity(self):

        return {

            "name": self.name,

            "style": self.style,

            "region": self.region,

            "languages": self.languages

        }
