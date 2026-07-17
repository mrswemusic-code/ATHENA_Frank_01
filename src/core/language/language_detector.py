
from src.core.language.language_context import LanguageContext



class LanguageDetector:



    def detect(
        self,
        text
    ):


        text = text.lower()



        spanish = [

            "hola",
            "estado",
            "sistema",
            "busca",
            "recuerda",
            "quiero",
            "dime",
            "analiza"

        ]



        english = [

            "hello",
            "status",
            "search",
            "remember",
            "tell me",
            "analyze"

        ]



        italian = [

            "ciao",
            "stato",
            "cerca",
            "ricorda"

        ]



        if any(
            word in text
            for word in spanish
        ):

            return LanguageContext(
                "es",
                0.95
            )



        if any(
            word in text
            for word in english
        ):

            return LanguageContext(
                "en",
                0.95
            )



        if any(
            word in text
            for word in italian
        ):

            return LanguageContext(
                "it",
                0.95
            )



        return LanguageContext(
            "es",
            0.5
        )

