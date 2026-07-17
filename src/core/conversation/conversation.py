from src.core.logger.logger import AthenaLogger

from src.core.conversation.session import ConversationSession



class ConversationEngine:


    def __init__(

        self,

        brain

    ):


        self.brain = brain


        self.session = ConversationSession()



        AthenaLogger.info(
            "Conversation Engine initialized."
        )



    def send(

        self,

        text

    ):


        self.session.add(

            "USER",

            text

        )


        AthenaLogger.info(

            f"[CHAT] USER -> {text}"

        )



        response = self.brain.think(

            text

        )



        self.session.add(

            "ATHENA",

            response

        )



        return response




    def history(self):

        return self.session.history()



    def status(self):

        return self.session.info()
