import time


class BootManager:

    def __init__(self):

        self.modules = [

            "Configuration",
            "Memory",
            "Overlay",
            "Voice",
            "Events",
            "Agents",
            "Widgets",
            "System Monitor"

        ]

    def boot(self):

        print("")

        for module in self.modules:

            print(f"[ OK ] {module}")

            time.sleep(0.15)

        print("")
        print("ATHENA READY")
