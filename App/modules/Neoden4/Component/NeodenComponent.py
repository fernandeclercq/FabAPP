from App.modules.PCB.Component.Component import Component, Position, Footprint


class NeodenComponent(Component):
    def __init__(self, pcb_comp: Component):
        super(NeodenComponent, self).__init__()

        self.feederId: int = 1
        self.nozzle: int = 1
        self._component: Component = pcb_comp
        self.skip: str = "No"



    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, val: Component):
        self._component = val



    def __str__(self):
        return "Feeder Id: {}, Nozzle: {}, Skip: {},\n Component: {}".format(
            self.feederId, self.nozzle, self.skip, self.component
        )


    def __repr__(self):
        return "Feeder Id: {}, Nozzle: {}, Skip: {},\n Component: {}\n".format(
            self.feederId, self.nozzle, self.skip, self.component
        )




        