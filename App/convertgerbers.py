import os
import platform
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.convertGerbers_ui import *
import zipfile
from modules.PCBLayer import *

class ConvertGerbers(QDialog, Ui_ConvertGerbersDialog):
    def __init__(self):
        super(ConvertGerbers, self).__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setWindowIcon(QtGui.QIcon("img/AP_logo_256.png"))

        #self.ledExportGerberPath.setText(os.getcwd())
        self.ledExportGerberPath.setReadOnly(True)

        self.btnExportGerbers.clicked.connect(self.evt_btnExportGerbers_clicked)
        self.btnRenameGerbers.clicked.connect(self.evt_btnRenameGerbers_clicked)

        self.myGerbersZipPath = os.getcwd()
        self.myOutputDirectory = os.getcwd()

        #### Relevant PCB Layers
        self.topLayer = PCBLayer()
        self.bottomLayer = PCBLayer()
        self.boardOutlineLayer = PCBLayer()
        self.drillLayer = PCBLayer()

        self.areLayersSorted = False
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
        # Check if dropped file has the .zip extension
        if event.mimeData().urls()[0].fileName().endswith(".zip"):
            event.accept()
            # Set the Drop action to a Copy Action(icon to show)
            event.setDropAction(Qt.CopyAction)
            # Get the name of the file
            fileName = event.mimeData().urls()[0].fileName()
            # Get the zip file path
            self.myGerbersZipPath = event.mimeData().urls()[0].toLocalFile()
            # Reset all PCBLayers information
            self.resetPCBLayers()
            # Get gerber files names and headers
            gerberFileHeaders = self.getGerbersFileHeader(self.myGerbersZipPath)
            # Read files headers and assign gerber file paths to the correct layer
            self.areLayersSorted = self.sortGerberFiles(gerberFileHeaders)
            # If the sorting of these gerber is successful
            if self.areLayersSorted:
                # Show geber zip file name on the window
                self.gerbersAccepted(fileName)
                # Display changes to be made to the gerber files
                self.displayChangesToGerbers()

            else:
                # Else, display reason why these gerbers were not accepted
                self.gerbersRejected(fileName)

        else:
            event.ignore()



    def evt_btnRenameGerbers_clicked(self):
        if self.ledExportGerberPath.text() != "":
            self.extractFilesToPath(self.myGerbersZipPath, self.myOutputDirectory)


    def extractFilesToPath(self, gerbers_zip_path: str, path_to_extract: str) -> None:

        new_top_path = path_to_extract + self.getPlatformDirectorySlash() + self.topLayer.getFileName()[:-3] + "TOP"
        new_bot_path = path_to_extract + self.getPlatformDirectorySlash() + self.bottomLayer.getFileName()[:-3] + "BOT"
        new_drill_path = path_to_extract + self.getPlatformDirectorySlash() + self.drillLayer.getFileName()[:-3] + "DRD"
        new_boardOutline_path = path_to_extract + self.getPlatformDirectorySlash() + self.boardOutlineLayer.getFileName()[:-3] + "BOA"

        isAnyGerberExistent = self.isConvertedGerberExistent([new_top_path, new_bot_path, new_drill_path, new_boardOutline_path])

        isReplaceEnabled = False

        if isAnyGerberExistent:
            ans = QtWidgets.QMessageBox.question(self, "Replace files",
                                                 "It seems some of the files already exist.<br><br> <b>Do you want to replace them?</b>")
            if ans == QMessageBox.Yes:
                isReplaceEnabled = True
            else:
                isReplaceEnabled = False
                self.ledExportGerberPath.setText("")
                self.disableRenameButton()

        if self.ledExportGerberPath.text() != "":
            with zipfile.ZipFile(gerbers_zip_path, 'r') as myGerberZip:
                # Extract single gerber file from zip file to the specified directory
                old_top_path = myGerberZip.extract(self.topLayer.layerFilePath, path_to_extract)
                if isReplaceEnabled:
                    # Replace files with newly created files
                    os.replace(old_top_path, new_top_path)
                else:
                    # Rename newly extracted file to the extension for further use
                    os.rename(old_top_path, new_top_path)

                old_bot_path = myGerberZip.extract(self.bottomLayer.layerFilePath, path_to_extract)
                if isReplaceEnabled:
                    # Replace files with newly created files
                    os.replace(old_bot_path, new_bot_path)
                else:
                    os.rename(old_bot_path, new_bot_path)

                old_drill_path = myGerberZip.extract(self.drillLayer.layerFilePath, path_to_extract)
                if isReplaceEnabled:
                    os.replace(old_drill_path, new_drill_path)
                else:
                    os.rename(old_drill_path, new_drill_path)

                old_boardOutline_path = myGerberZip.extract(self.boardOutlineLayer.layerFilePath, path_to_extract)
                if isReplaceEnabled:
                    os.replace(old_boardOutline_path, new_boardOutline_path)
                else:
                    os.rename(old_boardOutline_path, new_boardOutline_path)

            QMessageBox.information(self, "Gerber Export", "Gerbers were exported successfully to:<br><br> <b>{}</b>".format(
                path_to_extract
            ))
            self.cleanWindowForNextUse()


    def evt_btnExportGerbers_clicked(self):
        tmp = QFileDialog.getExistingDirectory(self, "Select your output directory", self.myOutputDirectory)
        if str(tmp) != "":
            self.myOutputDirectory = tmp
            self.ledExportGerberPath.setText(self.myOutputDirectory)
            if self.areLayersSorted:
                self.enableRenameButton()
            else:
                self.disableRenameButton()
        else:
            self.ledExportGerberPath.setText(self.myOutputDirectory)


    def isConvertedGerberExistent(self, gerber_list: list[str]) -> bool:
        result = False

        for file in gerber_list:
            if os.path.isfile(file):
                result = True
                break

        return result

    def cleanWindowForNextUse(self):
        self.lblConvertGerbers.setStyleSheet("border: 4px dashed #aaa;")
        self.lblConvertGerbers.setText("<p>Drag and drop </p><p>compressed gerber files here</p>")
        self.lblConvertGerbersDisplayChanges.setText("No gerbers were imported yet....")
        self.ledExportGerberPath.setText("")
        self.disableRenameButton()


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

        if self.topLayer.layerFilePath != "N/A" and self.bottomLayer.layerFilePath != "N/A" and self.boardOutlineLayer.layerFilePath != "N/A":
            return True
        else:
            return False


    def getGerbersFileHeader(self, gerber_files: str) -> list[list[str]]:
        listBuffer = []
        # Open gerber files with "ZipFile"
        with zipfile.ZipFile(str(gerber_files), 'r') as myGerberFiles:
            # Iterate over all files found
            for gerberFileName in myGerberFiles.namelist():
                buffer = []
                # get the current file name and save it for later use
                currentFileName = self.getFileName(gerberFileName)
                # Check whether the current file ends in ".gbr", ".xln" or ".drl". If so, proceed
                if currentFileName.endswith(".gbr") or currentFileName.endswith(".xln") or currentFileName.endswith(".drl"):
                    #append gerber file name to the buffer
                    buffer.append(gerberFileName)
                    with myGerberFiles.open(gerberFileName, mode='r') as gerber:
                        # Read the 10 first lines of the gerber file
                        for x in range(0, 7):
                            # Read one line(BIN), convert it to 'UTF-8' and strip 'return' and 'newline' characters
                            temp = gerber.readline().decode('UTF-8').rstrip('\r\n').removesuffix('*%')
                            buffer.append(temp)
                    listBuffer.append(buffer)

        return listBuffer


    def gerbersAccepted(self, filename):
        if filename != "":
            self.lblConvertGerbers.setStyleSheet("QLabel { border: 4px dashed #00E200; }")
            self.lblConvertGerbers.setText(filename)
            if self.ledExportGerberPath.text() != "":
                self.enableRenameButton()


    def gerbersRejected(self, filename):
        self.lblConvertGerbers.setStyleSheet("QLabel { border: 4px dashed red; }")
        self.lblConvertGerbers.setText("Gerbers from {} are not X2 compatible".format(filename))
        self.lblConvertGerbersDisplayChanges.setText("<h2>Reason:</h2> <b>Gerbers do not contain the proper header for automatic conversion</b>")
        self.disableRenameButton()


    def enableRenameButton(self):
        self.btnRenameGerbers.setEnabled(True)


    def disableRenameButton(self):
        self.btnRenameGerbers.setEnabled(False)


    def resetPCBLayers(self):
        self.topLayer = PCBLayer()
        self.bottomLayer = PCBLayer()
        self.boardOutlineLayer = PCBLayer()
        self.drillLayer = PCBLayer()


    def displayChangesToGerbers(self):
        if self.areLayersSorted:
            changesToDisplay = """
                    <h2>The following changes will be applied:</h2>
                    <p>
                        {} Top layer: {}<b> -> will be changed to -> </b> {}<br><br>
                        {} Bottom layer: {}<b> ->will be changed to -> </b> {}<br><br>
                        {} Drills layer: {}<b> ->will be changed to -> </b> {}<br><br>
                        {} Board Outline layer: {}<b> ->will be changed to -> </b> {}
                    </p>
            """.format(
                self.topLayer.layerGenerationSoftware, self.topLayer.getFileName(), self.topLayer.getFileName()[:-3] + "TOP",
                self.bottomLayer.layerGenerationSoftware, self.bottomLayer.getFileName(), self.bottomLayer.getFileName()[:-3] + "BOT",
                self.drillLayer.layerGenerationSoftware, self.drillLayer.getFileName(), self.drillLayer.getFileName()[:-3] + "DRD",
                self.boardOutlineLayer.layerGenerationSoftware, self.boardOutlineLayer.getFileName(), self.boardOutlineLayer.getFileName()[:-3] + "BOA"
            )
            self.lblConvertGerbersDisplayChanges.setText(changesToDisplay)


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





