import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from convertgerbers_ui import *
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

        self.kicadFiles = ['-F_Cu.gbr', '-B_Cu.gbr', '-Edge_Cuts.gbr', '-PTH.drl', '-NPTH.drl']
        self.eagleFiles = ['copper_top.gbr', 'copper_bottom.gbr', 'profile.gbr', '.xln']

        self.foundLayers = {"Top-layer":
                      {"fileName": "",
                       "lstIndex": ""
                       },
                  "Bottom-layer":
                      {"fileName": "",
                       "lstIndex": ""
                      },
                    "Plated-Drills":
                        {"fileName": "",
                         "lstIndex": ""
                        },
                    "Non-Plated-Drills":
                        {"fileName": "",
                         "lstIndex": ""},
                    "Board-Outline":
                        {"fileName": "",
                         "lstIndex": ""
                        }
                  }

        self.hasKicadLayers = False

        self.myGerberFileName = ""
        self.myGerberFilePath = ""

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
        self.ledGerberPath.setText(self.myGerbersPath)
        self.lblConvertGerbers.setStyleSheet("QLabel { border: 4px dashed #00E200; }")
        self.lblConvertGerbers.setText(fileName)
        self.btnRenameGerbers.setEnabled(True)

        with zipfile.ZipFile(str(self.myGerbersPath), 'r') as myGerbers:
            myPCBLayers = myGerbers.namelist()
            self.hasKicadLayers = False

            for layer in range(0, len(myPCBLayers)):
                for layerName in self.kicadFiles:
                    layerFound = myPCBLayers[layer].endswith(layerName)
                    if layerFound:
                        if myPCBLayers[layer].endswith("-F_Cu.gbr"):
                            self.foundLayers["Top-layer"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Top-layer"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith("-B_Cu.gbr"):
                            self.foundLayers["Bottom-layer"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Bottom-layer"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith("-Edge_Cuts.gbr"):
                            self.foundLayers["Board-Outline"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Board-Outline"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith("-PTH.drl"):
                            self.foundLayers["Plated-Drills"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Plated-Drills"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith("-NPTH.drl"):
                            self.foundLayers["Non-Plated-Drills"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Non-Plated-Drills"]["lstIndex"] = str(layer)

                for layerName in self.eagleFiles:
                    layerFound = myPCBLayers[layer].endswith(layerName)
                    if layerFound:
                        if myPCBLayers[layer].endswith("copper_top.gbr"):
                            self.foundLayers["Top-layer"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Top-layer"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith("copper_bottom.gbr"):
                            self.foundLayers["Bottom-layer"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Bottom-layer"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith("profile.gbr"):
                            self.foundLayers["Board-Outline"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Board-Outline"]["lstIndex"] = str(layer)
                        if myPCBLayers[layer].endswith(".xln"):
                            self.foundLayers["Plated-Drills"]["fileName"] = myPCBLayers[layer]
                            self.foundLayers["Plated-Drills"]["lstIndex"] = str(layer)

            if self.foundLayers["Top-layer"]["fileName"].endswith("-F_Cu.gbr"):
                self.hasKicadLayers = True
                newStatus = """
                                    <h1>KiCad Layers:</h1>
                                    <p>
                                        Top layer: {} <b>---></b> {}<br><br>
                                        Bottom layer: {} <b>---></b> {}<br><br>
                                        Plated Drills: {} <b>---></b> {}<br>
                                        Non-Plated Drills: {} <b>---></b> {}<br><br>
                                        Board Outline: {} <b>---></b> {}
                                    </p>
                                    """.format(self.foundLayers["Top-layer"]["fileName"],
                                               self.foundLayers["Top-layer"]["fileName"][0:-4] + ".TOP",
                                               self.foundLayers["Bottom-layer"]["fileName"],
                                               self.foundLayers["Bottom-layer"]["fileName"][0:-4] + ".BOT",
                                               self.foundLayers["Plated-Drills"]["fileName"],
                                               self.foundLayers["Plated-Drills"]["fileName"][0:-4] + ".DRD",
                                               self.foundLayers["Non-Plated-Drills"]["fileName"],
                                               self.foundLayers["Non-Plated-Drills"]["fileName"][0:-4] + ".DRL",
                                               self.foundLayers["Board-Outline"]["fileName"],
                                               self.foundLayers["Board-Outline"]["fileName"][0:-4] + ".BOA")

                self.lblConvertGerbersDisplayChanges.setText(newStatus)
            elif self.foundLayers["Top-layer"]["fileName"].endswith("copper_top.gbr"):
                self.hasKicadLayers = False
                newStatus = """
                <h1>Eagle Layers:</h1>
                <p>
                    Top layer: {} <b>---></b> {}<br><br>
                    Bottom layer: {} <b>---></b> {}<br><br>
                    Drills: {} <b>---></b> {}<br><br>
                    Board Outline: {} <b>---></b> {}
                </p>
                """.format(self.foundLayers["Top-layer"]["fileName"],
                           self.foundLayers["Top-layer"]["fileName"][0:-4] + ".TOP",
                           self.foundLayers["Bottom-layer"]["fileName"],
                           self.foundLayers["Bottom-layer"]["fileName"][0:-4] + ".BOT",
                           self.foundLayers["Plated-Drills"]["fileName"],
                           self.foundLayers["Plated-Drills"]["fileName"][0:-4] + ".DRD",
                           self.foundLayers["Board-Outline"]["fileName"],
                           self.foundLayers["Board-Outline"]["fileName"][0:-4] + ".BOA")

                self.lblConvertGerbersDisplayChanges.setText(newStatus)

    def evt_btnRenameGerbers_clicked(self):
        with zipfile.ZipFile(self.myGerbersPath, 'r') as myGerbers:
            pathToExtract = self.myGerberFilePath + "/" + self.myGerberFileName[0:-4]
            if self.hasKicadLayers:
                self.extractFilesToPath(myGerbers, pathToExtract)

                ### KiCad Non-Plated Drills Layer
                myGerbers.extract(self.foundLayers["Non-Plated-Drills"]["fileName"], pathToExtract)
                os.rename(pathToExtract + "/" + self.foundLayers["Non-Plated-Drills"]["fileName"],
                          pathToExtract + "/" + self.foundLayers["Non-Plated-Drills"]["fileName"][0:-4] + ".DRL")
            else:
                self.extractFilesToPath(myGerbers, pathToExtract)

    def extractFilesToPath(self, gerbers: zipfile, pathToExtract: str) -> None:
        gerbers.extract(self.foundLayers["Top-layer"]["fileName"], pathToExtract)
        os.rename(pathToExtract + "/" + self.foundLayers["Top-layer"]["fileName"],
                  pathToExtract + "/" + self.foundLayers["Top-layer"]["fileName"][0:-4] + ".TOP")

        gerbers.extract(self.foundLayers["Bottom-layer"]["fileName"], pathToExtract)
        os.rename(pathToExtract + "/" + self.foundLayers["Bottom-layer"]["fileName"],
                  pathToExtract + "/" + self.foundLayers["Bottom-layer"]["fileName"][0:-4] + ".BOT")

        gerbers.extract(self.foundLayers["Board-Outline"]["fileName"], pathToExtract)
        os.rename(pathToExtract + "/" + self.foundLayers["Board-Outline"]["fileName"],
                  pathToExtract + "/" + self.foundLayers["Board-Outline"]["fileName"][0:-4] + ".BOA")

        gerbers.extract(self.foundLayers["Plated-Drills"]["fileName"], pathToExtract)
        os.rename(pathToExtract + "/" + self.foundLayers["Plated-Drills"]["fileName"],
                  pathToExtract + "/" + self.foundLayers["Plated-Drills"]["fileName"][0:-4] + ".DRD")


    def evt_btnImportGerbers_clicked(self):
        self.myGerbersPath = QFileDialog.getOpenFileName(self, "Open File", self.myGerbersPath, "Zip file(*.zip)")[0]
        if self.myGerbersPath != "":
            self.myGerberFileName, self.myGerberFilePath = self.getFilenameFromPath(self.myGerbersPath)
            self.ledGerberPath.setText(self.myGerbersPath)
            self.lblConvertGerbers.setStyleSheet("QLabel { border: 4px dashed #00E200; }")
            self.lblConvertGerbers.setText(self.myGerberFileName)
            self.btnRenameGerbers.setEnabled(True)

            with zipfile.ZipFile(str(self.myGerbersPath), 'r') as myGerbers:
                myPCBLayers = myGerbers.namelist()
                self.hasKicadLayers = False

                for layer in range(0, len(myPCBLayers)):
                    for layerName in self.kicadFiles:
                        layerFound = myPCBLayers[layer].endswith(layerName)
                        if layerFound:
                            if myPCBLayers[layer].endswith("-F_Cu.gbr"):
                                self.foundLayers["Top-layer"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Top-layer"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith("-B_Cu.gbr"):
                                self.foundLayers["Bottom-layer"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Bottom-layer"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith("-Edge_Cuts.gbr"):
                                self.foundLayers["Board-Outline"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Board-Outline"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith("-PTH.drl"):
                                self.foundLayers["Plated-Drills"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Plated-Drills"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith("-NPTH.drl"):
                                self.foundLayers["Non-Plated-Drills"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Non-Plated-Drills"]["lstIndex"] = str(layer)

                    for layerName in self.eagleFiles:
                        layerFound = myPCBLayers[layer].endswith(layerName)
                        if layerFound:
                            if myPCBLayers[layer].endswith("copper_top.gbr"):
                                self.foundLayers["Top-layer"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Top-layer"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith("copper_bottom.gbr"):
                                self.foundLayers["Bottom-layer"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Bottom-layer"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith("profile.gbr"):
                                self.foundLayers["Board-Outline"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Board-Outline"]["lstIndex"] = str(layer)
                            if myPCBLayers[layer].endswith(".xln"):
                                self.foundLayers["Plated-Drills"]["fileName"] = myPCBLayers[layer]
                                self.foundLayers["Plated-Drills"]["lstIndex"] = str(layer)

                if self.foundLayers["Top-layer"]["fileName"].endswith("-F_Cu.gbr"):
                    self.hasKicadLayers = True
                    newStatus = """
                                        <h1>KiCad Layers:</h1>
                                        <p>
                                            Top layer: {} <b>---></b> {}<br><br>
                                            Bottom layer: {} <b>---></b> {}<br><br>
                                            Plated Drills: {} <b>---></b> {}<br>
                                            Non-Plated Drills: {} <b>---></b> {}<br><br>
                                            Board Outline: {} <b>---></b> {}
                                        </p>
                                        """.format(self.foundLayers["Top-layer"]["fileName"],
                                                   self.foundLayers["Top-layer"]["fileName"][0:-4] + ".TOP",
                                                   self.foundLayers["Bottom-layer"]["fileName"],
                                                   self.foundLayers["Bottom-layer"]["fileName"][0:-4] + ".BOT",
                                                   self.foundLayers["Plated-Drills"]["fileName"],
                                                   self.foundLayers["Plated-Drills"]["fileName"][0:-4] + ".DRD",
                                                   self.foundLayers["Non-Plated-Drills"]["fileName"],
                                                   self.foundLayers["Non-Plated-Drills"]["fileName"][0:-4] + ".DRL",
                                                   self.foundLayers["Board-Outline"]["fileName"],
                                                   self.foundLayers["Board-Outline"]["fileName"][0:-4] + ".BOA")

                    self.lblConvertGerbersDisplayChanges.setText(newStatus)
                elif self.foundLayers["Top-layer"]["fileName"].endswith("copper_top.gbr"):
                    self.hasKicadLayers = False
                    newStatus = """
                    <h1>Eagle Layers:</h1>
                    <p>
                        Top layer: {} <b>---></b> {}<br><br>
                        Bottom layer: {} <b>---></b> {}<br><br>
                        Drills: {} <b>---></b> {}<br><br>
                        Board Outline: {} <b>---></b> {}
                    </p>
                    """.format(self.foundLayers["Top-layer"]["fileName"], self.foundLayers["Top-layer"]["fileName"][0:-4] + ".TOP",
                               self.foundLayers["Bottom-layer"]["fileName"], self.foundLayers["Bottom-layer"]["fileName"][0:-4] + ".BOT",
                               self.foundLayers["Plated-Drills"]["fileName"], self.foundLayers["Plated-Drills"]["fileName"][0:-4] + ".DRD",
                               self.foundLayers["Board-Outline"]["fileName"], self.foundLayers["Board-Outline"]["fileName"][0:-4] + ".BOA")

                    self.lblConvertGerbersDisplayChanges.setText(newStatus)





    def getFilenameFromPath(self, path: str) -> list[str]:
        if path.find("/"):
            index = path.rfind("/")
            return [path[(index+1):], path[0:index]]
        elif path.find("\\"):
            index = path.rfind("\\")
            return [path[(index+1):], path[0:index]]
        else:
            return [path, path]

