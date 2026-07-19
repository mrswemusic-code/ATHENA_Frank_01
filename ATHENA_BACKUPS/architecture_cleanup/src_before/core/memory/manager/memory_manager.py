from datetime import datetime

from src.core.logger.logger import AthenaLogger



class MemoryManager:


    def __init__(self):

        self.records = []


        AthenaLogger.info(
            "Memory Manager initialized."
        )



    def remember(
        self,
        category,
        data
    ):


        record = {


            "category":
            category,


            "data":
            data,


            "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }


        self.records.append(
            record
        )


        AthenaLogger.info(
            f"[MEMORY] Stored {category}"
        )


        return record



    def recall(
        self,
        category=None
    ):


        if category is None:

            return self.records



        return [

            item

            for item in self.records

            if item["category"] == category

        ]



    def latest(
        self
    ):


        if not self.records:

            return None


        return self.records[-1]
