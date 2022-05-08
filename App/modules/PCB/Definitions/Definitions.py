import enum



class PCBSide(enum.Enum):
    NotDefined = 0
    TOP = 1
    BOT = 2



class GenerationSoftware(enum.Enum):
    NotDefined = 0
    Eagle = 1
    Kicad = 2
    Fusion360 = 3



class PlacementHeader(enum.Enum):
    Ref = 0
    Value = 1
    Package = 2
    X = 3
    Y = 4
    Rotation = 5
    Side = 6
