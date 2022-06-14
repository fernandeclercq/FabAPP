

class Nozzle:
    def __init__(self, nozzle_name: str = "N/A"):
        self.name = nozzle_name
        self.innerDiameter: float = 0.00
        self.outerDiameter: float = 0.00


    def __str__(self):
        return "Nozzle Name: {}".format(
            self.name
        )

    def __repr__(self):
        return "Nozzle Name: {}}\n".format(
            self.name,
        )

