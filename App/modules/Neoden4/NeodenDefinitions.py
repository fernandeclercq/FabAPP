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


class NeodenFootprints(enum.Enum):

    AllFootprints = ["0402", "0603", "0805", "1206", "1210", "1812", "2225", "SOP8", "SOP14", "SOP16", "SOP18", "SOP20", "SOP24", "SOP28", "SOP30",
                  "SSOP16", "SSOP20", "SSOP24", "SSOP28", "TSOP16", "QFP44", "QFP54", "QFP64", "QFP80", "LQFP32", "LQFP44", "QFN24", "QFN32",
                  "TQFP100", "SOT223", "SOT-223", "SOT-223-3", "SOT23"
                  ]

    Nozzle_1_2_Footprints = [
        "0402", "0603", "0805", "SOT23", "SOD123"
    ]

    Nozzle_2_Footprints = [
        "0402", "0603", "0805", "SOT23", "SOD123"
    ]

    Nozzle_3_Footprints = [
        "LQFP32", "LQFP44", "QFN24", "QFN32", "TQFP100", "SSOP16", "SSOP20", "SSOP24",
        "SSOP28", "SOP16", "SOP18", "SOP20", "SOP24", "SOP28", "SOP30", "5050"
    ]

    Nozzle_4_Footprints = [
        "SOP8", "SOP14", "1206", "1210", "1812", "2225", "SOT223", "SOT-223", "SOT-223-3"
    ]




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



class PCBOrigin(enum.Enum):
    X = 78.76
    Y = 24.31




