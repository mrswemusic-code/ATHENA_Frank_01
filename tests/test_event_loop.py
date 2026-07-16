import time

from src.core.loop.event_loop import EventLoop


loop = EventLoop()

loop.start()

time.sleep(5)

loop.stop()
