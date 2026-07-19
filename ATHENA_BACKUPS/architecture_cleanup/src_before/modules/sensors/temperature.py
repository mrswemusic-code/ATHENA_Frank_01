import subprocess


class TemperatureSensor:

    def cpu(self):

        try:

            output = subprocess.check_output(
                ["sensors"],
                text=True
            )

            for line in output.splitlines():

                if "Package id 0" in line:

                    return line.split("+")[1].split("°")[0]

        except:

            return None
