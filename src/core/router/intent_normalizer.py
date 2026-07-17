from src.core.logger.logger import AthenaLogger


class IntentNormalizer:


    """
    Converts user intentions into
    ATHENA internal capabilities.
    """



    RULES = {


        "status": [
            "status",
            "health",
            "computer",
            "system",
            "pc",
            "machine",
            "hardware"
        ],


        "memory": [
            "remember",
            "memory",
            "recall"
        ],


        "voice": [
            "voice",
            "speak",
            "listen"
        ],


        "internet": [
            "search",
            "web",
            "news",
            "research"
        ],


        "music": [
            "music",
            "spotify",
            "song"
        ],


        "coding": [
            "code",
            "program",
            "debug"
        ]

    }



    def normalize(
        self,
        text
    ):

        text = text.lower()


        for intent, words in self.RULES.items():

            for word in words:

                if word in text:

                    AthenaLogger.info(
                        f"[INTENT] Normalized -> {intent}"
                    )

                    return intent



        AthenaLogger.warning(
            "[INTENT] Unknown, fallback system"
        )


        return "system"
