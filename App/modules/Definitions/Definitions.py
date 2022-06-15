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
        self.availableNozzles = self.__linkFootprintPackages(self.__xmlHandler.getAvailableNozzles())
        self.installedNozzles = self.__linkAvailableNozzle(self.__xmlHandler.getInstalledNozzles())


    def __linkAvailableNozzle(self, raw_installed_nozzles: list [InstalledNozzle]) -> list[InstalledNozzle]:
        corrected_installed_nozzle_list: list[InstalledNozzle] = []

        for installed_nozzle in raw_installed_nozzles:
            new_installed_nozzle = InstalledNozzle(installed_nozzle.id, installed_nozzle.position, installed_nozzle.avNozzle)
            for av_nozzle in self.availableNozzles:
                if installed_nozzle.avNozzle.id == av_nozzle.id:
                    new_installed_nozzle.avNozzle = av_nozzle
                    break

            corrected_installed_nozzle_list.append(new_installed_nozzle)


        return corrected_installed_nozzle_list


    def __linkFootprintPackages(self, raw_availableNozzles: list[AvailableNozzle]) -> list[AvailableNozzle]:
        corrected_av_nozzles_list: list[AvailableNozzle] = []


        for av_nozzle in raw_availableNozzles:
            new_av_nozzle = AvailableNozzle(av_nozzle.nozzle, av_nozzle.id)

            for pickable_footprint in av_nozzle.pickableFootprintList:

                for footprint_package in self.footprintPackages:

                    if pickable_footprint.id == footprint_package.id:
                        new_av_nozzle.pickableFootprintList.append(footprint_package)
                        break

            corrected_av_nozzles_list.append(new_av_nozzle)


        return corrected_av_nozzles_list


    def getAvNozzlesNameList(self) -> list[str]:
        name_list: list[str] = []
        for av_nozzle in self.availableNozzles:
            name_list.append(av_nozzle.nozzle.name)
        return name_list

    def getInstalledNozzleByPosition(self, nozzle_position: int) -> InstalledNozzle:
        for installed_nozzle in self.installedNozzles:
            if installed_nozzle.position == nozzle_position:
                return installed_nozzle



