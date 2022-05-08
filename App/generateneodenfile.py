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
        inPath = QFileDialog.getOpenFileName(self, "Import Position File as Zip", self.inPosFilePath, "Zip file(*.zip)")[0]
        if inPath != "":
            if zipfile.is_zipfile(inPath):
                self.btnRemovePositionFile.setEnabled(True)
                self.ledImportPositionFilePath.setText(inPath)
                self.pcb.path = inPath
                topPlacementFile = self.pcb.getPlacementFile(PCBSide.TOP)
                print(topPlacementFile.entryList, sep="\n")
                print(topPlacementFile.headerList)




    def evt_btnRemovePosFile_clicked(self):
        if self.ledImportPositionFilePath.text() != "":
            self.ledImportPositionFilePath.setText("")
            self.inPosFilePath = os.getcwd()
            self.btnRemovePositionFile.setEnabled(False)


    def evt_btnOutputFolderDirectory_clicked(self):
        pass

    def evt_btnGenerateNeodenConfig_clicked(self):
        pass

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        pass

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        pass

    def dropEvent(self, event: QtGui.QDragEnterEvent) -> None:
        pass