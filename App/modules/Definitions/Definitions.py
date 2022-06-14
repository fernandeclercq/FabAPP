from App.modules.Definitions.XMLHandler import XMLHandler
from App.modules.PCB.Component.Footprint.Footprint import *


class Definition:
    def __init__(self):
        super().__init__()
        self.__xmlHandler = XMLHandler()
        self.originX: float = -1.00
        self.originY: float = -1.00
        self.footprintPackages: list[Footprint]



        print(self.__xmlHandler.getOriginValues())
