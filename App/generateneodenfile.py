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
                self.pcb.path = inPath


                self.neodenFile.topFiducialList = self.pcb.topFiducialList
                self.neodenFile.botFiducialList = self.pcb.botFiducialList
                self.neodenFile.topComponentList = self.pcb.topComponentList
                self.neodenFile.botComponentList = self.pcb.botComponentList




                self.populateTopComponentTable()
                # self.populateBotComponentTable()
                #
                # if self.tableTopComponents.rowCount() > 0 or self.tableBottomComponents.rowCount() > 0:
                #     self.btnGenerateNeodenConfig.setEnabled(True)





    def populateTopComponentTable(self):
        if len(self.neodenFile.topComponentList) > 0:
            self.tableTopComponents.setRowCount(len(self.neodenFile.topComponentList))

            for row in range(0, len(self.pcb.topComponentList)):
                # Export : Yes / No
                self.tableTopComponents.setCellWidget(row, 0, self.createCellWithCheckBox())
                # Feeder number (1 - 48)

                self.tableTopComponents.setCellWidget(row, 1, self.createFeederCmb(self.neodenFile.topComponentList[row].feederId))
                # Nozzle Number (1 - 4)
                self.tableTopComponents.setCellWidget(row, 2, self.createNozzleCmb(self.neodenFile.topComponentList[row].nozzle))
                # Comp Name
                self.tableTopComponents.setItem(row, 3, QTableWidgetItem(self.pcb.topComponentList[row].refName))
            #     self.tableTopComponents.setItem(row, 4, QTableWidgetItem(self.pcb.topComponentList[row].Value))
            #     self.tableTopComponents.setItem(row, 5, QTableWidgetItem(
            #         self.pcb.topComponentList[row].footprint.transformedValue))
            #     self.tableTopComponents.setItem(row, 6, QTableWidgetItem(
            #         str(self.pcb.topComponentList[row].position.transformedX_pos)))
            #     self.tableTopComponents.setItem(row, 7, QTableWidgetItem(
            #         str(self.pcb.topComponentList[row].position.transformedY_pos)))
            #     self.tableTopComponents.setItem(row, 8, QTableWidgetItem(
            #         str(self.pcb.topComponentList[row].position.transformedRotation)))
            #     self.tableTopComponents.setCellWidget(row, 9, self.createCellWithCmb(["No", "Yes"]))
            pass


    def populateBotComponentTable(self):
        if len(self.pcb.botComponentList) > 0:
            self.tableBottomComponents.setRowCount(len(self.pcb.botComponentList))

            # for row in range(0, len(self.pcb.botComponentList)):
            #     # Export : Yes / No
            #     self.tableBottomComponents.setCellWidget(row, 0, self.createCellWithCheckBox())
            #     # Feeder number (1 - 98)
            #     self.tableBottomComponents.setCellWidget(row, 1, self.createCellWithCmb(["1", "2", "3", "4"]))
            #     # Nozzle Number (1 - 4)
            #     self.tableBottomComponents.setCellWidget(row, 2, self.defineNozzleNumber(
            #         self.pcb.botComponentList[row].footprint.transformedValue))
            #     # Comp Name
            #     self.tableBottomComponents.setItem(row, 3, QTableWidgetItem(self.pcb.botComponentList[row].refName))
            #     self.tableBottomComponents.setItem(row, 4, QTableWidgetItem(self.pcb.botComponentList[row].Value))
            #     self.tableBottomComponents.setItem(row, 5, QTableWidgetItem(
            #         self.pcb.botComponentList[row].footprint.transformedValue))
            #     self.tableBottomComponents.setItem(row, 6, QTableWidgetItem(
            #         str(self.pcb.botComponentList[row].position.transformedX_pos)))
            #     self.tableBottomComponents.setItem(row, 7, QTableWidgetItem(
            #         str(self.pcb.botComponentList[row].position.transformedY_pos)))
            #     self.tableBottomComponents.setItem(row, 8, QTableWidgetItem(
            #         str(self.pcb.botComponentList[row].position.transformedRotation)))
            #     self.tableBottomComponents.setCellWidget(row, 9, self.createCellWithCmb(["No", "Yes"]))
            pass


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

    def defineNozzleNumber(self, footprint: str):
        cmb = QComboBox()
        cmb.addItems(["1", "2", "3", "4"])

        if self.prevNozzle == 0:
            if footprint == "0805":
                self.prevFootprint = footprint
                self.prevNozzle = 1
        else:
            if footprint == "0805":
                if footprint == self.prevFootprint and self.prevNozzle == 1:
                    cmb.setCurrentIndex(1)
                    self.prevFootprint = footprint
                    self.prevNozzle = 2
                else:
                    cmb.setCurrentIndex(0)
                    self.prevFootprint = footprint
                    self.prevNozzle = 1

        return cmb


    def evt_btnRemovePosFile_clicked(self):
        if self.ledImportPositionFilePath.text() != "":
            self.ledImportPositionFilePath.setText("")
            self.ledFilesOutputDirectory.setText("")
            self.cleanComponentTables()
            self.pcb.clearLists()
            self.inPosFilePath = os.getcwd()
            self.outNeodenConfigFilePath = os.getcwd()
            self.btnRemovePositionFile.setEnabled(False)
            self.btnGenerateNeodenConfig.setEnabled(False)


    def evt_btnOutputFolderDirectory_clicked(self):
        tempPath = QFileDialog.getExistingDirectory(self, "Select your output folder", self.outNeodenConfigFilePath)
        if tempPath != "":
            self.ledFilesOutputDirectory.setText(tempPath)
            self.outNeodenConfigFilePath = tempPath

    def evt_btnGenerateNeodenConfig_clicked(self):
        # with open(self.outNeodenConfigFilePath + "/test.txt", 'w') as file:
        #     file.write("""
        #     #Feeder,Feeder ID,Type,Nozzle,X,Y,Angle,Footprint,Value,Pick height,Pick delay,Placement height,Placement delay,Vacuum detection,Vacuum value,Vision alignment,Speed,
        #     stack,3,0,1,411.36,119.04,90.00,0805,0805/1k,1.50,100,1.00,100,No,-40,1,60,4,50,80,No,No,
        #     stack,6,0,1,411.07,158.43,90.00,0805,0805/10k,1.50,100,1.00,100,No,-40,1,60,8,50,80,No,No,
        #     stack,12,0,1,411.04,303.79,90.00,0805,0805/22pF,0.50,100,1.00,100,No,-40,1,60,4,50,80,No,No,
        #     stack,13,0,1,411.50,325.34,90.00,0805,0805/LED1,2.00,100,1.50,100,No,-40,1,60,4,50,80,No,No,
        #     stack,97,1,4,282.68,83.46,0.00,SOT223-3,SOT223-3/AMS-3.3V,0.00,100,1.50,100,No,-60,1,60,1,1,281.83,114.95,1,1,No,No,
        #     stack,98,1,3,95.72,320.98,90.00,QFN32,QFN-32/STM8S,1.00,100,2.00,100,No,-40,1,40,7,4,165.50,355.88,1,1,No,No,""")

        # Chip,Feeder ID,Nozzle,Name,Value,Footprint,X,Y,Rotation,Skip
        # comp, 12, 1, C1, 100nF, 0805, 83.73, 15.96, -90.00, No,
        # comp, 12, 1, C2, 22pF, 0805, 72.53, 28.32, -90.00, No,
        # comp, 12, 1, C3, 22pF, 0805, 78.63, 25.72, 90.00, No,


        # for i in range(self.tableTopComponents.rowCount()):
        #     chkbox = self.tableTopComponents.cellWidget(i, 0).findChild(QCheckBox).isChecked()
        #     print(chkbox)

        # tmp: QComboBox = self.tableTopComponents.cellWidget(0, 2)
        # tmp2: QCheckBox = self.tableTopComponents.cellWidget(0, 0).children()[1]
        # print(tmp.currentText())
        # print(tmp2.isChecked())
        #
        # for stack in self.neodenFile.stackList:
        #     print(stack.getAsLineString())
        #
        # print(self.neodenFile.pcbPanelFirstChipSetting.getAsStringLine())
        #
        # for fid in self.pcb.topFiducialList:
        #     print(fid)

        pass




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

            self.pcb.path = self.inPosFilePath

            self.populateTopComponentTable()
            self.populateBotComponentTable()

            if self.tableTopComponents.rowCount() > 0 or self.tableBottomComponents.rowCount() > 0:
                self.btnGenerateNeodenConfig.setEnabled(True)

