#     #Feeder,Feeder ID,Type,Nozzle,X,Y,Angle,Footprint,Value,Pick height,Pick delay,Placement height,Placement delay,Vacuum detection,Vacuum value,Vision alignment,Speed,

#     stack,6,0,1,411.07,158.43,90.00,0805,0805/10k,1.50,100,1.00,100,No,-40,1,60,8,50,80,No,No,
#     stack,12,0,1,411.04,303.79,90.00,0805,0805/22pF,0.50,100,1.00,100,No,-40,1,60,4,50,80,No,No,
#     stack,13,0,1,411.50,325.34,90.00,0805,0805/LED1,2.00,100,1.50,100,No,-40,1,60,4,50,80,No,No,
from App.modules.Neoden4.Stack.Stack import Stack, StackConfig, FeederType, VisionAlignment


class NeodenFile(Stack):
    def __init__(self, config_path: str):
        super().__init__()
        self.configPath: str = config_path
        self.stackList: list[Stack] = []
        self.__populateNeodenStackList()


    def __populateNeodenStackList(self):
        print(self.configPath)
        if self.configPath.endswith(".csv"):
            with open(self.configPath, mode='r') as config:
                header = config.readline().strip('\n')
                print(header)
                isLastLine = False
                while not isLastLine:
                    lst = config.readline().strip('\n')
                    if lst != "":
                        lst = lst.split(',')
                        if lst[0].lower() == "stack":
                            print(lst)
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

        print(self.stackList)

