from App.modules.PCB.Component.Footprint.Footprint import Footprint


class FootprintPackage(Footprint):
    def __init__(self, footprint_id: int, footprint: Footprint = Footprint(), length: float = -1.00, thickness: float = -1.00):
        super(FootprintPackage, self).__init__()
        self.id: int = footprint_id
        self.footprint: Footprint = footprint
        self._name: str = "N/A"
        self.length: float = length
        self.thickness: float = thickness

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val
        self.footprint.Value = val


    def __str__(self):
        return "Id: {}, Name: {}, Length: {}, Thickness: {}".format(
            self.id, self.name, self.length, self.thickness
        )

    def __repr__(self):
        return "Id: {}, Name: {}, Length: {}, Thickness: {}\n".format(
            self.id, self.name, self.length, self.thickness
        )

