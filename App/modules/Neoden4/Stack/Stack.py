from App.modules.Neoden4.NeodenDefinitions import *


class Stack:
    def __init__(self, feeder_id: int = 1, feeder_type: FeederType = FeederType.NormalFeeder,
                 nozzle: int = 1, x_pos: float = 411.36, y_pos: float = 119.04, pick_angle: int = 90, footprint: str = "0805", comp_value: str = "N/A",
                 pick_height: float = 1.50, pick_delay_ms: int = 100, placement_height: float = 1.00, placement_delay_ms: int = 100,
                 vacuum_detection: str = "No", vacuum_value: int = -50, vision_alignment: VisionAlignment = VisionAlignment.Individually,
                 speed: int = 60, feed_rate: int = 4, feed_strength: int = 50, peel_strength: int = 80, size_correction: str = "No", skip: str = "No"
                 ):
        self.stackName: NeodenFileIdentifiers = NeodenFileIdentifiers.StackIdentifier.value
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
        return "Name: {}, Feeder ID: {}, Feeder Type: {}, Nozzle: {}, X: {}, Y: {}, Pick Angle: {}, Footprint: {}, " \
               "Component Value: {}, Vision Alignment: {}\n".format(
                self.stackName, self.feederId, self.feederType.name, self.nozzle, self.xPos, self.yPos, self.pickAngle,
                self.footprint, self.compValue, self.visionAlignment.name
                )


    def getAsLineString(self):
        return "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},".format(
            self.stackName, self.feederId, self.feederType.value, self.nozzle, self.xPos, self.yPos, self.pickAngle,
            self.footprint, self.compValue, self.pickHeight, self.pickDelayMS, self.placementHeight,
            self.placementDelayMS, self.vacuumDetection, self.vacuumValue, self.visionAlignment.value,
            self.speed, self.feedRate, self.feedStrength, self.peelStrength, self.sizeCorrection, self.skip
        )



