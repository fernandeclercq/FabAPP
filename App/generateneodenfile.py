from PyQt5.QtWidgets import *
from ui.generateNeodenFile_ui import *


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



    def evt_btnImportPosFile_clicked(self):
        pass

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