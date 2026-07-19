import os
import yaml

from src.core.logger.logger import AthenaLogger


class CapabilityLoader:


    def __init__(self, path="src/capabilities"):

        self.path = path
        self.capabilities = {}


    def load(self):

        if not os.path.exists(self.path):

            AthenaLogger.warning(
                "[CAPABILITY] Directory missing"
            )

            return {}


        for file in os.listdir(self.path):

            if file.endswith(".yaml"):

                full_path = os.path.join(
                    self.path,
                    file
                )


                with open(
                    full_path,
                    "r"
                ) as f:

                    data = yaml.safe_load(f)


                agent = data.get(
                    "agent"
                )


                if agent:

                    self.capabilities[agent] = data


                    AthenaLogger.info(
                        f"[CAPABILITY] Loaded {agent}"
                    )


        return self.capabilities
