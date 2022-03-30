from PyQt5.QtWidgets import *
from generateneodenfile_ui import *

class GenerateNeodenFile(QDialog, Ui_Dialog):
    def __init__(self):
        super(GenerateNeodenFile, self).__init__()
        self.setupUi(self)

