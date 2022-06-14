from App.modules.Neoden4.Nozzle.Nozzle import Nozzle



class InstalledNozzle(Nozzle):
    def __init__(self, nozzle_id: int = 0, position: int = 0, nozzle: Nozzle = Nozzle()):
        super(InstalledNozzle, self).__init__()
        self.nozzle: Nozzle = nozzle
        self.position: int = position
        self.nozzleId: int = nozzle_id


    def __str__(self):
        return "Id: {}, Position: {}, Nozzle: {}".format(
            self.nozzleId, self.position, self.nozzle
        )

    def __repr__(self):
        return "Id: {}, Position: {}, Nozzle: {}\n".format(
            self.nozzleId, self.position, self.nozzle
        )



