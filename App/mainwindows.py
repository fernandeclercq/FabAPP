from App.ui.mainWindow_ui import Ui_MainWindowDialog
from App.convertgerbers import *
from App.generateneodenfile import *
from App.editDefinitions import *
from App.modules.Definitions.Definitions import Definition


class MainWindow(QDialog, Ui_MainWindowDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("img/AP_logo_256.png"))
        self.setWindowTitle("FabApp")
        self.setLayout(self.vQBox_main)


        self.btnConvertGrb.clicked.connect(self.evt_btnConvertGerbers_clicked)
        self.btnGenerateNeodenFile.clicked.connect(self.evt_btnGenerateNeodenFile_clicked)
        self.btnEditDefinitions.clicked.connect(self.evt_btnEditDefinitions_clicked)


        ### todo: Implement Check if Definitions.xml exists
        self.definitions = Definition()
        self.definitions.initializeXmlHandler()






    ### Events Handlers - Main Window

    def evt_btnConvertGerbers_clicked(self):
        convertGerbers_page = ConvertGerbers()
        convertGerbers_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        convertGerbers_page.exec_()

    def evt_btnGenerateNeodenFile_clicked(self):
        generateNeodenFile_page = GenerateNeodenFile()
        generateNeodenFile_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        generateNeodenFile_page.exec_()

    def evt_btnEditDefinitions_clicked(self):
        editDefinitions_page = EditDefinitions(self.definitions)
        editDefinitions_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        editDefinitions_page.exec_()

