from App.modules.PCB.Definitions.Definitions import PCBSide

class Position:
    def __init__(self, x_pos: float = 0.00, y_pos: float = 0.00, rot: float = 0.00, pcb_side: PCBSide = PCBSide.NotDefined):
        self.ori_xPos: float = x_pos
        self.transformedX_pos: float = 0.00
        self.ori_yPos: float = y_pos
        self.transformedY_pos: float = 0.00
        self.ori_rotation: float = rot
        self.transformedRotation: float = 0.00
        self.pcbSide: PCBSide = pcb_side

    def __str__(self):
        return "Original X: {}, Original Y: {}, Original Rotation: {}, {}\n" \
               "Transformed X: {}, Transformed Y: {}, Transformed Rotation: {}".format(
            self.ori_xPos, self.ori_yPos, self.ori_rotation, self.pcbSide,
            self.transformedX_pos, self.transformedY_pos, self.transformedRotation
        )


    def __repr__(self):
        return "Original X: {}, Original Y: {}, Original Rotation: {}, {}\n" \
               "Transformed X: {}, Transformed Y: {}, Transformed Rotation: {}\n".format(
            self.ori_xPos, self.ori_yPos, self.ori_rotation, self.pcbSide,
            self.transformedX_pos, self.transformedY_pos, self.transformedRotation
        )

