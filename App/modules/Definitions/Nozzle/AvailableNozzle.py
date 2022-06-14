from App.modules.Neoden4.Nozzle.Nozzle import Nozzle
from App.modules.Definitions.Footprint.FootprintPackage import FootprintPackage



class AvailableNozzle(Nozzle):
    def __init__(self, nozzle: Nozzle = Nozzle(), nozzle_id: int = 0):
        super(AvailableNozzle, self).__init__()
        self.nozzle: Nozzle = nozzle
        self.nozzleId: int = nozzle_id
        self.pickableFootprintList: list[FootprintPackage] = []


    def __str__(self):
        return "Id: {}, Nozzle: {}, Pickable Footprints: {}".format(
            self.nozzleId, self.nozzle, self.pickableFootprintList
        )

    def __repr__(self):
        return "Id: {}, Nozzle: {}, Pickable Footprints: {}\n".format(
            self.nozzleId, self.nozzle, self.pickableFootprintList
        )



