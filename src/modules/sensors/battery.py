import subprocess


class BatterySensor:

    def level(self):

        try:

            output = subprocess.check_output(
                ["acpi", "-b"],
                text=True
            )

            return output.strip()

        except:

            return "Unknown"
