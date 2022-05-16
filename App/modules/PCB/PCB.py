from App.modules.PCB.Component.Component import Component, Footprint, Position
from App.modules.PCB.Fiducial.Fiducial import Fiducial
from App.modules.PCB.PlacementFile.PlacementFile import PlacementFile, PCBSide, GenerationSoftware, NeodenHeader, KicadHeader, EagleHeader
import zipfile


class PCB(Component, Fiducial, PlacementFile):
    def __init__(self):
        super(PCB, self).__init__()
        self.name = ""
        self.dateCreated = ""
        self.softwareCreated = ""
        self._path: str = "N/A"
        self.topComponentList: list[Component] = []
        self.botComponentList: list[Component] = []
        self.topFiducialList: list[Fiducial] = []
        self.botFiducialList: list[Fiducial] = []
        self.placementFileList: list[PlacementFile] = []


    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str):
        self._path = value
        self.__identifyPlacementFiles()
        self.__convertPlacementListToComponentList()
        self.name = self.__getPCBName()


    def __getPCBName(self) -> str:
        idx_last_sep = self._path.rfind('/')
        idx_ext_char = self._path.rfind('.')

        return self._path[idx_last_sep + 1:idx_ext_char]


    def __identifyPlacementFiles(self):
        self.placementFileList.clear()
        with zipfile.ZipFile(self._path, 'r') as myZip:
            for file in myZip.namelist():
                if file.endswith(".csv"):
                    if file.lower().find("top") != -1 or file.lower().find("front") != -1:
                        tp = PlacementFile(file, PCBSide.TOP)
                        tp._identifySoftwareCreated(myZip)
                        tp._populateEntryList(myZip)
                        self.placementFileList.append(tp)
                    elif file.lower().find("bot") != -1 or file.lower().find("back") != -1:
                        bt = PlacementFile(file, PCBSide.BOT)
                        bt._identifySoftwareCreated(myZip)
                        bt._populateEntryList(myZip)
                        self.placementFileList.append(bt)

    def __getPlacementFile(self, side: PCBSide) -> PlacementFile:
        for file in self.placementFileList:
            if file.pcbSide == side:
                return file

    def clearLists(self):
        self.topComponentList.clear()
        self.botComponentList.clear()
        self.topFiducialList.clear()
        self.botFiducialList.clear()

    def __convertPlacementListToComponentList(self):
        self.clearLists()
        if len(self.placementFileList) > 0:
            topPF = self.__getPlacementFile(PCBSide.TOP)
            botPF = self.__getPlacementFile(PCBSide.BOT)

            ## Top & Bot components / Fiducials - KiCad
            if topPF.softwareCreated == GenerationSoftware.Kicad:
                for x in range(len(topPF.entryList)):
                    newFootprint = Footprint(topPF.entryList[x][KicadHeader.Footprint.value].strip("\" "))
                    newPosition = Position(float(topPF.entryList[x][KicadHeader.X_Pos.value].strip(" ")),
                                           float(topPF.entryList[x][KicadHeader.Y_Pos.value].strip(" ")),
                                           float(topPF.entryList[x][KicadHeader.Rotation.value].strip(" ")),
                                           PCBSide.TOP)

                    if newFootprint.Value.lower().find("fid") != -1 or newFootprint.Value.lower().find("fiducial") != -1:
                        newFid = Fiducial(topPF.entryList[x][KicadHeader.Name.value].strip("\" "),
                                          topPF.entryList[x][KicadHeader.Val.value].strip("\" "),
                                          newPosition, newFootprint)
                        newFid.generationSoftware = GenerationSoftware.Kicad
                        self.topFiducialList.append(newFid)
                    else:
                        newComp = Component(topPF.entryList[x][KicadHeader.Name.value].strip("\" "),
                                            topPF.entryList[x][KicadHeader.Val.value].strip("\" "),
                                            newPosition, newFootprint)
                        newComp.generationSoftware = GenerationSoftware.Kicad
                        self.topComponentList.append(newComp)

            if botPF.softwareCreated == GenerationSoftware.Kicad:
                for x in range(len(botPF.entryList)):
                    newFootprint = Footprint(botPF.entryList[x][KicadHeader.Footprint.value].strip("\" "))
                    newPosition = Position(float(botPF.entryList[x][KicadHeader.X_Pos.value].strip(" ")),
                                           float(botPF.entryList[x][KicadHeader.Y_Pos.value].strip(" ")),
                                           float(botPF.entryList[x][KicadHeader.Rotation.value].strip(" ")),
                                           PCBSide.BOT)

                    if newFootprint.Value.lower().find("fid") != -1 or newFootprint.Value.lower().find("fiducial") != -1:
                        newFid = Fiducial(botPF.entryList[x][KicadHeader.Name.value].strip("\" "),
                                          botPF.entryList[x][KicadHeader.Val.value].strip("\" "),
                                          newPosition, newFootprint)
                        newFid.generationSoftware = GenerationSoftware.Kicad
                        self.botFiducialList.append(newFid)
                    else:
                        newComp = Component(botPF.entryList[x][KicadHeader.Name.value].strip("\" "),
                                            botPF.entryList[x][KicadHeader.Val.value].strip("\" "),
                                            newPosition, newFootprint)
                        newComp.generationSoftware = GenerationSoftware.Kicad
                        self.botComponentList.append(newComp)


            ### Top & Bot Components - Eagle
            if topPF.softwareCreated == GenerationSoftware.Eagle:
                for x in range(len(topPF.entryList)):
                    newFootprint = Footprint(topPF.entryList[x][EagleHeader.Footprint.value].strip("\" "))
                    newPosition = Position(float(topPF.entryList[x][EagleHeader.X_Pos.value].strip(" ")),
                                           float(topPF.entryList[x][EagleHeader.Y_Pos.value].strip(" ")),
                                           float(topPF.entryList[x][EagleHeader.Rotation.value].strip(" ")),
                                           PCBSide.TOP)

                    if newFootprint.Value.lower().find("fid") != -1 or newFootprint.Value.lower().find("fiducial") != -1:
                        newFid = Fiducial(topPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                          topPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                          newPosition, newFootprint)
                        newFid.generationSoftware = GenerationSoftware.Eagle
                        self.topFiducialList.append(newFid)

                    else:
                        newComp = Component(topPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                            topPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                            newPosition, newFootprint)
                        newComp.generationSoftware = GenerationSoftware.Eagle
                        self.topComponentList.append(newComp)

            if botPF.softwareCreated == GenerationSoftware.Eagle:
                for x in range(len(botPF.entryList)):
                    newFootprint = Footprint(botPF.entryList[x][EagleHeader.Footprint.value].strip("\" "))
                    newPosition = Position(float(botPF.entryList[x][EagleHeader.X_Pos.value].strip(" ")),
                                           float(botPF.entryList[x][EagleHeader.Y_Pos.value].strip(" ")),
                                           float(botPF.entryList[x][EagleHeader.Rotation.value].strip(" ")),
                                           PCBSide.BOT)

                    if newFootprint.Value.lower().find("fid") != -1 or newFootprint.Value.lower().find("fiducial") != -1:
                        newFid = Fiducial(botPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                          botPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                          newPosition, newFootprint)
                        newFid.generationSoftware = GenerationSoftware.Eagle
                        self.botFiducialList.append(newFid)

                    else:
                        newComp = Component(botPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                            botPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                            newPosition, newFootprint)
                        newComp.generationSoftware = GenerationSoftware.Eagle
                        self.botComponentList.append(newComp)


            ### Top & Bot components - Fusion360
            if topPF.softwareCreated == GenerationSoftware.Fusion360:
                for x in range(len(topPF.entryList)):
                    newFootprint = Footprint(topPF.entryList[x][EagleHeader.Footprint.value].strip("\" "))
                    newPosition = Position(float(topPF.entryList[x][EagleHeader.X_Pos.value].strip(" ")),
                                           float(topPF.entryList[x][EagleHeader.Y_Pos.value].strip(" ")),
                                           float(topPF.entryList[x][EagleHeader.Rotation.value].strip(" ")),
                                           PCBSide.TOP)

                    if newFootprint.Value.lower().find("fid") != -1 or newFootprint.Value.lower().find("fiducial") != -1:
                        newFid = Fiducial(topPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                          topPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                          newPosition, newFootprint)
                        newFid.generationSoftware = GenerationSoftware.Fusion360
                        self.topFiducialList.append(newFid)

                    else:
                        newComp = Component(topPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                            topPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                            newPosition, newFootprint)
                        newComp.generationSoftware = GenerationSoftware.Fusion360
                        self.topComponentList.append(newComp)

            if botPF.softwareCreated == GenerationSoftware.Fusion360:
                for x in range(len(botPF.entryList)):
                    newFootprint = Footprint(botPF.entryList[x][EagleHeader.Footprint.value].strip("\" "))
                    newPosition = Position(float(botPF.entryList[x][EagleHeader.X_Pos.value].strip(" ")),
                                           float(botPF.entryList[x][EagleHeader.Y_Pos.value].strip(" ")),
                                           float(botPF.entryList[x][EagleHeader.Rotation.value].strip(" ")),
                                           PCBSide.BOT)

                    if newFootprint.Value.lower().find("fid") != -1 or newFootprint.Value.lower().find("fiducial") != -1:
                        newFid = Fiducial(botPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                          botPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                          newPosition, newFootprint)
                        newFid.generationSoftware = GenerationSoftware.Fusion360
                        self.botFiducialList.append(newFid)
                    else:
                        newComp = Component(botPF.entryList[x][EagleHeader.Name.value].strip("\" "),
                                            botPF.entryList[x][EagleHeader.Val.value].strip("\" "),
                                            newPosition, newFootprint)
                        newComp.generationSoftware = GenerationSoftware.Fusion360
                        self.botComponentList.append(newComp)










