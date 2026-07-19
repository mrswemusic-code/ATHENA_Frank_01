from src.core.logger.logger import AthenaLogger


class RuntimeCommand:


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
            "[COMMAND] Runtime requested"
        )


        return {

            "status":
                runtime.status(),

            "diagnostics":
                runtime.diagnostics_report()

        }
