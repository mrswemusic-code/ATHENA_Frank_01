from src.core.logger.logger import AthenaLogger

import threading
import time
import traceback



class EventLoop:


    def __init__(
        self,
        kernel=None,
        rate=1.0
    ):

        self.kernel = kernel

        self.running = False

        self.thread = None

        self.rate = rate

        self.callbacks = []

        self.tick = 0

        self.state = "IDLE"


        AthenaLogger.info(
            "[LOOP] Event Loop initialized."
        )



    def register(self, callback):

        self.callbacks.append(
            callback
        )


        AthenaLogger.info(
            "[LOOP] Callback registered"
        )



    def add_task(self, task):

        if not self.kernel:

            AthenaLogger.warning(
                "[LOOP] Kernel unavailable"
            )

            return



        task_manager = self.kernel.get(
            "tasks"
        )


        if not task_manager:

            AthenaLogger.warning(
                "[LOOP] Task Manager unavailable"
            )

            return



        task_manager.submit(
            task
        )


        AthenaLogger.info(
            f"[LOOP] Task submitted -> {task.name}"
        )



    def process_input(self, text):

        if not self.kernel:

            AthenaLogger.warning(
                "[LOOP] Kernel unavailable"
            )

            return None



        executive = self.kernel.get(
            "executive"
        )


        if not executive:

            AthenaLogger.warning(
                "[LOOP] Executive unavailable"
            )

            return None



        AthenaLogger.info(
            "[LOOP] Processing input"
        )


        return executive.cycle(
            text
        )



    def autonomous_cycle(self):

        if not self.kernel:

            return



        telemetry = self.kernel.get(
            "telemetry"
        )


        if telemetry:

            AthenaLogger.info(
                "[LOOP] Autonomous telemetry cycle"
            )



    def process_tasks(self):

        if not self.kernel:

            return



        task_manager = self.kernel.get(
            "tasks"
        )


        if not task_manager:

            return



        while task_manager.pending() > 0:

            task_manager.execute_next()



    def start(self):

        if self.running:

            return



        self.running = True

        self.state = "ACTIVE"



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

        self.state = "OFFLINE"


        AthenaLogger.info(
            "Event Loop OFFLINE"
        )



    def run(self):

        AthenaLogger.info(
            "[LOOP] Runtime started"
        )


        while self.running:


            try:


                self.tick += 1


                self.process_tasks()


                self.autonomous_cycle()



                for callback in self.callbacks:


                    try:

                        callback()


                    except Exception:


                        AthenaLogger.error(
                            traceback.format_exc()
                        )



                time.sleep(
                    self.rate
                )



            except Exception:


                AthenaLogger.error(
                    traceback.format_exc()
                )



        AthenaLogger.info(
            "[LOOP] Runtime stopped"
        )
