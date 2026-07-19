from src.core.logger.logger import AthenaLogger



class EventBus:


    def __init__(self):

        self.listeners = {}

        self.events_processed = 0



    def subscribe(
        self,
        event_name,
        callback
    ):


        if event_name not in self.listeners:

            self.listeners[event_name] = []


        self.listeners[event_name].append(
            callback
        )


        AthenaLogger.info(

            f"[BUS] Subscriber added: {event_name}"

        )



    def emit(
        self,
        event
    ):


        self.events_processed += 1


        AthenaLogger.info(

            f"[BUS] Event emitted: {event.name}"

        )



        if event.name not in self.listeners:

            return



        for callback in self.listeners[event.name]:

            callback(event)



    def stats(self):


        return {

            "listeners":
                len(self.listeners),


            "events_processed":
                self.events_processed

        }
