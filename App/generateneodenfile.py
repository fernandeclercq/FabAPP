from PyQt5.QtWidgets import *
from ui.generateNeodenFile_ui import *
from modules.PCB.PCB import *
import os
import platform
from PyQt5.QtCore import *
import zipfile


class GenerateNeodenFile(QDialog, Ui_GenerateNeodenConfigDialog):
    def __init__(self):
        super(GenerateNeodenFile, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("img/AP_logo_256.png"))
        self.setAcceptDrops(True)

        self.ledFilesOutputDirectory.setReadOnly(True)
        self.ledImportPositionFilePath.setReadOnly(True)

        self.btnImportPositionFile.clicked.connect(self.evt_btnImportPosFile_clicked)
        self.btnRemovePositionFile.clicked.connect(self.evt_btnRemovePosFile_clicked)
        self.btnRemovePositionFile.setEnabled(False)

        self.btnOutputFolderDirectory.clicked.connect(self.evt_btnOutputFolderDirectory_clicked)
        self.btnGenerateNeodenConfig.clicked.connect(self.evt_btnGenerateNeodenConfig_clicked)

        self.inPosFilePath = os.getcwd()
        self.outNeodenConfigFilePath = os.getcwd()

        self.pcb = PCB()



    def evt_btnImportPosFile_clicked(self):
        # noinspection PyArgumentList
        inPath = QFileDialog.getOpenFileName(self, "Import Position File as Zip", self.inPosFilePath, "Zip file(*.zip)")[0]
        if inPath != "":
            if zipfile.is_zipfile(inPath):
                self.btnRemovePositionFile.setEnabled(True)
                self.ledImportPositionFilePath.setText(inPath)
                self.pcb.path = inPath
                self.tableTopComponents.setRowCount(len(self.pcb.topComponentList))
                self.tableBottomComponents.setRowCount(len(self.pcb.botComponentList))

                print(len(self.pcb.topComponentList))
                print(len(self.pcb.topFiducialList))

                print(self.pcb.topComponentList)



                for row in range(0, len(self.pcb.topComponentList)):
                    self.tableTopComponents.setCellWidget(row, 0, self.createCellWithCheckBox())
                    self.tableTopComponents.setItem(row, 1, QTableWidgetItem("1"))
                    self.tableTopComponents.setItem(row, 2, QTableWidgetItem("1"))
                    self.tableTopComponents.setItem(row, 3, QTableWidgetItem(self.pcb.topComponentList[row].refName))
                    self.tableTopComponents.setItem(row, 4, QTableWidgetItem(self.pcb.topComponentList[row].Value))
                    self.tableTopComponents.setItem(row, 5, QTableWidgetItem(self.pcb.topComponentList[row].footprint.transformedValue))
                    self.tableTopComponents.setItem(row, 6, QTableWidgetItem(str(self.pcb.topComponentList[row].position.transformedX_pos)))
                    self.tableTopComponents.setItem(row, 7, QTableWidgetItem(str(self.pcb.topComponentList[row].position.transformedY_pos)))
                    self.tableTopComponents.setItem(row, 8, QTableWidgetItem(str(self.pcb.topComponentList[row].position.transformedRotation)))
                    self.tableTopComponents.setItem(row, 9, QTableWidgetItem("Yes"))



                # noinspection PyArgumentList
                # cell_widget = QWidget()
                # chk_box = QCheckBox()
                # chk_box.setCheckState(Qt.Unchecked)
                # lay_out = QHBoxLayout(cell_widget)
                # lay_out.addWidget(chk_box)
                # lay_out.setAlignment(Qt.AlignCenter)
                # lay_out.setContentsMargins(0, 0, 0, 0)
                # cell_widget.setLayout(lay_out)





                # for i in range(self.tableTopComponents.rowCount()):
                #     chkbox = self.tableTopComponents.cellWidget(i, 0).findChild(QCheckBox).isChecked()
                #     print(chkbox)




    def createCellWithCheckBox(self, isChecked: bool = True) -> QWidget:
        cell_widget = QWidget()
        chk_box = QCheckBox()
        if isChecked:
            chk_box.setCheckState(Qt.Checked)
        else:
            chk_box.setCheckState(Qt.Unchecked)
        lay_out = QHBoxLayout(cell_widget)
        lay_out.addWidget(chk_box)
        lay_out.setAlignment(Qt.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)

        return cell_widget


    def evt_btnRemovePosFile_clicked(self):
        if self.ledImportPositionFilePath.text() != "":
            self.ledImportPositionFilePath.setText("")
            self.pcb.clearLists()
            self.inPosFilePath = os.getcwd()
            self.btnRemovePositionFile.setEnabled(False)


    def evt_btnOutputFolderDirectory_clicked(self):
        pass

    def evt_btnGenerateNeodenConfig_clicked(self):
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

