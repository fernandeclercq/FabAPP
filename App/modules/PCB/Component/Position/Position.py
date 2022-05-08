class Position:
    def __init__(self, x_pos: float = 0.00, y_pos: float = 0.00, rot: int = 0):
        self.xPos = x_pos
        self.yPos = y_pos
        self.rotation = rot

    def __str__(self):
        return "X position: {}, Y Position: {}, Rotation: {}".format(
            self.xPos, self.yPos, self.rotation
        )


    def __repr__(self):
        return "X position: {}, Y Position: {}, Rotation: {}".format(
            self.xPos, self.yPos, self.rotation
        )

