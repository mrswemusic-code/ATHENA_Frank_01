import threading
import time

from src.core.logger.logger import AthenaLogger


class EventLoop:

    def __init__(self):

        self.running = False

        self.thread = None


    def start(self):

        if self.running:

            return

        self.running = True

        self.thread = threading.Thread(

            target=self.run,

            daemon=True

        )

        self.thread.start()

        AthenaLogger.info(

            "Event Loop ONLINE"

        )


    def stop(self):

        self.running = False

        AthenaLogger.info(

            "Event Loop OFFLINE"

        )


    def run(self):

        while self.running:

            time.sleep(1)
