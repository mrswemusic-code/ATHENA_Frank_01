from src.core.logger.logger import AthenaLogger


class DiagnosticsCommand:


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
            "[COMMAND] Diagnostics requested"
        )


        return runtime.diagnostics_report()
