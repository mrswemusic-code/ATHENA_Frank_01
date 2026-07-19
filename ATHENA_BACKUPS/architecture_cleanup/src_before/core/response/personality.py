class AthenaPersonality:


    def __init__(self):

        self.name = "ATHENA"


    def wrap(
        self,
        message,
        language="es"
    ):


        if language == "es":

            return (

                "ATHENA:\n\n"

                + message

            )


        return (

            "ATHENA:\n\n"

            + message

        )
