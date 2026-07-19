from dataclasses import dataclass, field



@dataclass
class ResponseContext:


    user_intent: str = None

    language: str = "es"

    priority: str = "normal"

    mode: str = "assistant"

    confidence: float = 1.0

    metadata: dict = field(
        default_factory=dict
    )



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
