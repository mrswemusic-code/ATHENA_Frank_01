
from src.core.logger.logger import AthenaLogger

from src.core.response.language_formatter import LanguageFormatter
from src.core.response.personality import AthenaPersonality



class ResponseEngine:


    def __init__(self):

        self.formatter = LanguageFormatter()

        self.personality = AthenaPersonality()


        self.default_language = "es"


        AthenaLogger.info(
            "Response Engine initialized."
        )



    def detect_language(
        self,
        execution_result
    ):

        """
        Future language routing layer.
        Currently ATHENA default:
        Spanish Latin America.
        """

        return self.default_language



    def extract_result(
        self,
        execution_result
    ):


        if not execution_result:

            return None


        first = execution_result[0]


        if isinstance(first, dict):

            return first.get(
                "result",
                {}
            )


        return first



    def generate(
        self,
        execution_result
    ):


        language = self.detect_language(
            execution_result
        )


        data = self.extract_result(
            execution_result
        )


        if data is None:

            return self.personality.wrap(

                "No encontré información disponible.",

                language

            )



        if isinstance(data, dict):


            if "cpu" in data:


                response = self.formatter.format_system_status(

                    data,

                    language

                )


                return self.personality.wrap(

                    response,

                    language

                )



        return self.personality.wrap(

            str(data),

            language

        )

