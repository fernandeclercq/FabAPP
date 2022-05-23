import zipfile
from App.modules.PCB.Definitions.Definitions import PCBSide, GenerationSoftware, KicadHeader, EagleHeader, NeodenHeader
import enum

class PlacementFile:
    def __init__(self, path: str = "N/A", pcb_side: PCBSide = PCBSide.NotDefined,
                 generation_software: GenerationSoftware = GenerationSoftware.NotDefined):
        self.pcbSide: PCBSide = pcb_side
        self.path = path
        self.softwareCreated: GenerationSoftware = generation_software
        self.entryList: list[list[str]] = []

    def __repr__(self):
        return "{}, {}, File path: {}\n".format(
            self.softwareCreated, self.pcbSide, self.path
        )

    def __str__(self):
        return "{}, {}, File path: {}".format(
            self.softwareCreated, self.pcbSide, self.path
        )

    def _identifySoftwareCreatedFromZip(self, zip_object: zipfile.ZipFile):
        if self.path != "N/A":
            with zip_object.open(self.path, mode='r') as file:
                fl = file.readline().decode('UTF-8').strip('\r\n')
                if fl == "Ref,Val,Package,PosX,PosY,Rot,Side":
                    self.softwareCreated = GenerationSoftware.Kicad
                elif fl == "Name,X,Y,Angle,Value,Package":
                    self.softwareCreated = GenerationSoftware.Fusion360
                else:
                    self.softwareCreated = GenerationSoftware.Eagle

    def _identifySoftwareCreatedFromFile(self):
        if self.path != "N/A":
            with open(self.path, mode='r') as file:
                fl = file.readline().strip('\r\n')
                if fl == "Ref,Val,Package,PosX,PosY,Rot,Side":
                    self.softwareCreated = GenerationSoftware.Kicad
                elif fl == "Name,X,Y,Angle,Value,Package":
                    self.softwareCreated = GenerationSoftware.Fusion360
                else:
                    self.softwareCreated = GenerationSoftware.Eagle


    def _getPCBNameFromFile(self) -> str:
        if self.path != "N/A":
            idx_slash = self.path.rfind('/')
            idx_suffix = 0

            if self.softwareCreated == GenerationSoftware.Kicad:
                if self.pcbSide == PCBSide.BOT:
                    idx_suffix = len("-bottom-pos.csv")
                    return self.path[idx_slash + 1:-idx_suffix]
                elif self.pcbSide == PCBSide.TOP:
                    idx_suffix = len("-top-pos.csv")
                    return self.path[idx_slash + 1:-idx_suffix]

            else:
                if self.pcbSide == PCBSide.BOT:
                    idx_suffix = len("-board_back.csv")
                    return self.path[idx_slash + 1: -idx_suffix]
                elif self.pcbSide == PCBSide.TOP:
                    idx_suffix = len("-board_front.csv")
                    return self.path[idx_slash + 1: -idx_suffix]




    def _populateEntryListFromZip(self, zip_object: zipfile.ZipFile):
        if self.path != "N/A":
            with zip_object.open(self.path, mode='r') as file:
                lastEntryReached = False
                entryCount = 0
                while not lastEntryReached:
                    entry = file.readline().decode('UTF-8').strip('\r\n')
                    if entry != "":
                        if entryCount == 0:
                            if self.softwareCreated == GenerationSoftware.Kicad or self.softwareCreated == GenerationSoftware.Fusion360:
                                pass
                            else:
                                self.entryList.append(entry.split(','))
                        else:
                            self.entryList.append(entry.split(','))
                        entryCount += 1
                    else:
                        lastEntryReached = True
                        break

    def _populateEntryListFromFile(self):
        if self.path != "N/A":
            with open(self.path, mode='r') as file:
                lastEntryReached = False
                entryCount = 0
                while not lastEntryReached:
                    entry = file.readline().strip('\r\n')
                    if entry != "":
                        if entryCount == 0:
                            if self.softwareCreated == GenerationSoftware.Kicad or self.softwareCreated == GenerationSoftware.Fusion360:
                                pass
                            else:
                                self.entryList.append(entry.split(','))
                        else:
                            self.entryList.append(entry.split(','))
                        entryCount += 1
                    else:
                        lastEntryReached = True
                        break



