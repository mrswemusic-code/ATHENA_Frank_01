class EngineManager:

    def __init__(self):

        self.engines = {}


    def register(self, engine):

        self.engines[engine.name] = engine


    def start_all(self):

        for engine in self.engines.values():

            engine.start()


    def stop_all(self):

        for engine in self.engines.values():

            engine.stop()


    def status(self):

        return {

            name: engine.status()

            for name, engine

            in self.engines.items()

        }
