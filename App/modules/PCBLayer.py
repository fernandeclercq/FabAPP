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

    def getFilePathRoot(self) -> str:
        if self.layerFilePath != "":
            if self.layerFilePath.find("/"):
                idx = self.layerFilePath.rfind("/")
                return self.layerFilePath[0:idx]
            elif self.layerFilePath.find("\\"):
                idx = self.layerFilePath.rfind("\\")
                return self.layerFilePath[0:idx]
            else:
                return ""


