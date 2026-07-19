from src.core.logger.logger import AthenaLogger


class ExecutiveLoop:

    def __init__(self, kernel):

        self.kernel = kernel

        AthenaLogger.info(
            "Executive Loop initialized."
        )


    def cycle(self, text):

        brain = self.kernel.get(
            "brain"
        )

        if not brain:

            AthenaLogger.warning(
                "[EXECUTIVE] Brain unavailable"
            )

            return None


        AthenaLogger.info(
            "[EXECUTIVE] Cycle started"
        )


        response = brain.think(
            text
        )


        AthenaLogger.info(
            "[EXECUTIVE] Cycle completed"
        )


        return response
