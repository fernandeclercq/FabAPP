from App.modules.Neoden4.NeodenDefinitions import NeodenFileIdentifiers


class FirstChipSetting:
    def __init__(self, columns: int = 1, rows: int = 1, left_bottom_x: float = 64.4, left_bottom_y: float = 9.83,
                 left_top_x: float = 0, left_top_y: float = 0, right_top_x: float = 0, right_top_y: float = 0,
                 pcb_angle: float = 0.00):
        self.columns: int = columns
        self.rows: int = rows
        self.leftBottomX: float = left_bottom_x
        self.leftBottomY: float = left_bottom_y
        self.leftTopX: float = left_top_x
        self.leftTopY: float = left_top_y
        self.rightTopX: float = right_top_x
        self.rightTopY: float = right_top_y
        self.pcbAngle: float = pcb_angle


    @classmethod
    def fromXYCoordinates(cls, _left_bottom_x: float, _left_bottom_y: float,):
        return cls(
            columns=1, rows=1, left_bottom_x=_left_bottom_x, left_bottom_y=_left_bottom_y, left_top_x=0,
            left_top_y=0, right_top_x=0, right_top_y=0, pcb_angle=0.00
        )


    def __str__(self):
        return "Colums: {}, Rows: {}, Left Bottom X: {}, Left Bottom Y: {}, Left Top X: {}, Left Top Y: {}, " \
               "Right Top X: {}, Right Top Y: {}, PCB Angle: {}".format(
                self.columns, self.rows, self.leftBottomX, self.leftBottomY, self.leftTopX, self.leftTopY,
                self.rightTopX, self.rightTopY, self.pcbAngle
                )

    def __repr__(self):
        return "Colums: {}, Rows: {}, Left Bottom X: {}, Left Bottom Y: {}, Left Top X: {}, Left Top Y: {}, " \
               "Right Top X: {}, Right Top Y: {}, PCB Angle: {}\n".format(
                self.columns, self.rows, self.leftBottomX, self.leftBottomY, self.leftTopX, self.leftTopY,
                self.rightTopX, self.rightTopY, self.pcbAngle
                )


    def getAsStringLine(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(
            NeodenFileIdentifiers.PCBPanelIdentifier.value, self.columns, self.rows, self.leftBottomX, self.leftBottomY,
            self.leftTopX, self.leftTopY, self.rightTopX, self.rightTopY, self.pcbAngle
        )
