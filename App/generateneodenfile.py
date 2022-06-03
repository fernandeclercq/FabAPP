from PyQt5.QtWidgets import *
from App.ui.generateNeodenFile_ui import *
from App.modules.PCB.PCB import *
from App.modules.Neoden4.NeodenDefinitions import *
from App.modules.Neoden4.NeodenFile import *
import os
import copy
import platform
from PyQt5.QtCore import *
import zipfile


class GenerateNeodenFile(QDialog, Ui_GenerateNeodenConfigDialog):
    def __init__(self):
        super(GenerateNeodenFile, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("img/AP_logo_256.png"))
        self.setAcceptDrops(True)

        self.neodenStackConfigPath = self.getConfigFilePath()
        self.neodenFile = NeodenFile(self.neodenStackConfigPath)

        self.ledFilesOutputDirectory.setReadOnly(True)
        self.ledImportPositionFilePath.setReadOnly(True)

        self.btnImportPositionFile.clicked.connect(self.evt_btnImportPosFile_clicked)
        self.btnRemovePositionFile.clicked.connect(self.evt_btnRemovePosFile_clicked)
        self.btnRemovePositionFile.setEnabled(False)

        self.btnOutputFolderDirectory.clicked.connect(self.evt_btnOutputFolderDirectory_clicked)
        self.btnGenerateNeodenConfig.clicked.connect(self.evt_btnGenerateNeodenConfig_clicked)
        self.btnGenerateNeodenConfig.setEnabled(False)

        self.inPosFilePath = os.getcwd()
        self.outNeodenConfigFilePath = os.getcwd()


        self.pcb = PCB()

        self.prevNozzle = 0
        self.prevFootprint = ""



    def getConfigFilePath(self, path: str = "config") -> str:
        platformName = platform.system()
        prefix = "./" + path + "/"
        finalPath: str = ""

        if platformName.lower() == "darwin":
            tmp = os.path.dirname(path)[:-3]
            return tmp
        else:
            filesLst = os.listdir("./" + path)
            for file in filesLst:
                if file.lower().find("config") != -1:
                    if file.lower().endswith(".csv"):
                        return prefix + str(file)




    def evt_btnImportPosFile_clicked(self):
        # noinspection PyArgumentList
        inPath: str = QFileDialog.getOpenFileName(self, "Import Position File as Zip", self.inPosFilePath, "Zip file(*.zip);; CSV File (*.csv)")[0]
        if len(self.pcb.topComponentList) > 0 or len(self.pcb.botComponentList) > 0:
            self.clearComponentTables()

        if inPath != "":
            self.btnRemovePositionFile.setEnabled(True)
            self.ledImportPositionFilePath.setText(inPath)

            self.pcb.path = inPath

            if zipfile.is_zipfile(inPath):
                self.pcb.processPlacementFileFromZip()

            else:
                if inPath.endswith(".csv"):
                    self.pcb.processPlacementFileFromFile(inPath)

            # Populate fiducials & component lists for further process
            self.neodenFile.topFiducialList = self.pcb.topFiducialList
            self.neodenFile.botFiducialList = self.pcb.botFiducialList
            self.neodenFile.topComponentList = self.pcb.topComponentList
            self.neodenFile.botComponentList = self.pcb.botComponentList

            # Populate top & bottom component tables
            self.populateTopComponentTable()
            self.populateBotComponentTable()

            # If the top or bottom comp table contains data, enable the "export" button
            if self.tableTopComponents.rowCount() > 0 or self.tableBottomComponents.rowCount() > 0:
                self.btnGenerateNeodenConfig.setEnabled(True)



    def populateTopComponentTable(self):
        if len(self.neodenFile.topComponentList) > 0:
            self.tableTopComponents.setRowCount(len(self.neodenFile.topComponentList))

            for row in range(0, len(self.pcb.topComponentList)):
                # Feeder number (1 - 48)
                self.tableTopComponents.setCellWidget(row, 0, self.createFeederCmb(self.neodenFile.topComponentList[row]))
                # Nozzle Number (1 - 4)
                self.tableTopComponents.setCellWidget(row, 1, self.createNozzleCmb(self.neodenFile.topComponentList[row].nozzle))
                # Comp Name
                self.tableTopComponents.setItem(row, 2, QTableWidgetItem(self.neodenFile.topComponentList[row].component.refName))
                self.tableTopComponents.itemAt(row, 2)
                # Component Value
                self.tableTopComponents.setItem(row, 3, QTableWidgetItem(self.neodenFile.topComponentList[row].component.Value))
                # Component Footprint
                self.tableTopComponents.setItem(row, 4, QTableWidgetItem(self.neodenFile.topComponentList[row].component.footprint.Value))
                # Component X pos
                self.tableTopComponents.setItem(row, 5, QTableWidgetItem(str(self.neodenFile.topComponentList[row].component.position.xPos)))
                # Component Y pos
                self.tableTopComponents.setItem(row, 6, QTableWidgetItem(str(self.neodenFile.topComponentList[row].component.position.yPos)))
                # Component Rotation
                self.tableTopComponents.setItem(row, 7, QTableWidgetItem(str(self.neodenFile.topComponentList[row].component.position.rotation)))
                # Component Skip
                self.tableTopComponents.setCellWidget(row, 8, self.createSkipCmb(self.neodenFile.topComponentList[row].skip))


    def populateBotComponentTable(self):
        if len(self.neodenFile.botComponentList) > 0:
            self.tableBottomComponents.setRowCount(len(self.neodenFile.botComponentList))

            for row in range(0, len(self.neodenFile.botComponentList)):
                # Feeder number (1 - 48)
                self.tableBottomComponents.setCellWidget(row, 0, self.createFeederCmb(self.neodenFile.botComponentList[row]))
                # Nozzle Number (1 - 4)
                self.tableBottomComponents.setCellWidget(row, 1, self.createNozzleCmb(self.neodenFile.botComponentList[row].nozzle))
                # Comp Name
                self.tableBottomComponents.setItem(row, 2, QTableWidgetItem(self.neodenFile.botComponentList[row].component.refName))
                # Component Value
                self.tableBottomComponents.setItem(row, 3, QTableWidgetItem(self.neodenFile.botComponentList[row].component.Value))
                # Component Footprint
                self.tableBottomComponents.setItem(row, 4, QTableWidgetItem(self.neodenFile.botComponentList[row].component.footprint.Value))
                # Component X pos
                self.tableBottomComponents.setItem(row, 5, QTableWidgetItem(str(self.neodenFile.botComponentList[row].component.position.xPos)))
                # Component Y pos
                self.tableBottomComponents.setItem(row, 6, QTableWidgetItem(str(self.neodenFile.botComponentList[row].component.position.yPos)))
                # Component Rotation
                self.tableBottomComponents.setItem(row, 7, QTableWidgetItem(str(self.neodenFile.botComponentList[row].component.position.rotation)))
                # Component Skip
                self.tableBottomComponents.setCellWidget(row, 8, self.createSkipCmb(self.neodenFile.botComponentList[row].skip))


    def cleanComponentTables(self):
        topRowCount = self.tableTopComponents.rowCount()
        botRowCount = self.tableBottomComponents.rowCount()

        for row in range(topRowCount, -1, -1):
            self.tableTopComponents.removeRow(row)

        for row in range(botRowCount, -1, -1):
            self.tableBottomComponents.removeRow(row)



    def createFeederCmb(self, component: NeodenComponent) -> QComboBox:
        cmb = QComboBox()
        start = 1
        end = 49
        myFeederIds = []
        for i in range(start, end):
            myFeederIds.append(str(i))

        cmb.addItems(myFeederIds)

        cmb.setCurrentIndex(int(component.feederId) - 1)

        cmb.setProperty("comp_name", component.component.refName)

        if component.feederConfigFound:
            cmb.setEnabled(False)
        else:
            cmb.currentIndexChanged.connect(self.evt_feederCmb_currentIndexChanged)

        return cmb


    def evt_feederCmb_currentIndexChanged(self, idx):
        print(idx)

        cmb: QComboBox = self.sender()
        print(cmb.property("comp_name"))



    def createNozzleCmb(self, nozzle: int) -> QComboBox:
        newCmb = QComboBox()

        start = 1
        end = 5
        myNozzles = []
        for i in range(start, end):
            myNozzles.append(str(i))

        newCmb.addItems(myNozzles)
        newCmb.setCurrentIndex(int(nozzle) - 1)
        return newCmb

    def createSkipCmb(self, skip: str) -> QComboBox:
        newCmb = QComboBox()
        newCmb.addItems(["No", "Yes"])
        if skip.lower() == "no":
            newCmb.setCurrentIndex(0)
        else:
            newCmb.setCurrentIndex(1)

        return newCmb


    def evt_btnRemovePosFile_clicked(self):
        if self.ledImportPositionFilePath.text() != "":
            self.ledImportPositionFilePath.setText("")
            self.ledFilesOutputDirectory.setText("")
            self.clearComponentTables()
            self.inPosFilePath = os.getcwd()
            self.outNeodenConfigFilePath = os.getcwd()
            self.btnRemovePositionFile.setEnabled(False)
            self.btnGenerateNeodenConfig.setEnabled(False)


    def clearComponentTables(self):
        self.cleanComponentTables()
        self.pcb.clearLists()
        self.neodenFile.clearComponentList()


    def evt_btnOutputFolderDirectory_clicked(self):
        tempPath = QFileDialog.getExistingDirectory(self, "Select your output folder", self.outNeodenConfigFilePath)
        if tempPath != "":
            self.ledFilesOutputDirectory.setText(tempPath)
            self.outNeodenConfigFilePath = tempPath


    def evt_btnGenerateNeodenConfig_clicked(self):
        isTopNeodenFileCreated: bool = False
        isBotNeodenFileCreated: bool = False
        fileTopPath = self.outNeodenConfigFilePath + "/" + self.pcb.name + "-top.csv"
        fileBotPath = self.outNeodenConfigFilePath + "/" + self.pcb.name + "-bot.csv"



        if self.tableTopComponents.rowCount() > 0:
            isTopNeodenFileCreated = self.generateTopNeodenFile(fileTopPath)

            if isTopNeodenFileCreated:
                QMessageBox.information(self, "Pick and Place Files Created",
                                        "Pick and Place Top Neoden file was created in:<br><br><b>{}</b>".format(fileTopPath))

        if self.tableBottomComponents.rowCount() > 0:
            isBotNeodenFileCreated = self.generateBotNeodenFile(fileBotPath)

            if isBotNeodenFileCreated:
                QMessageBox.information(self, "Pick and Place Files Created",
                                        "Pick and Place Bot Neoden file was created in:<br><br><b>{}</b>".format(fileBotPath))



    def generateBotNeodenFile(self, toWriteFile: str) -> bool:
        buffer: str = ""

        if self.outNeodenConfigFilePath != "":
            buffer += NeodenFileIdentifiers.ConfigFileIdentifier.value
            buffer += '\n'

            for stack in self.neodenFile.botStackList:
                buffer += stack.getAsLineString()
                buffer += '\n'

            buffer += self.neodenFile.panelSetting
            buffer += '\n'

            buffer += self.neodenFile.getBotPCBFiducialSettingAsStringLine()
            buffer += '\n'

            for fid in self.neodenFile.botFiducialList:
                buffer += fid.getAsStringLine()
                buffer += '\n'

            buffer += self.neodenFile.pcbTesting
            buffer += '\n'

            buffer += self.neodenFile.pcbPanelFirstChipSetting.getAsStringLine()
            buffer += '\n'

            buffer += self.neodenFile.botPcbSinglePanel.getAsStringLine()
            buffer += '\n'

            buffer += NeodenFileIdentifiers.ComponentSectionIdentifier.value
            buffer += '\n'

            for comp in self.neodenFile.botComponentList:
                buffer += comp.getAsStringLine()
                buffer += '\n'

            buffer += '\n'

            if os.path.exists(toWriteFile):
                ans = QMessageBox.question(self, "Replace Existing File", "There exists already a <b>Bot neoden config file</b> in this folder\n"
                                                                    "<b>Do you want to replace this?</b>")
                if ans == QMessageBox.Yes:
                    with open(toWriteFile, 'w') as file:
                        file.write(buffer)
                        return True
                else:
                    QMessageBox.information(self, "Writing Neoden File - Bot", "Generate \"Neoden File - Bot\" has been canceled")
                    return False
            else:
                with open(toWriteFile, 'w') as file:
                    file.write(buffer)
                    return True


    def generateTopNeodenFile(self, toWriteFile: str) -> bool:
        buffer: str = ""

        if self.outNeodenConfigFilePath != "":
            buffer += NeodenFileIdentifiers.ConfigFileIdentifier.value
            buffer += '\n'

            for stack in self.neodenFile.topStackList:
                buffer += stack.getAsLineString()
                buffer += '\n'

            buffer += self.neodenFile.panelSetting
            buffer += '\n'

            buffer += self.neodenFile.getTopPCBFiducialSettingAsStringLine()
            buffer += '\n'

            for fid in self.neodenFile.topFiducialList:
                buffer += fid.getAsStringLine()
                buffer += '\n'

            buffer += self.neodenFile.pcbTesting
            buffer += '\n'

            buffer += self.neodenFile.pcbPanelFirstChipSetting.getAsStringLine()
            buffer += '\n'

            buffer += self.neodenFile.topPcbSinglePanel.getAsStringLine()
            buffer += '\n'

            buffer += NeodenFileIdentifiers.ComponentSectionIdentifier.value
            buffer += '\n'

            for comp in self.neodenFile.topComponentList:
                buffer += comp.getAsStringLine()
                buffer += '\n'

            buffer += '\n'

            if os.path.exists(toWriteFile):
                ans = QMessageBox.question(self, "Replace Existing File", "There exists already a <b>Top neoden config file</b> in this folder\n"
                                                                          "<b>Do you want to replace this?</b>")
                if ans == QMessageBox.Yes:
                    with open(toWriteFile, 'w') as file:
                        file.write(buffer)
                        return True
                else:
                    QMessageBox.information(self, "Writing Neoden File - Bot", "Generate \"Neoden File - Top\" has been canceled")
                    return False
            else:
                with open(toWriteFile, 'w') as file:
                    file.write(buffer)
                    return True



    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        fileEnter: str = event.mimeData().urls()[0].fileName()
        if fileEnter.endswith(".zip") or fileEnter.endswith(".csv"):
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        fileMoved: str = event.mimeData().urls()[0].fileName()
        if fileMoved.endswith(".zip") or fileMoved.endswith(".csv"):
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event: QtGui.QDragEnterEvent) -> None:
        fileDropped: str = event.mimeData().urls()[0].fileName()
        event.accept()
        # Set the Drop action to a Copy Action(icon to show)
        event.setDropAction(Qt.CopyAction)

        if len(self.pcb.topComponentList) > 0 or len(self.pcb.botComponentList):
            self.clearComponentTables()

        # Get the zip file path
        self.inPosFilePath = event.mimeData().urls()[0].toLocalFile()
        self.ledImportPositionFilePath.setText(self.inPosFilePath)
        self.btnRemovePositionFile.setEnabled(True)

        self.pcb.path = self.inPosFilePath

        # Check if dropped file has the .zip extension
        if fileDropped.endswith(".zip"):
            self.pcb.processPlacementFileFromZip()

        if fileDropped.endswith(".csv"):
            self.pcb.processPlacementFileFromFile(self.inPosFilePath)

        # Populate fiducials & component lists for further process
        self.neodenFile.topFiducialList = self.pcb.topFiducialList
        self.neodenFile.botFiducialList = self.pcb.botFiducialList
        self.neodenFile.topComponentList = self.pcb.topComponentList
        self.neodenFile.botComponentList = self.pcb.botComponentList

        # Populate top & bottom component tables
        self.populateTopComponentTable()
        self.populateBotComponentTable()

        # If the top or bottom comp table contains data, enable the "export" button
        if self.tableTopComponents.rowCount() > 0 or self.tableBottomComponents.rowCount() > 0:
            self.btnGenerateNeodenConfig.setEnabled(True)

