import enum



class NeodenFileIdentifiers(enum.Enum):
    ConfigFileIdentifier = "#Feeder,Feeder ID,Type,Nozzle,X,Y,Angle,Footprint,Value,Pick height,Pick delay," \
                           "Placement height,Placement delay,Vacuum detection,Vacuum value,Vision alignment,Speed,"

    ComponentSectionIdentifier = "#Chip,Feeder ID,Nozzle,Name,Value,Footprint,X,Y,Rotation,Skip"
    StackIdentifier = "stack"
    PCBSettingIdentifier = "pcb"
    PCBFiducialIdentifier = "mark"
    SingleFiducialIdentifier = "markext"
    PCBPanelIdentifier = "mirror_create"
    SinglePanelIdentifier = "mirror"
    ComponentIdentifier = "comp"


class LightSource(enum.IntEnum):
    Inner = 1
    Outer = 2


class StackName(enum.Enum):
    Stack = "stack"


class FeederType(enum.IntEnum):
    NormalFeeder = 0
    SpecialFeeder = 1


class VisionAlignment(enum.IntEnum):
    NoCorrection = 0
    Individually = 1
    Jointly = 2
    LargeComponent = 3


class StackConfig(enum.IntEnum):
    Stack = 0
    FeederId = 1
    FeederType = 2
    Nozzle = 3
    X = 4
    Y = 5
    Angle = 6
    Footprint = 7
    CompValue = 8
    PickHeight = 9
    PickDelay = 10
    PlacementHeight = 11
    PlacementDelay = 12
    VacuumDetection = 13
    VacuumValue = 14
    VisionAlignment = 15
    Speed = 16
    FeedRate = 17
    FeedStrength = 18
    PeelStrength = 19
    SizeCorrection = 20
    Skip = 21


class FirstChipMapping(enum.Enum):
    LineIdentifier = 0
    Columns = 1
    Rows = 2
    LeftBottomX = 3
    LeftBottomY = 4
    LeftTopX = 5
    LeftTopY = 6
    RightTopX = 7
    RightTopY = 8
    PcbAngle = 9


