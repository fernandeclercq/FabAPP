from App.modules.PCB.Component.Component import Component, Footprint, Position
from App.modules.PCB.PlacementFile.PlacementFile import PlacementFile, PCBSide, GenerationSoftware
import zipfile


class PCB(Component, PlacementFile):
    def __init__(self):
        super(PCB, self).__init__()
        self.name = ""
        self.dateCreated = ""
        self.softwareCreated = ""
        self._path: str = "N/A"
        self.componentList: list[Component] = []
        self.placementFileList: list[PlacementFile] = []


    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str):
        self._path = value
        self.__identifyPlacementFiles()


    def __identifyPlacementFiles(self):
        self.placementFileList.clear()
        with zipfile.ZipFile(self._path, 'r') as myZip:
            for file in myZip.namelist():
                if file.endswith(".csv"):
                    if file.lower().find("top") != -1 or file.lower().find("front") != -1:
                        tp = PlacementFile(file, PCBSide.TOP)
                        tp.identifySoftwareCreated(myZip)
                        tp.populateEntryList(myZip)
                        print(tp)
                        self.placementFileList.append(tp)
                    elif file.lower().find("bot") != -1 or file.lower().find("back") != -1:
                        bt = PlacementFile(file, PCBSide.BOT)
                        bt.identifySoftwareCreated(myZip)
                        bt.populateEntryList(myZip)
                        print(bt)
                        self.placementFileList.append(bt)


    def getPlacementFile(self, side: PCBSide) -> PlacementFile:
        for file in self.placementFileList:
            if file.pcbSide == side:
                return file






