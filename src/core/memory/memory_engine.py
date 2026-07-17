from src.core.logger.logger import AthenaLogger

from src.core.memory.cache import MemoryCache
from src.core.memory.session import SessionMemory
from src.core.memory.database import MemoryDatabase
from src.core.memory.memory_record import MemoryRecord



class MemoryEngine:



    def __init__(self):


        AthenaLogger.info(
            "Memory Engine initialized."
        )


        self.cache = MemoryCache()

        self.session = SessionMemory()

        self.database = MemoryDatabase()



    def remember(
        self,
        key,
        value,
        category="general",
        persistent=False
    ):


        record = MemoryRecord(

            key=key,

            value=value,

            category=category

        )



        self.cache.set(

            key,

            record.to_dict()

        )


        self.session.remember(

            key,

            record.to_dict()

        )


        if persistent:

            self.database.set(

                key,

                record.to_dict()

            )



        AthenaLogger.info(

            f"[MEMORY] Stored -> {key}"

        )


        return record.to_dict()



    def recall(
        self,
        key
    ):


        value = self.cache.get(

            key

        )


        if value:

            return value



        value = self.session.recall(

            key

        )


        if value:

            return value



        return self.database.get(

            key

        )



    def search(
        self,
        text
    ):


        results = []


        database = self.database.all()


        for key,value in database.items():


            content = str(value).lower()


            if text.lower() in content:


                results.append(

                    value

                )


        return results



    def snapshot(self):


        return {


            "cache":

            self.cache.all(),


            "session":

            self.session.snapshot(),


            "database":

            self.database.all()

        }
