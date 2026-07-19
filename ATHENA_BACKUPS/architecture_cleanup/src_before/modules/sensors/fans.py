import subprocess


class FanSensor:

    def rpm(self):

        try:

            output = subprocess.check_output(
                ["sensors"],
                text=True
            )

            for line in output.splitlines():

                if "Exhaust" in line:

                    return line.strip()

        except:

            return "Unknown"
