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

        self.btnEditDefinitions_Cancel.clicked.connect(self.evt_btnCancel_clicked)


        self.definitions = definitions

        self.dspbNeodenOriginX.setValue(self.definitions.originX)
        self.dspbNeodenOriginY.setValue(self.definitions.originY)

        print(self.definitions.footprintPackages)
        print(self.definitions.availableNozzles)
        print(self.definitions.installedNozzles)





    def evt_btnCancel_clicked(self):
        self.close()

