class Service:


    def __init__(self, name):

        self.name = name
        self.running = False


    def start(self):

        self.running = True
        print(f"[SERVICE START] {self.name}")


    def stop(self):

        self.running = False
        print(f"[SERVICE STOP] {self.name}")
