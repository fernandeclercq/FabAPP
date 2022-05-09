class Footprint:
    def __init__(self, ori_val: str = ""):
        self.originalValue = ori_val
        self.transformedValue = "N/A"


    def __repr__(self):
        return "Original value: {}, Transformed Value: {}".format(
            self.originalValue, self.transformedValue
        )


    def __str__(self):
        return "Original value: {}, Transformed Value: {}\n".format(
            self.originalValue, self.transformedValue
        )

