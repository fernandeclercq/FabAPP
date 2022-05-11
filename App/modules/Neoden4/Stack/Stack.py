#Feeder,    Feeder ID,  Type,   Nozzle, X,      Y,      Angle,  Footprint,  Value,      Pick height,    Pick delay, Placement height,   Placement delay,
#stack,     3,          0,      1,      411.36, 119.04, 90.00,  0805,       0805/1k,    1.50,           100,        1.00,               100,

#Vacuum detection,  Vacuum value,   Vision alignment,   Speed,  (Feeding rate), (Feed strength),    (peel strength),    (size correction),  (Skip)
#No,                -40,            1,                  60,     4,              50,                 80,                 No,                 No,
from App.modules.Neoden4.NeodenDefinitions import *


class Stack:
    def __init__(self, stack_name: NeodenDef = NeodenDef.NeodenStackHeader, feeder_id: int = 1, feeder_type: FeederType = FeederType.NormalFeeder,
                 nozzle: int = 1, x_pos: float = 411.36, y_pos: float = 119.04, pick_angle: int = 90, footprint: str = "0805", comp_value: str = "N/A",
                 pick_height: float = 1.50, pick_delay_ms: int = 100, placement_height: float = 1.00, placement_delay_ms: int = 100,
                 vacuum_detection: str = "No", vacuum_value: int = -50, vision_alignment: VisionAlignment = VisionAlignment.Individually,
                 speed: int = 60, feed_rate: int = 4, feed_strength: int = 50, peel_strength: int = 80, size_correction: str = "No", skip: str = "No"
                 ):
        self.stackName: NeodenDef = stack_name
        self.feederId: int = feeder_id
        self.feederType: FeederType = feeder_type
        self.nozzle: int = nozzle
        self.xPos: float = x_pos
        self.yPos: float = y_pos
        self.pickAngle: float = pick_angle
        self.footprint: str = footprint
        self.compValue: str = comp_value
        self.pickHeight: float = pick_height
        self.pickDelayMS: int = pick_delay_ms
        self.placementHeight: float = placement_height
        self.placementDelayMS: int = placement_delay_ms
        self.vacuumDetection: str = vacuum_detection
        self.vacuumValue: int = vacuum_value
        self.visionAlignment: VisionAlignment = vision_alignment
        self.speed: int = speed
        self.feedRate: int = feed_rate
        self.feedStrength: int = feed_strength
        self.peelStrength: int = peel_strength
        self.sizeCorrection: str = size_correction
        self.skip: str = skip


    def __str__(self):
        return "Name: {}, Feeder ID: {}, Feeder Type: {}, Nozzle: {}, X: {}, Y: {}, Pick Angle: {}, " \
               "Footprint: {}, Component Value: {}, Vision Alignment: {}".format(
                self.stackName, self.feederId, self.feederType.name, self.nozzle, self.xPos, self.yPos, self.pickAngle,
                self.footprint, self.compValue, self.visionAlignment.name
        )

    def __repr__(self):
        return "Name: {}, Feeder ID: {}, Feeder Type: {}, Nozzle: {}, X: {}, Y: {}, Pick Angle: {}, Footprint: {}, Component Value: {}, Vision Alignment: {}\n".format(
            self.stackName, self.feederId, self.feederType.name, self.nozzle, self.xPos, self.yPos, self.pickAngle, self.footprint, self.compValue, self.visionAlignment.name
        )




