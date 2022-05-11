from App.modules.PCB.Fiducial.Fiducial import Fiducial
from App.modules.Neoden4.NeodenDefinitions import NeodenFileIdentifiers, LightSource


class NeodenFiducial(Fiducial):
    def __init__(self, fiducial: Fiducial):
        super(NeodenFiducial, self).__init__()
        self.identifier: NeodenFileIdentifiers = NeodenFileIdentifiers.SingleFiducialIdentifier
        self.fiducial: Fiducial = fiducial
        self.min: float = 0.8
        self.max: float = 3
        self.lightSource: LightSource = LightSource.Inner
        self.brightness = 0


    def __str__(self):
        return "Identifier: {}, Min: {}, Max{}, Light Source: {}, Brightness: {}\nFiducial: {}".format(
            self.identifier, self.min, self.max, self.lightSource, self.brightness, self.fiducial
        )

    def __repr__(self):
        return "Identifier: {}, Min: {}, Max{}, Light Source: {}, Brightness: {}\nFiducial: {}\n".format(
            self.identifier, self.min, self.max, self.lightSource, self.brightness, self.fiducial
        )
        