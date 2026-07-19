class ResponseContext:


    def __init__(self):

        self.user_intent = None

        self.language = "es"

        self.priority = "normal"

        self.mode = "assistant"

        self.confidence = 1.0

        self.metadata = {}



    def update(
        self,
        intent=None,
        language="es",
        priority="normal",
        mode="assistant",
        confidence=1.0,
        metadata=None
    ):


        self.user_intent = intent

        self.language = language

        self.priority = priority

        self.mode = mode

        self.confidence = confidence


        if metadata:

            self.metadata.update(
                metadata
            )
