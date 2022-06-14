from App.modules.Definitions.XMLHandler import XMLHandler
from App.modules.Definitions.Footprint.FootprintPackage import FootprintPackage
from App.modules.Definitions.Nozzle.AvailableNozzle import AvailableNozzle
from App.modules.Definitions.Nozzle.InstalledNozzle import InstalledNozzle



class Definition:
    def __init__(self):
        super().__init__()
        self.__xmlHandler = XMLHandler()
        self.originX: float = -1.00
        self.originY: float = -1.00
        self.footprintPackages: list[FootprintPackage] = []
        self.installedNozzles: list[InstalledNozzle] = []
        self.availableNozzles: list[AvailableNozzle] = []


    def initializeXmlHandler(self):
        self.originX, self.originY = self.__xmlHandler.getOriginValues()
        self.footprintPackages = self.__xmlHandler.getFootprints()
        self.availableNozzles = self.__xmlHandler.getAvailableNozzles()
        #self.linkFootprintPackages()
        self.installedNozzles = self.__xmlHandler.getInstalledNozzles()




    #def linkFootprintPackages(self):




