import enum
import xml.etree.ElementTree as ET
from App.modules.PCB.Component.Footprint import Footprint


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
        x_val: float = 0.00
        y_val: float = 0.00

        x_val = float(self._xmlRoot.find(XMLTags.Neoden.value).find(XMLTags.Origin.value).find(XMLTags.X.value).text)
        y_val = float(self._xmlRoot.find(XMLTags.Neoden.value).find(XMLTags.Origin.value).find(XMLTags.Y.value).text)

        return [x_val, y_val]





