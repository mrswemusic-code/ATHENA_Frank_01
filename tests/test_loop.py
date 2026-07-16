import time

from src.core.loop.event_loop import EventLoop



def heartbeat():

    print(
        "ATHENA HEARTBEAT"
    )



loop = EventLoop(
    rate=1
)


loop.register(
    heartbeat
)


loop.start()


time.sleep(5)


loop.stop()
