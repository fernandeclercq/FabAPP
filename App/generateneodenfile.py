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

        self.btnOutputFolderDirectory.clicked.connect(self.evt_btnOutputFolderDirectory_clicked)
        self.btnGenerateNeodenConfig.clicked.connect(self.evt_btnGenerateNeodenConfig_clicked)

        self.inPosFilePath = ""
        self.outNeodenConfigFilePath = ""

        self.c1 = Component("C1", "100nf", "100nf", Position(12.5, 15.5, 90), Footprint("0805_handSolder", "0805"))
        self.c2 = Component("C1", "100nf", "100nf", Position(12.5, 15.5, 90), Footprint("0805_handSolder", "0805"))
        self.c3 = Component("C1", "100nf", "100nf", Position(12.5, 15.5, 90), Footprint("0805_handSolder", "0805"))
        self.c4 = Component("C1", "100nf", "100nf", Position(12.5, 15.5, 90), Footprint("0805_handSolder", "0805"))

        self.pcb = PCB()
        self.pcb.componentList.append(self.c1)
        self.pcb.componentList.append(self.c2)
        self.pcb.componentList.append(self.c3)
        self.pcb.componentList.append(self.c4)




        print(self.pcb.componentList, sep="\n")
        print(self.pcb.placementFileList)


    def evt_btnImportPosFile_clicked(self):
        inPath = QFileDialog.getOpenFileName(self, "Import Position File as Zip", os.getcwd(), "Zip file(*.zip)")[0]
        if inPath != "":
            if zipfile.is_zipfile(inPath):
                print(inPath)

            #print(zipfile.is_zipfile(inPath))


    def evt_btnRemovePosFile_clicked(self):
        pass

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