from src.core.logger.logger import AthenaLogger
from src.core.kernel.kernel import AthenaKernel


class AthenaApplication:


    def __init__(self):

        AthenaLogger.info(
            "Initializing ATHENA Application..."
        )


        self.kernel = AthenaKernel()


        AthenaLogger.info(
            "ATHENA Application initialized."
        )



    def boot(self):


        AthenaLogger.info(
            "ATHENA Application boot sequence..."
        )


        self.kernel.boot()


        self.kernel.start()


        AthenaLogger.info(
            "ATHENA ONLINE."
        )



    def shutdown(self):


        AthenaLogger.info(
            "ATHENA shutdown requested."
        )


        self.kernel.stop()
