import enum
import xml.etree.ElementTree as ET
from App.modules.Definitions.Footprint.FootprintPackage import FootprintPackage
from App.modules.Definitions.Nozzle.AvailableNozzle import AvailableNozzle, Nozzle
from App.modules.Definitions.Nozzle.InstalledNozzle import InstalledNozzle



class XMLTags(enum.Enum):
    Neoden = "Neoden4"
    Origin = "origin"
    X = "x"
    Y = "y"
    FootprintList = "footprints"
    FootprintSingle = "ft"
    Id = "id"
    FootprintName = "name"
    FootprintLength = "length"
    FootprintThickness = "thickness"
    NozzleList = "nozzles"
    NozzleInstalledList = "installed-nozzle"
    NozzleInstalledSingle = "in"
    NozzleInstalledPosition = "position"
    NozzleRefId = "nozzle-id"
    NozzleAvailableList = "available-nozzle"
    NozzleAvailableSingle = "an"
    NozzleAvailableName = "name"
    NozzleAvailablePickableFootprintList = "pickable-footprints"
    NozzleAvailablePickableFootprintSingle = "pf"
    NozzleAvailablePickableFootprintRef = "footprint-id"

    def __str__(self):
        return str(self.value)



class XMLHandler(object):
    def __init__(self):
        super().__init__()
        self._definitionsPath: str = "./config/definitions.xml"
        self._xmlRoot: ET.Element
        self._xmlTree: ET.ElementTree
        self._populateData()


    def _populateData(self):
        with open(self.definitionsPath) as xml_file:
            self._xmlTree = ET.parse(xml_file)
            self._xmlRoot = self._xmlTree.getroot()

    @property
    def definitionsPath(self):
        return self._definitionsPath

    @definitionsPath.setter
    def definitionsPath(self, val):
        self._definitionsPath = val


    def getOriginValues(self) -> [float, float]:
        x_val = float(self._xmlRoot.find(XMLTags.Neoden.value).find(XMLTags.Origin.value).find(XMLTags.X.value).text)
        y_val = float(self._xmlRoot.find(XMLTags.Neoden.value).find(XMLTags.Origin.value).find(XMLTags.Y.value).text)
        return [x_val, y_val]


    def getFootprints(self) -> list[FootprintPackage]:
        new_footprint_package_list: list[FootprintPackage] = []

        footprints = self._xmlRoot.find(XMLTags.FootprintList.value)
        for footprint_package in footprints.findall(XMLTags.FootprintSingle.value):
            new_footprint_package = FootprintPackage(0)
            new_footprint_package.id = int(footprint_package.attrib[XMLTags.Id.value])
            new_footprint_package.name = footprint_package.find(XMLTags.FootprintName.value).text
            new_footprint_package.length = footprint_package.find(XMLTags.FootprintLength.value).text
            new_footprint_package.thickness = footprint_package.find(XMLTags.FootprintThickness.value).text
            new_footprint_package_list.append(new_footprint_package)

        return new_footprint_package_list


    def getAvailableNozzles(self) -> list[AvailableNozzle]:
        new_available_nozzles_list: list[AvailableNozzle] = []

        all_nozzles = self._xmlRoot.find(XMLTags.NozzleList.value)
        available_nozzles = all_nozzles.find(XMLTags.NozzleAvailableList.value)
        for available_nozzle in available_nozzles.findall(XMLTags.NozzleAvailableSingle.value):
            new_available_nozzle = AvailableNozzle()
            new_available_nozzle.id = int(available_nozzle.attrib[XMLTags.Id.value])
            new_available_nozzle.nozzle = Nozzle(available_nozzle.find(XMLTags.NozzleAvailableName.value).text)

            pickable_footprints = available_nozzle.find(XMLTags.NozzleAvailablePickableFootprintList.value)
            for pickable_footprint in pickable_footprints.findall(XMLTags.NozzleAvailablePickableFootprintSingle.value):
                new_footprint_package = FootprintPackage(0)
                new_footprint_package.id = int(pickable_footprint.find(XMLTags.NozzleAvailablePickableFootprintRef.value).text)

                new_available_nozzle.pickableFootprintList.append(new_footprint_package)



            new_available_nozzles_list.append(new_available_nozzle)


        return new_available_nozzles_list


    def getInstalledNozzles(self) -> list[InstalledNozzle]:
        new_installed_nozzles_list: list[InstalledNozzle] = []
        all_nozzles = self._xmlRoot.find(XMLTags.NozzleList.value)
        installed_nozzles = all_nozzles.find(XMLTags.NozzleInstalledList.value)
        for installed_nozzle in installed_nozzles.findall(XMLTags.NozzleInstalledSingle.value):
            new_installed_nozzle = InstalledNozzle()
            new_installed_nozzle.id = int(installed_nozzle.attrib[XMLTags.Id.value])
            new_installed_nozzle.position = int(installed_nozzle.find(XMLTags.NozzleInstalledPosition.value).text)
            new_installed_nozzle.avNozzle = AvailableNozzle(Nozzle(), int(installed_nozzle.find(XMLTags.NozzleRefId.value).text))

            new_installed_nozzles_list.append(new_installed_nozzle)

        return new_installed_nozzles_list




