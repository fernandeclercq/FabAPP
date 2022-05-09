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

    def _identifySoftwareCreated(self, zip_object: zipfile.ZipFile):
        if self.path != "":
            with zip_object.open(self.path, mode='r') as file:
                fl = file.readline().decode('UTF-8').strip('\r\n')
                if fl == "Ref,Val,Package,PosX,PosY,Rot,Side":
                    self.softwareCreated = GenerationSoftware.Kicad
                elif fl == "Name,X,Y,Angle,Value,Package":
                    self.softwareCreated = GenerationSoftware.Fusion360
                else:
                    self.softwareCreated = GenerationSoftware.Eagle


    def _populateEntryList(self, zip_object: zipfile.ZipFile):
        if self.path != "":
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



