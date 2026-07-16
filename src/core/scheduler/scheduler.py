import threading
import time


class Scheduler:

    def every(self, seconds, func):

        def loop():

            while True:

                func()

                time.sleep(seconds)

        threading.Thread(target=loop, daemon=True).start()
