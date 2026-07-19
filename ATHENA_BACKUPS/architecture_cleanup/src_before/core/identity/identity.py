class AthenaIdentity:


    def __init__(self):

        self.name = "ATHENA"

        self.codename = (
            "Adaptive Tactical "
            "Heuristic Executive "
            "Neural Assistant"
        )

        self.version = "0.3-alpha"

        self.mode = "CORE"



    def info(self):

        return {

            "name": self.name,

            "codename": self.codename,

            "version": self.version,

            "mode": self.mode

        }
