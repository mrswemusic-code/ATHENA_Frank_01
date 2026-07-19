class ResponseStyle:


    def __init__(self):

        self.styles = {

            "assistant": {

                "tone": "neutral",
                "detail": "medium"

            },

            "technical": {

                "tone": "precise",
                "detail": "high"

            },

            "brief": {

                "tone": "minimal",
                "detail": "low"

            },

            "executive": {

                "tone": "professional",
                "detail": "structured"

            }

        }



    def get(
        self,
        mode="assistant"
    ):

        return self.styles.get(

            mode,

            self.styles["assistant"]

        )



    def apply(
        self,
        message,
        mode="assistant"
    ):


        style = self.get(
            mode
        )


        if mode == "technical":

            return (

                "Análisis técnico:\n\n"

                + message

            )


        if mode == "executive":

            return (

                "Resumen ejecutivo:\n\n"

                + message

            )


        return message
