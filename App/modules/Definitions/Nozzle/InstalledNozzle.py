from App.modules.Definitions.Nozzle.AvailableNozzle import AvailableNozzle



class InstalledNozzle(AvailableNozzle):
    def __init__(self, nozzle_id: int = 0, position: int = 0, nozzle: AvailableNozzle = AvailableNozzle()):
        super(InstalledNozzle, self).__init__()
        self.nozzle: AvailableNozzle = nozzle
        self.position: int = position
        self.id: int = nozzle_id


    def __str__(self):
        return "Installed Nozzle - Id: {}, Position: {}, Nozzle: {}".format(
            self.id, self.position, self.nozzle
        )

    def __repr__(self):
        return "Installed Nozzle - Id: {}, Position: {}, Nozzle: {}\n".format(
            self.id, self.position, self.nozzle
        )



