
class Footprint:
    def __init__(self, ori_val: str = ""):
        self.Value = ori_val


    def __repr__(self):
        return "Original value: {}".format(self.Value)


    def __str__(self):
        return "Original value: {}\n".format(self.Value)

