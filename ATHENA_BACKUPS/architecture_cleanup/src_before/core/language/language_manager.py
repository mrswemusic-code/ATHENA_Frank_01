
from src.core.language.language_detector import LanguageDetector



class LanguageManager:



    def __init__(self):

        self.detector = LanguageDetector()



        self.current = "es"



    def analyze(
        self,
        text
    ):


        context = self.detector.detect(
            text
        )


        self.current = context.language


        return context



    def get_language(self):

        return self.current

