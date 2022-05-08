from App.modules.PCB.Component.Footprint.Footprint import Footprint
from App.modules.PCB.Component.Position.Position import Position


class Component(Footprint, Position):
    def __init__(self, ref_name: str = "", ori_val: str = "", val: str = "", pos: Position = Position(),
                 fpt: Footprint = Footprint()):
        super().__init__()
        self.refName = ref_name
        self.originalValue = ori_val
        self.value = val
        self.position = pos
        self.footprint = fpt


    def __str__(self):
        return "Reference name: {}, Original value: {}, Value: {}, Position: {}, Footprint: {}".format(
            self.refName, self.originalValue, self.value, self.position, self.footprint
        )

    def __repr__(self):
        return "Reference name: {}, Original value: {}, Value: {}, Position: {}, Footprint: {}\n".format(
            self.refName, self.originalValue, self.value, self.position, self.footprint
        )

