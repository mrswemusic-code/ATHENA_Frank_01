from src.core.logger.logger import AthenaLogger

from src.core.memory.cache import MemoryCache

from src.core.memory.session import SessionMemory

from src.core.memory.database import MemoryDatabase



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
        persistent=False
    ):


        self.cache.set(
            key,
            value
        )


        self.session.remember(
            key,
            value
        )


        if persistent:

            self.database.set(
                key,
                value
            )



    def recall(
        self,
        key
    ):


        value = self.cache.get(
            key
        )


        if value is not None:

            return value



        value = self.session.recall(
            key
        )


        if value is not None:

            return value



        return self.database.get(
            key
        )



    def snapshot(self):

        return {

            "cache": self.cache.all(),

            "session": self.session.snapshot(),

            "database": self.database.all()

        }
