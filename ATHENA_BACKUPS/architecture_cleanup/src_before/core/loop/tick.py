import time


class AthenaTick:


    def __init__(self, rate=1.0):

        self.rate = rate

        self.last_tick = time.time()

        self.counter = 0



    def update(self):

        now = time.time()

        elapsed = now - self.last_tick


        if elapsed >= self.rate:

            self.last_tick = now

            self.counter += 1

            return True


        return False



    def count(self):

        return self.counter
