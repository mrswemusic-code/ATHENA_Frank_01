from src.core.logger.logger import AthenaLogger
from src.core.kernel.kernel import AthenaKernel
from src.core.loop.event_loop import EventLoop


class AthenaApplication:


    def __init__(self):

        AthenaLogger.info(
            "Initializing ATHENA Application..."
        )


        # ==========================
        # ATHENA KERNEL
        # ==========================

        self.kernel = AthenaKernel()


        # ==========================
        # EVENT LOOP
        # ==========================

        self.loop = EventLoop()


        AthenaLogger.info(
            "ATHENA Application initialized."
        )



    def boot(self):


        AthenaLogger.info(
            "Application boot sequence started."
        )


        # Start kernel

        self.kernel.boot()



        # Register loop

        self.kernel.registry.register(
            "loop",
            self.loop
        )


        # Start event loop

        self.loop.start()



        AthenaLogger.info(
            "ATHENA APPLICATION ONLINE"
        )



    def shutdown(self):


        AthenaLogger.info(
            "ATHENA shutdown initiated."
        )


        self.loop.stop()


        AthenaLogger.info(
            "ATHENA OFFLINE"
        )
