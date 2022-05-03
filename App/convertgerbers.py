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

        self.ledGerberPath.setText(os.getcwd())

        self.btnImportGrbs.clicked.connect(self.evt_btnImportGerbers_clicked)
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
        event.accept()
        event.setDropAction(Qt.CopyAction)
        fileName = event.mimeData().urls()[0].fileName()
        self.myGerbersZipPath = event.mimeData().urls()[0].toLocalFile()

        self.gerbersAccepted(fileName)


        with zipfile.ZipFile(str(self.myGerbersZipPath), 'r') as myGerbers:
            myPCBLayers = myGerbers.namelist()
            print(myPCBLayers)



    def evt_btnRenameGerbers_clicked(self):
        pass

    def extractFilesToPath(self, gerbers: zipfile, pathToExtract: str) -> None:
        pass

    def evt_btnImportGerbers_clicked(self):
        self.myGerbersZipPath = QFileDialog.getOpenFileName(self, "Import Gerber Files",
                                                         self.myGerbersZipPath, "Zip file(*.zip)")[0]


        if self.myGerbersZipPath != "":
            gerberFileHeaders = self.getGerbersFileHeader(self.myGerbersZipPath)
            self.sortGerberFiles(gerberFileHeaders)
        #print(gerberAbsPaths)


        # #print(self.myGerbersPath)
        # with zipfile.ZipFile(str(self.myGerbersPath), 'r') as myGerbers:
        # #    print(myGerbers.namelist())
        #
        #     for file in myGerbers.namelist():
        #         lastSlashIndex =  file.rfind("/")
        #         if file[(lastSlashIndex + 1):] != "":
        #
        #             if file.endswith(".gbr"):
        #                 print(file)
        #                 with myGerbers.open(file, mode='r') as thefile:
        #                     lstStr = []
        #                     for x in range(0, 10):
        #                         temp = thefile.readline().decode('UTF-8')
        #                         if temp.find("G75*") == -1:
        #                             print(temp[:-2])
        #                         else:
        #                             break


    def sortGerberFiles(self, gerber_file_headers: list[list[str]]):

        for gerber_header in gerber_file_headers:
            print(gerber_header)
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

                print(self.drillLayer)
            else:
                gerberLayerFunction = ""
                gerberLayerGenSoft = ""
                gerberLayerCreationDate = ""
                for gerber_header_line in gerber_header:
                    if gerber_header_line.find("FileFunction") != -1:
                        idx = gerber_header_line.find("FileFunction")
                        gerberLayerFunction = gerber_header_line[idx + len("FileFunction") + 1:]
                    if gerber_header_line.find("GenerationSoftware") != -1:
                        idx = gerber_header_line.find("GenerationSoftware")
                        gerberLayerGenSoft = gerber_header_line[(idx + len("GenerationSoftware") + 1):].replace(',', ' ')
                    if gerber_header_line.find("CreationDate") != -1:
                        idx = gerber_header_line.find("CreationDate")
                        gerberLayerCreationDate = gerber_header_line[(idx + len("CreationDate") + 1):]

                print(gerberLayerFunction, gerberLayerGenSoft, gerberLayerCreationDate)



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
        self.ledGerberPath.setText(self.myGerbersPath)
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





