from src.core.brain.intent import Intent
from src.core.logger.logger import AthenaLogger



class IntentClassifier:



    def detect_language(
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
            "guarda",
            "reproduce",
            "analiza"

        ]



        english = [

            "hello",
            "check",
            "search",
            "play",
            "remember",
            "save",
            "analyze"

        ]



        italian = [

            "ciao",
            "cerca",
            "ricorda",
            "salva",
            "riproduci"

        ]



        if any(
            x in text
            for x in spanish
        ):

            return "es"



        if any(
            x in text
            for x in english
        ):

            return "en"



        if any(
            x in text
            for x in italian
        ):

            return "it"



        return "es"




    def extract_memory_payload(
        self,
        text
    ):


        text = text.lower()



        payload = {

            "operation": None,

            "key": None,

            "value": None

        }



        remember_words = [

            "recuerda",

            "guarda",

            "save",

            "remember"

        ]



        recall_words = [

            "que uso",

            "cual es",

            "cuál es",

            "what is",

            "what's"

        ]



        if any(
            x in text
            for x in remember_words
        ):


            payload["operation"] = "remember"



            if "brave" in text:

                payload["key"] = "browser"

                payload["value"] = "Brave"



            elif "spotify" in text:

                payload["key"] = "music_service"

                payload["value"] = "Spotify"



            return payload




        if any(
            x in text
            for x in recall_words
        ):


            payload["operation"] = "recall"



            if "navegador" in text or "browser" in text:

                payload["key"] = "browser"



            return payload




        return payload





    def classify(
        self,
        text
    ):


        command = text.lower().strip()


        language = self.detect_language(
            command
        )



        intents = {



            "system": [

                "status",
                "estado",
                "computadora",
                "ordenador",
                "cpu",
                "ram",
                "temperatura",
                "revisa mi pc",
                "check my computer"

            ],



            "memory": [

                "recuerda",
                "remember",
                "guarda",
                "save",
                "memoria",
                "navegador"

            ],



            "music": [

                "spotify",
                "playlist",
                "musica",
                "music",
                "reproduce",
                "play"

            ],



            "internet": [

                "busca",
                "search",
                "noticias",
                "news",
                "investiga",
                "research"

            ],



            "coding": [

                "codigo",
                "code",
                "python",
                "debug",
                "programa"

            ],



            "voice": [

                "escucha",
                "listen",
                "voz",
                "voice"

            ],



            "vision": [

                "imagen",
                "foto",
                "camera",
                "image"

            ]

        }




        for intent_name, keywords in intents.items():


            for keyword in keywords:


                if keyword in command:



                    payload = {

                        "language": language,

                        "text": text

                    }



                    if intent_name == "memory":

                        payload.update(

                            self.extract_memory_payload(
                                command
                            )

                        )



                    AthenaLogger.info(

                        f"[INTENT] {intent_name} ({language})"

                    )



                    return Intent(

                        name=intent_name,

                        confidence=0.95,

                        payload=payload

                    )




        return Intent(

            name="unknown",

            confidence=0.0,

            payload={

                "language": language,

                "text": text

            }

        )
