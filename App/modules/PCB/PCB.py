from App.modules.PCB.Component.Component import Component, Footprint, Position


class PCB(Component):
    def __init__(self):
        super(PCB, self).__init__()
        self.name = ""
        self.dateCreated = ""
        self.componentList: list[Component] = []

