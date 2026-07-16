from src.services.core.service import Service


class ServiceManager:


    def __init__(self):

        self.services = {}


    def register(self, service):

        self.services[service.name] = service


    def start_all(self):

        for service in self.services.values():

            service.start()


    def stop_all(self):

        for service in self.services.values():

            service.stop()
