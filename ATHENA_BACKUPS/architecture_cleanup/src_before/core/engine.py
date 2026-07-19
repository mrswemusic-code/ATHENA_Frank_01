class AthenaEngine:

    def __init__(self, name):

        self.name = name

        self.online = False


    def start(self):

        self.online = True


    def stop(self):

        self.online = False


    def status(self):

        return self.online
