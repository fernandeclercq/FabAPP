from App.ui.editDefinitions import *
import os
import platform
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import zipfile
from App.modules.PCBLayer import *


class EditDefinitions(QDialog, Ui_EditDefinitions_Dialog):
    def __init__(self):
        super(EditDefinitions, self).__init__()
        self.setupUi(self)
        self.setLayout(self.vQBox_Main)


