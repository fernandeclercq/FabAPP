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

        self.neodenStackConfigPath = "./config/Neoden_stack_config.csv"
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





    def evt_btnImportPosFile_clicked(self):
        # noinspection PyArgumentList
        inPath = QFileDialog.getOpenFileName(self, "Import Position File as Zip", self.inPosFilePath, "Zip file(*.zip)")[0]
        if inPath != "":
            if zipfile.is_zipfile(inPath):
                self.btnRemovePositionFile.setEnabled(True)
                self.ledImportPositionFilePath.setText(inPath)

                # Setting the path of the zip for the gerbers + componentlists,
                # will automatically sort the list for the components and create 2 lists with:
                # top components and bot components
                if len(self.pcb.topComponentList) > 0 or len(self.pcb.botComponentList):
                    self.clearComponentTables()

                self.pcb.path = inPath

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
                # Export : Yes / No
                # self.tableTopComponents.setCellWidget(row, 0, self.createCellWithCheckBox())
                # Feeder number (1 - 48)
                self.tableTopComponents.setCellWidget(row, 0, self.createFeederCmb(self.neodenFile.topComponentList[row].feederId))
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
                # Export : Yes / No
                # self.tableBottomComponents.setCellWidget(row, 0, self.createCellWithCheckBox())
                # Feeder number (1 - 48)
                self.tableBottomComponents.setCellWidget(row, 0, self.createFeederCmb(self.neodenFile.botComponentList[row].feederId))
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



    def createCellWithCheckBox(self, is_checked: bool = True) -> QWidget:
        cell_widget = QWidget()
        chk_box = QCheckBox()
        if is_checked:
            chk_box.setCheckState(Qt.Checked)
        else:
            chk_box.setCheckState(Qt.Unchecked)
        lay_out = QHBoxLayout(cell_widget)
        lay_out.addWidget(chk_box)
        lay_out.setAlignment(Qt.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)

        return cell_widget


    def createFeederCmb(self, feeder_id: int) -> QComboBox:
        cmb = QComboBox()
        start = 1
        end = 49
        myFeederIds = []
        for i in range(start, end):
            myFeederIds.append(str(i))

        cmb.addItems(myFeederIds)
        cmb.setCurrentIndex(int(feeder_id ) - 1)
        return cmb

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
        isBopNeodenFileCreated: bool = False
        fileTopPath = self.outNeodenConfigFilePath + "/" + self.pcb.name + "-top.csv"
        fileBopPath = self.outNeodenConfigFilePath + "/" + self.pcb.name + "-bot.csv"



        if self.tableTopComponents.rowCount() > 0:
            isTopNeodenFileCreated = self.generateTopNeodenFile(fileTopPath)

            if isTopNeodenFileCreated:
                QMessageBox.information(self, "Pick and Place Files Created",
                                        "Pick and Place Top Neoden file was created in:<br><br><b>{}</b>".format(
                                        fileTopPath))

        if self.tableBottomComponents.rowCount() > 0:
            isBopNeodenFileCreated = self.generateBotNeodenFile(fileBopPath)

            if isBopNeodenFileCreated:
                QMessageBox.information(self, "Pick and Place Files Created",
                                        "Pick and Place Bot Neoden file was created in:<br><br><b>{}</b>".format(
                                        fileBopPath
                                        ))



    def generateBotNeodenFile(self, toWriteFile: str) -> bool:
        buffer: str = ""

        if self.outNeodenConfigFilePath != "":
            buffer += NeodenFileIdentifiers.ConfigFileIdentifier.value
            buffer += '\n'

            for stack in self.neodenFile.botStackList():
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
            self.inPosFilePath = event.mimeData().urls()[0].toLocalFile()
            self.ledImportPositionFilePath.setText(self.inPosFilePath)
            self.btnRemovePositionFile.setEnabled(True)

            # Setting the path of the zip for the gerbers + componentlists,
            # will automatically sort the list for the components and create 2 lists with:
            # top components and bot components
            if len(self.pcb.topComponentList) > 0 or len(self.pcb.botComponentList):
                self.clearComponentTables()

            self.pcb.path = self.inPosFilePath

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

