from src.core.events.event_bus import EventBus

from src.core.telemetry.event_detector import EventDetector



bus = EventBus()



def cpu_alert(event):

    print("\nHUD RECEIVED:")

    print(event)



bus.subscribe(
    "CPU_OVERLOAD",
    cpu_alert
)



detector = EventDetector(
    bus
)



detector.analyze(
    "cpu",
    95
)



print("\nBUS STATUS")

print(
    bus.stats()
)
