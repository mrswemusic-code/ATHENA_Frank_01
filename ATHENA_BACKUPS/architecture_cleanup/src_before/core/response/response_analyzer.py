from src.core.logger.logger import AthenaLogger



class ResponseAnalyzer:


    def __init__(self):


        AthenaLogger.info(
            "Response Analyzer initialized."
        )



    def analyze(
        self,
        result,
        context=None
    ):


        analysis = {


            "type":
            "normal",


            "format":
            "text",


            "priority":
            "normal",


            "voice":
            False,


            "hud":
            False,


            "summary":
            False


        }



        intent = None



        if context:


            intent = getattr(

                context,

                "user_intent",

                None

            )



        #
        # SYSTEM REPORTS
        #

        if intent in [

            "system",

            "status",

            "hardware",

            "monitor"

        ]:


            analysis.update({

                "type":
                "system_report",


                "format":
                "report",


                "hud":
                True

            })



        #
        # CODING TASKS
        #

        elif intent in [

            "coding",

            "code"

        ]:


            analysis.update({

                "type":
                "technical",


                "format":
                "technical"

            })



        #
        # INTERNET / RESEARCH
        #

        elif intent in [

            "internet",

            "research"

        ]:


            analysis.update({

                "type":
                "research",


                "summary":
                True

            })



        #
        # VOICE MODE
        #

        if context:


            mode = getattr(

                context,

                "mode",

                None

            )


            if mode == "voice":


                analysis["voice"] = True



        AthenaLogger.info(

            f"[RESPONSE ANALYZER] {analysis['type']}"

        )


        return analysis
