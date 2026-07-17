import threading
import time

from src.core.logger.logger import AthenaLogger
from src.core.planner.task_queue import TaskQueue



class EventLoop:


    def __init__(self, rate=1.0):

        self.running = False

        self.thread = None

        self.rate = rate

        self.tasks = TaskQueue()

        self.callbacks = []



    def register(self, callback):

        self.callbacks.append(callback)

        AthenaLogger.info(
            "[LOOP] Callback registered"
        )



    def add_task(self, task):

        self.tasks.add(task)



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


            self.tasks.run_pending()



            for callback in self.callbacks:

                callback()



            time.sleep(
                self.rate
            )
