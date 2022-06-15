from App.ui.editDefinitions import *
import os
import platform
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import zipfile
from App.modules.Definitions.Definitions import Definition


class EditDefinitions(QDialog, Ui_EditDefinitions_Dialog):
    def __init__(self, definitions: Definition):
        super(EditDefinitions, self).__init__()
        self.setupUi(self)
        self.setLayout(self.vQBox_Main)
        self.setWindowIcon(QtGui.QIcon("img/AP_logo_256.png"))

        self.btnEditDefinitions_Cancel.clicked.connect(self.evt_btnCancel_clicked)


        self.definitions = definitions

        self.dspbNeodenOriginX.setValue(self.definitions.originX)
        self.dspbNeodenOriginY.setValue(self.definitions.originY)
        self.populateNozzleCmbBox()



    def populateNozzleCmbBox(self):
        for av_nozzles in self.definitions.availableNozzles:
            self.cmbInstalledNozzle_1.addItem(av_nozzles.nozzle.name, av_nozzles.id)
            self.cmbInstalledNozzle_2.addItem(av_nozzles.nozzle.name, av_nozzles.id)
            self.cmbInstalledNozzle_3.addItem(av_nozzles.nozzle.name, av_nozzles.id)
            self.cmbInstalledNozzle_4.addItem(av_nozzles.nozzle.name, av_nozzles.id)

        idx_1 = self.cmbInstalledNozzle_1.findText(self.definitions.getInstalledNozzleByPosition(1).avNozzle.nozzle.name)
        idx_2 = self.cmbInstalledNozzle_1.findText(self.definitions.getInstalledNozzleByPosition(2).avNozzle.nozzle.name)
        idx_3 = self.cmbInstalledNozzle_1.findText(self.definitions.getInstalledNozzleByPosition(3).avNozzle.nozzle.name)
        idx_4 = self.cmbInstalledNozzle_1.findText(self.definitions.getInstalledNozzleByPosition(4).avNozzle.nozzle.name)

        self.cmbInstalledNozzle_1.setCurrentIndex(idx_1)
        self.cmbInstalledNozzle_2.setCurrentIndex(idx_2)
        self.cmbInstalledNozzle_3.setCurrentIndex(idx_3)
        self.cmbInstalledNozzle_4.setCurrentIndex(idx_4)




    def evt_btnCancel_clicked(self):
        self.close()

