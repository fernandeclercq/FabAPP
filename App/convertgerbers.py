import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.convertGerbers_ui import *
import zipfile

class ConvertGerbers(QDialog, Ui_Dialog):
    def __init__(self):
        super(ConvertGerbers, self).__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.ledGerberPath.setText(os.getcwd())

        self.btnImportGrbs.clicked.connect(self.evt_btnImportGerbers_clicked)
        self.btnRenameGerbers.clicked.connect(self.evt_btnRenameGerbers_clicked)

        self.myGerbersPath = os.getcwd()


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
        self.myGerbersPath = event.mimeData().urls()[0].toLocalFile()

        self.gerbersAccepted(fileName)


        with zipfile.ZipFile(str(self.myGerbersPath), 'r') as myGerbers:
            myPCBLayers = myGerbers.namelist()
            print(myPCBLayers)



    def evt_btnRenameGerbers_clicked(self):
        pass

    def extractFilesToPath(self, gerbers: zipfile, pathToExtract: str) -> None:
        pass

    def evt_btnImportGerbers_clicked(self):
        self.myGerbersPath = QFileDialog.getOpenFileName(self, "Import Gerber Files",
                                                         self.myGerbersPath, "Zip file(*.zip)")[0]

        #print(self.myGerbersPath)
        with zipfile.ZipFile(str(self.myGerbersPath), 'r') as myGerbers:
        #    print(myGerbers.namelist())

            for file in myGerbers.namelist():
                lastSlashIndex =  file.rfind("/")
                if file[(lastSlashIndex + 1):] != "":

                    if file.endswith(".gbr"):
                        print(file)
                        with myGerbers.open(file, mode='r') as thefile:
                            lstStr = []
                            for x in range(0, 10):
                                temp = thefile.readline(200)
                                #print(temp)
                                if temp != "b'G75*\\n'":
                                    print(temp)
                                #     lstStr.append(thefile.readline(200))
                                # else:
                                #     break;
                                # print(lstStr)


    def gerbersAccepted(self, filename):
        self.ledGerberPath.setText(self.myGerbersPath)
        self.lblConvertGerbers.setStyleSheet("QLabel { border: 4px dashed #00E200; }")
        self.lblConvertGerbers.setText(filename)
        self.btnRenameGerbers.setEnabled(True)






