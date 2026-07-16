from datetime import datetime


class AthenaTelemetry:


    def __init__(self):

        self.events = []



    def record(self, event, data=None):


        packet = {

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "event":
                event,

            "data":
                data

        }


        self.events.append(
            packet
        )


        return packet



    def latest(self):

        return self.events[-1] if self.events else None
