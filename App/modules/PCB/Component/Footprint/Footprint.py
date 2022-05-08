class Footprint:
    def __init__(self, ori_val: str = "", val: str = ""):
        self.originalValue = ori_val
        self.value = val


    def __repr__(self):
        return "Original value: {}, Value: {}".format(
            self.originalValue, self.value
        )


    def __str__(self):
        return "Original value: {}, Value: {}".format(
            self.originalValue, self.value
        )

