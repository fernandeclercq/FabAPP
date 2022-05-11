from App.modules.Neoden4.Stack.Stack import Stack
from App.modules.PCB.Fiducial.Fiducial import Fiducial
from App.modules.Neoden4.FirstChip.FirstChipSetting import FirstChipSetting
from App.modules.Neoden4.NeodenDefinitions import *


class NeodenFile(Stack):
    def __init__(self, config_path: str):
        super().__init__()
        self.configPath: str = config_path
        self.stackList: list[Stack] = []
        self.panelSetting: str = "pcb,Manual,Lock,100,100,350,150,Front,10,10,0,"
        self.pcbTesting: str = "test,No"
        self.pcbPanelFirstChipSetting: FirstChipSetting = FirstChipSetting()
        self.fiducialList: list[Fiducial] = []



        self.__populateNeodenStackList()
        self.__populateNeodenFirstChipSetting()





    def __populateNeodenFirstChipSetting(self):
        if self.configPath.endswith(".csv"):
            with open(self.configPath, mode='r') as config:
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
                header = config.readline().strip('\n')
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

