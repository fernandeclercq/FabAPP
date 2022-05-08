
class PlacementFile:
    def __init__(self, path: str = "N/A", file_name: str = "N/A", pcb_side: str = "N/A"):
        self.name = file_name
        self.pcbSide = pcb_side
        self.path = path

    def __repr__(self):
        return "File Name: {}, PCB Side: {}, File path: {}".format(
            self.name, self.pcbSide, self.path
        )

    def __str__(self):
        return "File Name: {}, PCB Side: {}, File path: {}".format(
            self.name, self.pcbSide, self.path
        )


