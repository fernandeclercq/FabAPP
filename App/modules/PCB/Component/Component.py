from App.modules.PCB.Component.Footprint.Footprint import Footprint
from App.modules.PCB.Component.Position.Position import Position
from App.modules.PCB.Definitions.Definitions import GenerationSoftware


class Component(Footprint, Position):
    def __init__(self, ref_name: str = "", ori_val: str = "", pos: Position = Position(),
                 fpt: Footprint = Footprint()):
        super().__init__()
        self.refName = ref_name
        self.Value = ori_val
        self.position = pos
        self.footprint = fpt
        self._generationSoftware: GenerationSoftware = GenerationSoftware.NotDefined


    @property
    def generationSoftware(self):
        return self._generationSoftware

    @generationSoftware.setter
    def generationSoftware(self, val: GenerationSoftware):
        self._generationSoftware = val
        self.footprint.footprintGenSoft = val
        self.position.positionGenSoft = val


    def __str__(self):
        return "Reference name: {},Value: {}, Position: {}, Footprint: {}".format(
            self.refName, self.Value, self.position, self.footprint
        )

    def __repr__(self):
        return "Reference name: {}, Value: {}, Position: {}, Footprint: {}\n".format(
            self.refName, self.Value, self.position, self.footprint
        )

