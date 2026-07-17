
class LanguageContext:


    def __init__(
        self,
        language="es",
        confidence=1.0
    ):

        self.language = language

        self.confidence = confidence



    def to_dict(self):

        return {

            "language": self.language,

            "confidence": self.confidence

        }

