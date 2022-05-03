import os
import platform

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.convertGerbers_ui import *
import zipfile
from modules.PCBLayer import *

class ConvertGerbers(QDialog, Ui_Dialog):
    def __init__(self):
        super(ConvertGerbers, self).__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.ledExportGerberPath.setText(os.getcwd())

        self.btnExportGerbers.clicked.connect(self.evt_btnExportGerbers_clicked)
        self.btnRenameGerbers.clicked.connect(self.evt_btnRenameGerbers_clicked)

        self.myGerbersZipPath = os.getcwd()

        #### Relevant PCB Layers
        self.topLayer = PCBLayer()
        self.bottomLayer = PCBLayer()
        self.boardOutlineLayer = PCBLayer()
        self.drillLayer = PCBLayer()


        self.btnRenameGerbers.setEnabled(False)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().urls()[0].fileName().endswith(".zip"):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        if event.mimeData().urls()[0].fileName().endswith(".zip"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().urls()[0].fileName().endswith(".zip"):
            event.accept()
            event.setDropAction(Qt.CopyAction)
            fileName = event.mimeData().urls()[0].fileName()
            self.myGerbersZipPath = event.mimeData().urls()[0].toLocalFile()

            self.gerbersAccepted(fileName)
            gerberFileHeaders = self.getGerbersFileHeader(self.myGerbersZipPath)
            areLayersSorted = self.sortGerberFiles(gerberFileHeaders)
            if areLayersSorted:
                print(self.bottomLayer, self.topLayer, sep="\n")

        else:
            event.ignore()




    def evt_btnRenameGerbers_clicked(self):
        pass

    def extractFilesToPath(self, gerbers: zipfile, pathToExtract: str) -> None:
        pass

    def evt_btnExportGerbers_clicked(self):
        self.myGerbersZipPath = QFileDialog.getOpenFileName(self, "Import Gerber Files",
                                                         self.myGerbersZipPath, "Zip file(*.zip)")[0]


        # if self.myGerbersZipPath != "":
        #     gerberFileHeaders = self.getGerbersFileHeader(self.myGerbersZipPath)
        #     areLayersSorted = self.sortGerberFiles(gerberFileHeaders)
        #     if areLayersSorted:
        #         pass



    def sortGerberFiles(self, gerber_file_headers: list[list[str]]) -> bool:

        for gerber_header in gerber_file_headers:
            gerberFilePath = gerber_header[0]

            #Drill file starts with command "M48" in its header
            if gerber_header[1].find("M48") != -1:
                self.drillLayer.layerFilePath = gerberFilePath
                self.drillLayer.layerType = "Drill"
                for gerber_header_line in gerber_header:
                    if gerber_header_line.find("GenerationSoftware") != -1:
                        idx = gerber_header_line.find("GenerationSoftware")
                        self.drillLayer.layerGenerationSoftware = gerber_header_line[(idx + len("GenerationSoftware") + 1):].replace(',', ' ')
                    if gerber_header_line.find("CreationDate") != -1:
                        idx = gerber_header_line.find("CreationDate")
                        self.drillLayer.layerCreationDate = gerber_header_line[(idx + len("CreationDate") + 1):]

            # All other layers
            else:
                gerberLayerFunction = ""
                gerberLayerGenSoft = ""
                gerberLayerCreationDate = ""
                for gerber_header_line in gerber_header:
                    if gerber_header_line.find("FileFunction") != -1:
                        idx = gerber_header_line.find("FileFunction")
                        gerberLayerFunction = gerber_header_line[idx + len("FileFunction") + 1:].split(',')
                    if gerber_header_line.find("GenerationSoftware") != -1:
                        idx = gerber_header_line.find("GenerationSoftware")
                        gerberLayerGenSoft = gerber_header_line[(idx + len("GenerationSoftware") + 1):].replace(',', ' ')
                    if gerber_header_line.find("CreationDate") != -1:
                        idx = gerber_header_line.find("CreationDate")
                        gerberLayerCreationDate = gerber_header_line[(idx + len("CreationDate") + 1):]

                if len(gerberLayerFunction) > 0:

                    if gerberLayerFunction[0] == "Profile":
                        self.boardOutlineLayer.layerFilePath = gerberFilePath
                        self.boardOutlineLayer.layerGenerationSoftware = gerberLayerGenSoft
                        self.boardOutlineLayer.layerCreationDate = gerberLayerCreationDate
                        self.boardOutlineLayer.layerType = "Board Outline"

                    elif gerberLayerGenSoft.lower().find("eagle") != -1:
                        if gerberLayerFunction[0] == "Copper":
                            if gerberLayerFunction[2] == "Bot":
                                self.bottomLayer.layerType = gerberLayerFunction[0]
                                self.bottomLayer.layerNumber = gerberLayerFunction[1]
                                self.bottomLayer.layerSide = gerberLayerFunction[2]
                                self.bottomLayer.layerSignalType = gerberLayerFunction[3]
                                self.bottomLayer.layerGenerationSoftware = gerberLayerGenSoft
                                self.bottomLayer.layerCreationDate = gerberLayerCreationDate
                                self.bottomLayer.layerFilePath = gerberFilePath
                            elif gerberLayerFunction[2] == "Top":
                                self.topLayer.layerType = gerberLayerFunction[0]
                                self.topLayer.layerNumber = gerberLayerFunction[1]
                                self.topLayer.layerSide = gerberLayerFunction[2]
                                self.topLayer.layerSignalType = gerberLayerFunction[3]
                                self.topLayer.layerGenerationSoftware = gerberLayerGenSoft
                                self.topLayer.layerCreationDate = gerberLayerCreationDate
                                self.topLayer.layerFilePath = gerberFilePath
                    elif gerberLayerGenSoft.lower().find("kicad") != -1:
                        if gerberLayerFunction[0] == "Copper":
                            print("copper layer kicad")
                            if gerberLayerFunction[2] == "Bot":
                                print("bot layer")
                                self.bottomLayer.layerType = gerberLayerFunction[0]
                                self.bottomLayer.layerNumber = gerberLayerFunction[1]
                                self.bottomLayer.layerSide = gerberLayerFunction[2]
                                self.bottomLayer.layerGenerationSoftware = gerberLayerGenSoft
                                self.bottomLayer.layerCreationDate = gerberLayerCreationDate
                                self.bottomLayer.layerFilePath = gerberFilePath
                            elif gerberLayerFunction[2] == "Top":
                                self.topLayer.layerType = gerberLayerFunction[0]
                                self.topLayer.layerNumber = gerberLayerFunction[1]
                                self.topLayer.layerSide = gerberLayerFunction[2]
                                self.topLayer.layerGenerationSoftware = gerberLayerGenSoft
                                self.topLayer.layerCreationDate = gerberLayerCreationDate
                                self.topLayer.layerFilePath = gerberFilePath

        if self.topLayer.layerFilePath != "" and self.bottomLayer.layerFilePath != "" and self.boardOutlineLayer.layerFilePath != "":
            return True
        else:
            return False


    def getGerbersFileHeader(self, gerber_files) -> list[list[str]]:
        listBuffer = []

        with zipfile.ZipFile(str(gerber_files), 'r') as myGerberFiles:
            for gerberFile in myGerberFiles.namelist():
                buffer = []
                currentFileName = self.getFileName(gerberFile)
                if currentFileName.endswith(".gbr") or currentFileName.endswith(".xln") or currentFileName.endswith(".drl"):
                    #listBuffer.append(os.getcwd() + self.getPlatformDirectorySlash() + gerberFile)
                    buffer.append(gerberFile)
                    with myGerberFiles.open(gerberFile, mode='r') as gerber:
                        # Read the 10 first lines of the gerber file
                        for x in range(0, 7):
                            # Read one line(BIN), convert it to 'UTF-8' and strip 'return' and 'newline' characters
                            temp = gerber.readline().decode('UTF-8').rstrip('\r\n').removesuffix('*%')
                            buffer.append(temp)
                    listBuffer.append(buffer)

        return listBuffer

    def gerbersAccepted(self, filename):
        #self.ledGerberPath.setText(self.myGerbersPath)
        self.lblConvertGerbers.setStyleSheet("QLabel { border: 4px dashed #00E200; }")
        self.lblConvertGerbers.setText(filename)
        self.btnRenameGerbers.setEnabled(True)

    def getFileName(self, gerber_file) -> str:
        if gerber_file != "":
            if gerber_file.find("/"):
                idx = gerber_file.rfind("/")
                return gerber_file[(idx+1):]
            elif gerber_file.find("\\"):
                idx = gerber_file.rfind("\\")
                return gerber_file[(idx+1):]
            else:
                return ""

    def getFilePathRoot(self, gerber_file) -> str:
        if gerber_file != "":
            if gerber_file.find("/"):
                idx = gerber_file.rfind("/")
                return gerber_file[0:idx]
            elif gerber_file.find("\\"):
                idx = gerber_file.rfind("\\")
                return gerber_file[0:idx]
            else:
                return ""

    def getPlatformDirectorySlash(self) -> str:
        system = platform.system()
        if system == "Windows":
            return "\\"
        elif system == "Darwin":
            return "/"
        elif system == "Linux":
            return "/"





