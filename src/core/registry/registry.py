from src.core.logger.logger import AthenaLogger


class AthenaRegistry:


    def __init__(self):

        self.components = {}



    def register(
        self,
        name,
        component
    ):


        if name in self.components:

            AthenaLogger.info(
                f"[REGISTRY] Updating {name}"
            )

        else:

            AthenaLogger.info(
                f"[REGISTRY] Registered {name}"
            )


        self.components[name] = component



    def get(
        self,
        name
    ):


        component = self.components.get(
            name
        )


        if component is None:

            AthenaLogger.info(
                f"[REGISTRY] Missing component: {name}"
            )


        return component



    def has(
        self,
        name
    ):


        return name in self.components



    def list(self):


        return list(
            self.components.keys()
        )



    def clear(self):


        self.components.clear()


        AthenaLogger.info(
            "[REGISTRY] Cleared"
        )

