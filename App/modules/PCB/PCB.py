import zipfile
from App.modules.PCB.Component.Component import Component, Footprint, Position
from App.modules.PCB.PlacementFile.PlacementFile import PlacementFile


class PCB(Component, PlacementFile):
    def __init__(self, file_path: str = "N/A"):
        super(PCB, self).__init__()
        self.name = ""
        self.dateCreated = ""
        self.softwareCreated = ""
        self.path: str = file_path
        self.componentList: list[Component] = []
        self.placementFileList: list[PlacementFile] = []


    @property
    def path(self) -> str:
        return self.path

    @path.setter
    def path(self, value: str):
        self.path = value


