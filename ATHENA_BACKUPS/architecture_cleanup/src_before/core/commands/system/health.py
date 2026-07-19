from src.core.logger.logger import AthenaLogger


class HealthCommand:


    def __init__(self, kernel):

        self.kernel = kernel



    def execute(self):

        runtime = self.kernel.get(
            "runtime"
        )


        if not runtime:

            return {
                "error":
                "Runtime unavailable"
            }


        AthenaLogger.info(
            "[COMMAND] Health requested"
        )


        return runtime.status()
