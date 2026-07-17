from datetime import datetime
import uuid



class ConversationSession:


    def __init__(self):

        self.id = str(
            uuid.uuid4()
        )

        self.created = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


        self.messages = []



    def add(

        self,

        role,

        content

    ):


        self.messages.append(

            {

                "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "role":
                role,

                "content":
                content

            }

        )



    def history(self):

        return self.messages



    def info(self):

        return {

            "id":
            self.id,

            "created":
            self.created,

            "messages":
            len(self.messages)

        }
