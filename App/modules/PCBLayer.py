
class PCBLayer:
    def __init__(self, layer_file_path: str = "N/A", layer_type: str = "N/A", layer_side: str = "N/A",
                 layer_number: str = "N/A", layer_signal_type: str = "N/A", layer_polarity: str = "N/A",
                 layer_generation_software: str = "N/A", layer_creation_date: str = "N/A"):
        super(PCBLayer, self).__init__()

        self.layerFilePath = layer_file_path
        self.layerType = layer_type
        self.layerSide = layer_side
        self.layerNumber = layer_number
        self.layerSignalType = layer_signal_type
        self.layerPolarity = layer_polarity
        self.layerGenerationSoftware = layer_generation_software
        self.layerCreationDate = layer_creation_date


    def __str__(self):
        return "Layer Generation Software: {}, Layer name: {}, Layer type: {}, Side: {}, Layer filepath: {}".format(
            self.layerGenerationSoftware, self.getFileName(), self.layerType, self.layerSide, self.layerFilePath)

    def __repr__(self):
        return "Layer Generation Software: {}, Layer name: {}, Layer type: {}, Side: {}, Layer filepath: {}\n".format(
            self.layerGenerationSoftware, self.getFileName(), self.layerType, self.layerSide, self.layerFilePath)

    def getFileName(self) -> str:
        if self.layerFilePath != "":
            if self.layerFilePath.find("/"):
                idx = self.layerFilePath.rfind("/")
                return self.layerFilePath[(idx+1):]
            elif self.layerFilePath.find("\\"):
                idx = self.layerFilePath.rfind("\\")
                return self.layerFilePath[(idx+1):]
            else:
                return ""

    def getFileSeparatorChar(self) -> str:
        if self.layerFilePath != "":
            if self.layerFilePath.find("/"):
                return "/"
            elif self.layerFilePath.find("\\"):
                return "\\"
            else:
                return "/"

    def getPathToFile(self) -> str:
        if self.layerFilePath != "":
            if self.layerFilePath.find("/"):
                idx = self.layerFilePath.rfind("/")
                if idx != -1:
                    return self.layerFilePath[0:idx]
                else:
                    return self.layerFilePath
            elif self.layerFilePath.find("\\"):
                idx = self.layerFilePath.rfind("\\")
                if idx != -1:
                    return self.layerFilePath[0:idx]
                else:
                    return self.layerFilePath
            else:
                return ""

    def getFileRootPath(self) -> str:

        result = ""

        if self.layerFilePath != "":
            tmp_str = self.getPathToFile()
            idx = tmp_str.find(self.getFileSeparatorChar())
            if idx != -1:
                result = tmp_str[:idx]
            else:
                if tmp_str.find('.') != -1:
                    result = ""
                else:
                    result = tmp_str
        else:
            result = ""

        return result

