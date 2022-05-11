import enum


class NeodenDef(enum.Enum):
    NeodenStackHeader = "#Feeder,Feeder ID,Type,Nozzle,X,Y,Angle,Footprint,Value,Pick height,Pick delay,Placement height,Placement delay," \
                        "Vacuum detection,Vacuum value,Vision alignment,Speed,\n"

    NeodenStackPrefix = "stack"
    NeodenCompPrefix = "comp"


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


#Feeder,    Feeder ID,  Type,   Nozzle, X,      Y,      Angle,  Footprint,  Value,      Pick height,    Pick delay, Placement height,   Placement delay,
#stack,     3,          0,      1,      411.36, 119.04, 90.00,  0805,       0805/1k,    1.50,           100,        1.00,               100,

#Vacuum detection,  Vacuum value,   Vision alignment,   Speed,  (Feeding rate), (Feed strength),    (peel strength),    (size correction),  (Skip)
#No,                -40,            1,                  60,     4,              50,                 80,                 No,                 No,


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
