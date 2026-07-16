from src.core.bus.bus import AthenaBus

from src.core.bus.message import AthenaMessage


bus = AthenaBus()


def receiver(message):

    print()

    print("MESSAGE RECEIVED")

    print(message.source)

    print(message.topic)

    print(message.payload)

    print()


bus.subscribe(

    "system.status",

    receiver

)


bus.publish(

    AthenaMessage(

        source="Runtime",

        target="HUD",

        topic="system.status",

        payload={

            "cpu": 31,

            "ram": 48

        }

    )

)
