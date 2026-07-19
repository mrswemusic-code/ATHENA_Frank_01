from src.core.logger.logger import AthenaLogger

from src.core.response.language_formatter import LanguageFormatter
from src.core.response.personality import AthenaPersonality
from src.core.response.context import ResponseContext
from src.core.response.response_analyzer import ResponseAnalyzer



class ResponseEngine:


    def __init__(self):


        self.context = ResponseContext()


        self.formatter = LanguageFormatter()


        self.personality = AthenaPersonality()


        self.analyzer = ResponseAnalyzer()


        self.default_language = "es"



        AthenaLogger.info(
            "Response Engine initialized."
        )



    def detect_language(
        self,
        execution_result
    ):


        return self.default_language





    def extract_result(
        self,
        execution_result
    ):


        """
        Extracts the real payload
        from ExecutionResult.

        New architecture:

        ExecutionResult
            |
            result
            |
            list
            |
            task result

        """



        if execution_result is None:

            return None



        #
        # NEW EXECUTION RESULT OBJECT
        #

        if hasattr(
            execution_result,
            "result"
        ):


            results = execution_result.result



        else:


            results = execution_result



        if not results:

            return None



        #
        # If result is dictionary directly
        #

        if isinstance(
            results,
            dict
        ):

            return results



        #
        # List of executed tasks
        #

        if isinstance(
            results,
            list
        ):



            first = results[0]



            if isinstance(
                first,
                dict
            ):


                if "result" in first:

                    return first["result"]


                return first



            return first



        return results





    def generate(
        self,
        execution_result
    ):



        language = self.detect_language(
            execution_result
        )



        #
        # Analyze response type
        #

        response_type = self.analyzer.analyze(

            execution_result,

            self.context

        )



        self.context.update(

            language=language,

            mode="assistant",

            metadata={

                "engine":
                "response",

                "type":
                response_type["type"],

                "format":
                response_type["format"]

            }

        )



        data = self.extract_result(
            execution_result
        )



        if data is None:



            response = (

                "No encontré información "
                "disponible."

            )


            return self.personality.wrap(

                response,

                language

            )





        #
        # SYSTEM REPORT
        #

        if isinstance(
            data,
            dict
        ):



            if "cpu" in data:



                response = self.formatter.format_system_status(

                    data,

                    language

                )


                return self.personality.wrap(

                    response,

                    language

                )





        #
        # ERROR
        #

        if isinstance(
            data,
            dict
        ) and "error" in data:



            return self.personality.wrap(

                data["error"],

                language

            )





        #
        # GENERIC RESPONSE
        #

        response = str(
            data
        )



        return self.personality.wrap(

            response,

            language

        )
