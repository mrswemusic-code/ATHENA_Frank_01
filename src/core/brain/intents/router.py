from src.core.brain.intent import Intent

from src.core.brain.intents.status import StatusIntent


class IntentRouter:


    def __init__(self):

        self.status = StatusIntent()


    def detect(
        self,
        text
    ):

        if self.status.match(text):

            return Intent(

                name="status",

                confidence=1.0,

                payload={}

            )


        return Intent(

            name="unknown",

            confidence=0.0,

            payload={

                "text": text

            }

        )
