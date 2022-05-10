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



class NeodenHeader(enum.Enum):
    Feeder = 0
    Nozzle = 1
    Name = 2
    Val = 3
    Footprint = 4
    X_Pos = 5
    Y_Pos = 6
    Rotation = 7
    Skip = 8


class NeodenOfsset(enum.Enum):
    X_Offset = 64.93
    Y_Offset = 9.72


class NeodenFootprints(enum.Enum):
    Footprints = ["0402", "0603", "0805", "1206", "1210", "1812", "2225", "SOP8", "SOP14", "SOP16", "SOP18", "SOP20", "SOP24", "SOP28", "SOP30",
                  "SSOP16", "SSOP20", "SSOP24", "SSOP28", "TSOP16", "QFP44", "QFP54", "QFP64", "QFP80", "LQFP32", "LQFP44", "QFN24", "QFN32",
                  "TQFP100", "SOT223", "SOT-223"
                  ]


class KicadHeader(enum.Enum):
    Name = 0
    Val = 1
    Footprint = 2
    X_Pos = 3
    Y_Pos = 4
    Rotation = 5
    Side = 6



class EagleHeader(enum.Enum):
    Name = 0
    X_Pos = 1
    Y_Pos = 2
    Rotation = 3
    Val = 4
    Footprint = 5