from App.modules.PCB.Definitions.Definitions import PCBSide, GenerationSoftware


class Position:
    def __init__(self, x_pos: float = 0.00, y_pos: float = 0.00, rot: float = 0.00, pcb_side: PCBSide = PCBSide.NotDefined):
        self.xPos: float = x_pos
        self.yPos: float = y_pos
        self.rotation: float = rot
        self.pcbSide: PCBSide = pcb_side
        self.positionGenSoft: GenerationSoftware = GenerationSoftware.NotDefined


    def __str__(self):
        return "X: {}, Y: {}, Rotation: {}, {}".format(
            self.xPos, self.yPos, self.rotation, self.pcbSide)


    def __repr__(self):
        return "X: {}, Y: {}, Rotation: {}, {}\n".format(
            self.xPos, self.yPos, self.rotation, self.pcbSide)

