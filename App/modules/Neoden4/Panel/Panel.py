from App.modules.Neoden4.NeodenDefinitions import NeodenFileIdentifiers


class Panel:
    def __init__(self, first_comp_x: float = 0.00, first_comp_y: float = 0.00, first_comp_rot: float = 0.00):
        self.identifier: NeodenFileIdentifiers = NeodenFileIdentifiers.SinglePanelIdentifier.value
        self.firstCompX: float = first_comp_x
        self.firstCompY: float = first_comp_y
        self.rotation: float = first_comp_rot
        self.skip: str = "No"


    def __str__(self):
        return "Identifier: {}, First Component X: {}, First Component Y: {}, First Component Rotation: {}, Skip: {}".format(
            self.identifier, self.firstCompX, self.firstCompY, self.rotation, self.skip
        )

    def __repr__(self):
        return "Identifier: {}, First Component X: {}, First Component Y: {}, First Component Rotation: {}, Skip: {}\n".format(
            self.identifier, self.firstCompX, self.firstCompY, self.rotation, self.skip
        )


    def getAsStringLine(self):
        return "{},{},{},{},{},".format(
            self.identifier, self.firstCompX, self.firstCompY, self.rotation, self.skip
        )



