from App.modules.PCB.Definitions.Definitions import GenerationSoftware



class Footprint:
    def __init__(self, ori_val: str = ""):
        self.Value = ori_val
        self.footprintGenSoft: GenerationSoftware = GenerationSoftware.NotDefined


    def __repr__(self):
        return "Value: {}".format(self.Value)


    def __str__(self):
        return "Value: {}\n".format(self.Value)

