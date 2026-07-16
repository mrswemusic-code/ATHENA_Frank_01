from src.core.logger.logger import AthenaLogger


class AthenaBus:


    def __init__(self):

        self.listeners = {}


    def subscribe(self, topic, callback):

        if topic not in self.listeners:

            self.listeners[topic] = []

        self.listeners[topic].append(callback)


    def publish(self, message):

        AthenaLogger.info(

            f"[BUS] {message.source}"

            f" -> {message.target}"

            f" ({message.topic})"

        )

        callbacks = self.listeners.get(

            message.topic,

            []

        )

        for callback in callbacks:

            callback(message)
