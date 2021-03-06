from App.modules.Neoden4.Stack.Stack import Stack
from App.modules.Neoden4.Component.NeodenComponent import *
from App.modules.Neoden4.Fiducial.NeodenFiducial import NeodenFiducial, Fiducial
from App.modules.Neoden4.FirstChip.FirstChipSetting import FirstChipSetting
from App.modules.Neoden4.Panel.Panel import Panel
from App.modules.Neoden4.NeodenDefinitions import *
from App.modules.PCB.Definitions.Definitions import PCBSide
import copy


class NeodenFile(Stack, NeodenFiducial, NeodenComponent, Panel):
    def __init__(self, config_path: str):
        super().__init__()
        self.configPath: str = config_path
        self.stackList: list[Stack] = []
        self.panelSetting: str = "pcb,Manual,Lock,100,100,350,150,Front,10,10,0,"
        self.pcbTesting: str = "test,No"
        self.pcbPanelFirstChipSetting: FirstChipSetting = FirstChipSetting()
        self.topPcbSinglePanel: Panel = Panel()
        self.botPcbSinglePanel: Panel = Panel()
        self._topStackList: list[Stack] = []
        self._botStackList: list[Stack] = []
        self._topFiducialList: list[NeodenFiducial] = []
        self._botFiducialList: list[NeodenFiducial] = []
        self._topComponentList: list[NeodenComponent] = []
        self._botComponentList: list[NeodenComponent] = []
        self.xOrigin: float = 0.00
        self.yOrigin: float = 0.00
        self.prevNozzle = -1
        self.prevFootprint = "N/A"


        self.__populateNeodenStackList()
        self.__populateNeodenFirstChipSetting()
        self.__populateXYOrigin()


    @property
    def topStackList(self):
        return self._topStackList

    @property
    def botStackList(self):
        return self._botStackList


    def clearComponentList(self):
        self._topFiducialList.clear()
        self._botFiducialList.clear()
        self._botComponentList.clear()
        self._topComponentList.clear()
        self._topStackList.clear()
        self._botStackList.clear()


    @property
    def botComponentList(self):
        return self._botComponentList


    @botComponentList.setter
    def botComponentList(self, pcb_comp_list: list[Component]):
        for pcb_comp in pcb_comp_list:
            # copy.deepcopy() makes a copy of each object inside "pcb_comp"
            # Deepcopy is necessary to decouple the references between pcb.component and neoden.component
            newNeodenComp = NeodenComponent(copy.deepcopy(pcb_comp))
            newNeodenComp.component.position = self.__botCorrectPosition(newNeodenComp.component.position)
            newNeodenComp.component.footprint = self.__correctFootprint(newNeodenComp.component.footprint)
            [newNeodenComp.nozzle, newNeodenComp.isNozzleAssigned] = self.__assignNozzle(newNeodenComp.component)
            [newNeodenComp.feederId, newNeodenComp.isFeederConfigFound] = self.__assignFeederId(newNeodenComp.component)
            self._botComponentList.append(newNeodenComp)

        if len(self._botComponentList) > 0:
            self.botPcbSinglePanel.firstCompX = float(self._botComponentList[0].component.position.xPos)
            self.botPcbSinglePanel.firstCompY = float(self._botComponentList[0].component.position.yPos)

    @property
    def topComponentList(self):
        return self._topComponentList


    @topComponentList.setter
    def topComponentList(self, pcb_comp_list: list[Component]):
        for pcb_comp in pcb_comp_list:
            newNeodenComp = NeodenComponent(copy.deepcopy(pcb_comp))
            newNeodenComp.component.position = self.__topCorrectPosition(newNeodenComp.component.position)
            newNeodenComp.component.footprint = self.__correctFootprint(newNeodenComp.component.footprint)
            [newNeodenComp.nozzle, newNeodenComp.isNozzleAssigned] = self.__assignNozzle(newNeodenComp.component)
            [newNeodenComp.feederId, newNeodenComp.isFeederConfigFound] = self.__assignFeederId(newNeodenComp.component)
            self._topComponentList.append(newNeodenComp)

        if len(self._topComponentList) > 0:
            self.topPcbSinglePanel.firstCompX = float(self._topComponentList[0].component.position.xPos)
            self.topPcbSinglePanel.firstCompY = float(self._topComponentList[0].component.position.yPos)


    def __topCorrectPosition(self, original_position: Position) -> Position:
        newPos = Position()
        if original_position.rotation > 180:
            newPos.rotation = round((original_position.rotation - 360), 2)
        else:
            newPos.rotation = original_position.rotation
        newPos.xPos = round((original_position.xPos + self.xOrigin), 2)
        newPos.yPos = round((original_position.yPos + self.yOrigin), 2)
        newPos.pcbSide = original_position.pcbSide

        return newPos


    def __botCorrectPosition(self, original_position: Position) -> Position:
        newPos = Position()
        if original_position.rotation > 180:
            newPos.rotation = round((original_position.rotation - 360), 2)
        else:
            newPos.rotation = original_position.rotation

        if original_position.positionGenSoft == GenerationSoftware.Kicad:
            newPos.xPos = round(((original_position.yPos + self.xOrigin) + 0.22), 2)
            newPos.yPos = round(((abs(original_position.xPos) + self.yOrigin) - 0.31), 2)
        else:
            newPos.xPos = round(((original_position.yPos + self.xOrigin) + 0.22), 2)
            newPos.yPos = round(((original_position.xPos + self.yOrigin) - 0.31), 2)

        newPos.pcbSide = original_position.pcbSide

        return newPos


    def __correctFootprint(self, original_footprint: Footprint) -> Footprint:
        newFootprint = Footprint()
        foundFootprintInStack = False
        for stack in self.stackList:
            if original_footprint.Value.lower().find(stack.footprint.lower()) != -1:
                newFootprint.Value = stack.footprint
                foundFootprintInStack = True
                break

        if not foundFootprintInStack:
            for footprint in NeodenFootprints.AllFootprints.value:
                if original_footprint.Value.lower().find(str(footprint).lower()) != -1:
                    newFootprint.Value = str(footprint)
                    break

        return newFootprint

    def __assignNozzle(self, comp: Component) -> [int, bool]:
        newNozzle = 1
        isNozzleFound: bool = False

        for stack in self.stackList:
            if stack.compValue == (comp.footprint.Value + "/" + comp.Value):
                newNozzle = stack.nozzle
                isNozzleFound = True

                if comp.position.pcbSide == PCBSide.BOT:
                    if len(self._botStackList) > 0:
                        found = stack in self._botStackList
                        if not found:
                            self._botStackList.append(stack)
                    else:
                        self._botStackList.append(stack)


                else:
                    if len(self._topStackList) > 0:
                        found = stack in self._topStackList
                        if not found:
                            self._topStackList.append(stack)
                    else:
                        self._topStackList.append(stack)

                break


        if self.prevNozzle == -1 and self.prevFootprint == "N/A":
            if comp.footprint.Value in NeodenFootprints.Nozzle_1_2_Footprints.value:
                self.prevNozzle = newNozzle
                self.prevFootprint = comp.footprint.Value
                isNozzleFound = True
            elif comp.footprint.Value in NeodenFootprints.Nozzle_3_Footprints.value:
                newNozzle = 3
                isNozzleFound = True

            elif comp.footprint.Value in NeodenFootprints.Nozzle_4_Footprints.value:
                newNozzle = 4
                isNozzleFound = True
        else:
            if comp.footprint.Value in NeodenFootprints.Nozzle_1_2_Footprints.value:
                self.prevFootprint = comp.footprint.Value
                if self.prevNozzle == 1:
                    newNozzle = 2
                    self.prevNozzle = 2
                    isNozzleFound = True
                else:
                    newNozzle = 1
                    self.prevNozzle = 1
                    isNozzleFound = True

            elif comp.footprint.Value in NeodenFootprints.Nozzle_3_Footprints.value:
                newNozzle = 3
                isNozzleFound = True

            elif comp.footprint.Value in NeodenFootprints.Nozzle_4_Footprints.value:
                newNozzle = 4
                isNozzleFound = True

        return [newNozzle, isNozzleFound]

    def __assignFeederId(self, comp: Component) -> [int, bool]:
        newFeederId: int = 1

        for stack in self.stackList:
            if stack.compValue == (comp.footprint.Value + "/" + comp.Value):
                newFeederId = stack.feederId
                return [newFeederId, True]

        return [newFeederId, False]


    @property
    def botFiducialList(self):
        return self._botFiducialList

    @botFiducialList.setter
    def botFiducialList(self, pcb_fid_list: list[Fiducial]):
        fidNr = 0
        for pcb_fid in pcb_fid_list:
            newNeoFid = NeodenFiducial(copy.deepcopy(pcb_fid))
            newNeoFid.fiducialNumber = fidNr
            newNeoFid.fiducial.position = self.__botCorrectPosition(newNeoFid.fiducial.position)
            self._botFiducialList.append(newNeoFid)
            fidNr += 1


    @property
    def topFiducialList(self):
        return self._topFiducialList


    @topFiducialList.setter
    def topFiducialList(self, pcb_fid_list: list[Fiducial]):
        fidNr = 0
        for pcb_fid in pcb_fid_list:
            newNeoFid = NeodenFiducial(copy.deepcopy(pcb_fid))
            newNeoFid.fiducialNumber = fidNr
            newNeoFid.fiducial.position = self.__topCorrectPosition(newNeoFid.fiducial.position)
            self._topFiducialList.append(newNeoFid)
            fidNr += 1


    def __populateXYOrigin(self):
        self.xOrigin = self.pcbPanelFirstChipSetting.leftBottomX
        self.yOrigin = self.pcbPanelFirstChipSetting.leftBottomY



    def __populateNeodenFirstChipSetting(self):
        if self.configPath.endswith(".csv"):
            with open(self.configPath, mode='r') as config:
                header: str = config.readline().strip('\n')
                if header == str(NeodenFileIdentifiers.ConfigFileIdentifier.value):
                    FirstChipSettingFound = False
                    while not FirstChipSettingFound:
                        fileEntry = config.readline()
                        if fileEntry != "":
                            fileEntry = fileEntry.split(',')
                            if fileEntry[0] == "mirror_create":
                                self.pcbPanelFirstChipSetting.leftBottomX = round(float(fileEntry[FirstChipMapping.
                                                                                        LeftBottomX.value]), 2)
                                self.pcbPanelFirstChipSetting.leftBottomY = round(float(fileEntry[FirstChipMapping.
                                                                                        LeftBottomY.value]), 2)
                                FirstChipSettingFound = True
                                break


    def __populateNeodenStackList(self):
        if self.configPath.endswith(".csv"):
            with open(self.configPath, mode='r') as config:
                header: str = config.readline().strip('\n')
                if header == str(NeodenFileIdentifiers.ConfigFileIdentifier.value):
                    isLastLine = False
                    while not isLastLine:
                        lst = config.readline().strip('\n')
                        if lst != "":
                            lst = lst.split(',')
                            if lst[0].lower() == "stack":
                                newStack = Stack()
                                newStack.stackName = lst[StackConfig.Stack.value]
                                newStack.feederId = lst[StackConfig.FeederId.value]
                                newStack.feederType = FeederType(int(lst[StackConfig.FeederType.value]))
                                newStack.nozzle = lst[StackConfig.Nozzle.value]
                                newStack.xPos = lst[StackConfig.X.value]
                                newStack.yPos = lst[StackConfig.Y.value]
                                newStack.pickAngle = lst[StackConfig.Angle.value]
                                newStack.footprint = lst[StackConfig.Footprint.value]
                                newStack.compValue = lst[StackConfig.CompValue.value]
                                newStack.pickHeight = lst[StackConfig.PickHeight.value]
                                newStack.pickDelayMS = lst[StackConfig.PickDelay.value]
                                newStack.placementHeight = lst[StackConfig.PlacementHeight.value]
                                newStack.placementDelayMS = lst[StackConfig.PlacementDelay.value]
                                newStack.vacuumDetection = lst[StackConfig.VacuumDetection.value]
                                newStack.vacuumValue = lst[StackConfig.VacuumValue.value]
                                newStack.visionAlignment = VisionAlignment(int(lst[StackConfig.VisionAlignment.value]))
                                newStack.speed = lst[StackConfig.Speed.value]
                                newStack.feedRate = lst[StackConfig.FeedRate.value]
                                newStack.feedStrength = lst[StackConfig.FeedStrength.value]
                                newStack.peelStrength = lst[StackConfig.PeelStrength.value]
                                newStack.sizeCorrection = lst[StackConfig.SizeCorrection.value]
                                newStack.skip = lst[StackConfig.Skip.value]

                                if newStack.feederType == FeederType.NormalFeeder:
                                    self.stackList.append(newStack)

                            else:
                                isLastLine = True
                                break
                        else:
                            isLastLine = True
                            break


    def getTopPCBFiducialSettingAsStringLine(self):
        tmpStr: str = "" + str(NeodenFileIdentifiers.PCBFiducialIdentifier.value) + ",Whole,Auto,"
        for pcb_fid in self._topFiducialList:
            tmpStr += "{},{},".format(pcb_fid.fiducial.position.xPos, pcb_fid.fiducial.position.yPos)

        return tmpStr

    def getBotPCBFiducialSettingAsStringLine(self):
        tmpStr: str = "" + str(NeodenFileIdentifiers.PCBFiducialIdentifier.value) + ",Whole,Auto,"
        for pcb_fid in self._botFiducialList:
            tmpStr += "{},{},".format(pcb_fid.fiducial.position.xPos, pcb_fid.fiducial.position.yPos)

        return tmpStr

    def getCompByRefName(self, ref_name: str) -> NeodenComponent:
        result = NeodenComponent(Component())
        compFound: bool = False

        for topCmp in self.topComponentList:
            if topCmp.component.refName == ref_name:
                result = topCmp
                compFound = True
                break

        if not compFound:
            for botCmp in self.botComponentList:
                if botCmp.component.refName == ref_name:
                    result = botCmp
                    compFound = True
                    break

        return result
