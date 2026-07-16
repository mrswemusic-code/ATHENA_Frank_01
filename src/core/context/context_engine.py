from datetime import datetime

from src.core.logger.logger import AthenaLogger

from src.core.context.context import Context


class ContextEngine:


    def __init__(self):

        self.context = Context()

        AthenaLogger.info(
            "Context Engine initialized."
        )


    def set(

        self,

        key,

        value

    ):

        if hasattr(

            self.context,

            key

        ):

            setattr(

                self.context,

                key,

                value

            )

            self.context.updated = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )


    def get(

        self,

        key

    ):

        return getattr(

            self.context,

            key,

            None

        )


    def remember(

        self,

        role,

        text

    ):

        self.context.conversation.append(

            {

                "role": role,

                "text": text

            }

        )


    def history(self):

        return self.context.conversation


    def snapshot(self):

        return vars(

            self.context

        )
