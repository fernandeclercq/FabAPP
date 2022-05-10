from App.modules.PCB.Definitions.Definitions import PCBSide, NeodenOfsset


class Position:
    def __init__(self, x_pos: float = 0.00, y_pos: float = 0.00, rot: float = 0.00, pcb_side: PCBSide = PCBSide.NotDefined):
        self.ori_xPos: float = x_pos
        self.transformedX_pos: float = 0.00
        self.ori_yPos: float = y_pos
        self.transformedY_pos: float = 0.00
        self.ori_rotation: float = rot
        self.transformedRotation: float = 0.00
        self.pcbSide: PCBSide = pcb_side
        self.__offsetXY()
        self.__correctRotation()

    def __offsetXY(self):
        self.transformedX_pos = round((self.ori_xPos + NeodenOfsset.X_Offset.value), 2)
        self.transformedY_pos = round((self.ori_yPos + NeodenOfsset.Y_Offset.value), 2)

    def __correctRotation(self):
        if self.ori_rotation > 180:
            self.transformedRotation = round((self.ori_rotation - 360), 2)
        else:
            self.transformedRotation = round(self.ori_rotation, 2)

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

