import Submodules.Position as pos


class Component(pos.Position):
    def __init__(self):

        super().__init__()

        self.name = ""
        self.value = ""
        self.footprint = ""

