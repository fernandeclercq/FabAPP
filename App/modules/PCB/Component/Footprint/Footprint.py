from App.modules.PCB.Definitions.Definitions import NeodenFootprints


class Footprint:
    def __init__(self, ori_val: str = ""):
        self.originalValue = ori_val
        self.transformedValue = "N/A"
        self.__correctFootprint()

    def __correctFootprint(self):
        for ft in NeodenFootprints.Footprints.value:
            if self.originalValue.find(ft) != -1:
                self.transformedValue = ft
                break


    def __repr__(self):
        return "Original value: {}, Transformed Value: {}".format(
            self.originalValue, self.transformedValue
        )


    def __str__(self):
        return "Original value: {}, Transformed Value: {}\n".format(
            self.originalValue, self.transformedValue
        )

