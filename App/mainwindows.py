from App.ui.mainWindow_ui import Ui_MainWindowDialog
from App.convertgerbers import *
from App.generateneodenfile import *


class MainWindow(QDialog, Ui_MainWindowDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("img/AP_logo_256.png"))
        self.setWindowTitle("FabApp")

        self.btnConvertGrb.clicked.connect(self.evt_btnConvertGerbers_clicked)
        self.btnGenerateNeodenFile.clicked.connect(self.evt_btnGenerateNeodenFile_clicked)
        self.setLayout(self.vQBox_main)


    ### Events Handlers - Main Window

    def evt_btnConvertGerbers_clicked(self):
        convertGerbers_page = ConvertGerbers()
        convertGerbers_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        convertGerbers_page.exec_()

    def evt_btnGenerateNeodenFile_clicked(self):
        generateNeodenFile_page = GenerateNeodenFile()
        generateNeodenFile_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        generateNeodenFile_page.exec_()

