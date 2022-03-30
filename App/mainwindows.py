from ui.mainWindows_ui import Ui_Dialog as mainwindows_ui
from convertgerbers import *
from generateneodenfile import *

class MainWindow(QDialog, mainwindows_ui):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btnConvertGrb.clicked.connect(self.evt_btnConvertGerbers_clicked)
        self.btnGenerateNeodenFile.clicked.connect(self.evt_btnGenerateNeodenFile_clicked)

    ### Events Handlers - Main Window

    def evt_btnConvertGerbers_clicked(self):
        convertGerbers_page = ConvertGerbers()
        convertGerbers_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        convertGerbers_page.exec_()

    def evt_btnGenerateNeodenFile_clicked(self):
        generateNeodenFile_page = GenerateNeodenFile()
        generateNeodenFile_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        generateNeodenFile_page.exec_()

