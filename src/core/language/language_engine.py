from src.core.language.personality import AthenaPersonality
from src.core.language.locale_manager import LocaleManager
from src.core.language import templates



class LanguageEngine:


    def __init__(self):

        self.personality = AthenaPersonality()

        self.locale = LocaleManager()



    def system_status(
        self,
        data,
        language="es"
    ):


        language = self.locale.detect(
            language
        )


        if language == "en":

            template = templates.SYSTEM_STATUS_EN


        elif language == "it":

            template = templates.SYSTEM_STATUS_IT


        else:

            template = templates.SYSTEM_STATUS_ES



        return template.format(

            cpu=data.get("cpu"),

            ram=data.get("ram"),

            disk=data.get("disk"),

            temperature=data.get("temperature")

        )
