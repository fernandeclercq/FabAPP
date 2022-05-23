# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateNeodenFile_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GenerateNeodenConfigDialog(object):
    def setupUi(self, GenerateNeodenConfigDialog):
        GenerateNeodenConfigDialog.setObjectName("GenerateNeodenConfigDialog")
        GenerateNeodenConfigDialog.resize(1024, 535)
        GenerateNeodenConfigDialog.setMinimumSize(QtCore.QSize(100, 100))
        GenerateNeodenConfigDialog.setMaximumSize(QtCore.QSize(1024, 768))
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(GenerateNeodenConfigDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1021, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ledImportPositionFilePath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.ledImportPositionFilePath.setObjectName("ledImportPositionFilePath")
        self.horizontalLayout_2.addWidget(self.ledImportPositionFilePath)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnImportPositionFile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnImportPositionFile.setFont(font)
        self.btnImportPositionFile.setObjectName("btnImportPositionFile")
        self.horizontalLayout_2.addWidget(self.btnImportPositionFile)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnRemovePositionFile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnRemovePositionFile.setObjectName("btnRemovePositionFile")
        self.horizontalLayout_2.addWidget(self.btnRemovePositionFile)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(GenerateNeodenConfigDialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 500, 1021, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.ledFilesOutputDirectory = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.ledFilesOutputDirectory.setObjectName("ledFilesOutputDirectory")
        self.horizontalLayout_4.addWidget(self.ledFilesOutputDirectory)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.btnOutputFolderDirectory = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btnOutputFolderDirectory.setObjectName("btnOutputFolderDirectory")
        self.horizontalLayout_4.addWidget(self.btnOutputFolderDirectory)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.btnGenerateNeodenConfig = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerateNeodenConfig.setFont(font)
        self.btnGenerateNeodenConfig.setObjectName("btnGenerateNeodenConfig")
        self.horizontalLayout_4.addWidget(self.btnGenerateNeodenConfig)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayoutWidget = QtWidgets.QWidget(GenerateNeodenConfigDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 1021, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.twContainerTabs = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.twContainerTabs.setObjectName("twContainerTabs")
        self.tbFrontComponents = QtWidgets.QWidget()
        self.tbFrontComponents.setObjectName("tbFrontComponents")
        self.tableTopComponents = QtWidgets.QTableWidget(self.tbFrontComponents)
        self.tableTopComponents.setGeometry(QtCore.QRect(0, 0, 1011, 421))
        self.tableTopComponents.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableTopComponents.setRowCount(0)
        self.tableTopComponents.setObjectName("tableTopComponents")
        self.tableTopComponents.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTopComponents.setHorizontalHeaderItem(8, item)
        self.twContainerTabs.addTab(self.tbFrontComponents, "")
        self.tbBackComponents = QtWidgets.QWidget()
        self.tbBackComponents.setObjectName("tbBackComponents")
        self.tableBottomComponents = QtWidgets.QTableWidget(self.tbBackComponents)
        self.tableBottomComponents.setGeometry(QtCore.QRect(0, 0, 1011, 421))
        self.tableBottomComponents.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableBottomComponents.setObjectName("tableBottomComponents")
        self.tableBottomComponents.setColumnCount(9)
        self.tableBottomComponents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBottomComponents.setHorizontalHeaderItem(8, item)
        self.twContainerTabs.addTab(self.tbBackComponents, "")
        self.verticalLayout.addWidget(self.twContainerTabs)

        self.retranslateUi(GenerateNeodenConfigDialog)
        self.twContainerTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GenerateNeodenConfigDialog)

    def retranslateUi(self, GenerateNeodenConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        GenerateNeodenConfigDialog.setWindowTitle(_translate("GenerateNeodenConfigDialog", "Generate Neoden4 Config"))
        self.ledImportPositionFilePath.setPlaceholderText(_translate("GenerateNeodenConfigDialog", "Look for your position file or drag and drop position file to this window...."))
        self.btnImportPositionFile.setText(_translate("GenerateNeodenConfigDialog", "Import..."))
        self.btnRemovePositionFile.setText(_translate("GenerateNeodenConfigDialog", "Remove..."))
        self.ledFilesOutputDirectory.setPlaceholderText(_translate("GenerateNeodenConfigDialog", "Define the output directory for the Neoden Config File..."))
        self.btnOutputFolderDirectory.setText(_translate("GenerateNeodenConfigDialog", "Output folder..."))
        self.btnGenerateNeodenConfig.setText(_translate("GenerateNeodenConfigDialog", "Generate Neoden 4 Config"))
        item = self.tableTopComponents.horizontalHeaderItem(0)
        item.setText(_translate("GenerateNeodenConfigDialog", "Feeder #"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the feeder number from 1 to 48 for normal feeders.</p><p>From 49 to 98 to use Special feeders.</p><p>&quot;Special feeders&quot; are:</p><p> - Cut reel-tape</p><p> - Waffer Trays</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the feeder number from 1 to 48 for normal feeders.</p><p>From 49 to 98 to use Special feeders.</p><p>&quot;Special feeders&quot; are:</p><p> - Cut reel-tape</p><p> - Waffer Trays</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(1)
        item.setText(_translate("GenerateNeodenConfigDialog", "Nozzle #"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the correct Nozzle number for the component size. </p><p>Nozzle 1 = 0402,0603, 0805</p><p>Nozzle 2 = 1206, 1210, 2512, 3528, 5630</p><p>Nozzle 3 = TQFP, IC\'s</p><p>Nozzle 4 = 5050, SOP-8, SOIC, SOT</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the correct Nozzle number for the component size. </p><p>Nozzle 1 = 0402,0603, 0805</p><p>Nozzle 2 = 1206, 1210, 2512, 3528, 5630</p><p>Nozzle 3 = TQFP, IC\'s</p><p>Nozzle 4 = 5050, SOP-8, SOIC, SOT</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(2)
        item.setText(_translate("GenerateNeodenConfigDialog", "Name"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the name of the component. For example:</p><p>C1 =&gt; Capacitor 1</p><p>R10 =&gt; Resistor 10</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the name of the component. For example:</p><p>C1 =&gt; Capacitor 1</p><p>R10 =&gt; Resistor 10</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(3)
        item.setText(_translate("GenerateNeodenConfigDialog", "Value"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the value of the component. For example:</p><p>100nF, 10k, ESP32, etc</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the value of the component. For example:</p><p>100nF, 10k, ESP32, etc</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(4)
        item.setText(_translate("GenerateNeodenConfigDialog", "Footprint"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the footprint of the Component.</p><p>If this footprint is wrong, select the correct footprint from the list. Example:</p><p>- SOT223-3</p><p>- 0805</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the footprint of the Component.</p><p>If this footprint is wrong, select the correct footprint from the list. Example:</p><p>- SOT223-3</p><p>- 0805</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(5)
        item.setText(_translate("GenerateNeodenConfigDialog", "X Pos"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be X coordinate for the component. For example:</p><p>98.62</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be X coordinate for the component. For example:</p><p>98.62</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(6)
        item.setText(_translate("GenerateNeodenConfigDialog", "Y Pos"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be Y coordinate for the component. For example:</p><p>56.21</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be Y coordinate for the component. For example:</p><p>56.21</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(7)
        item.setText(_translate("GenerateNeodenConfigDialog", "Rotation"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the amount of degrees the component has to be rotated for placement.</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the amount of degrees the component has to be rotated for placement.</p></body></html>"))
        item = self.tableTopComponents.horizontalHeaderItem(8)
        item.setText(_translate("GenerateNeodenConfigDialog", "Skip"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Display &quot;Yes&quot; if component needs to be skipped during the pick&amp;place proccess.</p><p>Select &quot;Yes&quot; if the component needs to be skipped or</p><p>select &quot;No&quot; if the component does not need to be skipped.</p><p>Default value = &quot;No&quot;</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Display &quot;Yes&quot; if component needs to be skipped during the pick&amp;place proccess.</p><p>Select &quot;Yes&quot; if the component needs to be skipped or</p><p>select &quot;No&quot; if the component does not need to be skipped.</p><p>Default value = &quot;No&quot;</p></body></html>"))
        self.twContainerTabs.setTabText(self.twContainerTabs.indexOf(self.tbFrontComponents), _translate("GenerateNeodenConfigDialog", "Components Top Side"))
        item = self.tableBottomComponents.horizontalHeaderItem(0)
        item.setText(_translate("GenerateNeodenConfigDialog", "Feeder #"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the feeder number from 1 to 48 for normal feeders.</p><p>From 49 to 98 to use Special feeders.</p><p>&quot;Special feeders&quot; are:</p><p> - Cut reel-tape</p><p> - Waffer Trays</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the feeder number from 1 to 48 for normal feeders.</p><p>From 49 to 98 to use Special feeders.</p><p>&quot;Special feeders&quot; are:</p><p> - Cut reel-tape</p><p> - Waffer Trays</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(1)
        item.setText(_translate("GenerateNeodenConfigDialog", "Nozzle #"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the correct Nozzle number for the component size. </p><p>Nozzle 1 = 0402,0603, 0805</p><p>Nozzle 2 = 1206, 1210, 2512, 3528, 5630</p><p>Nozzle 3 = TQFP, IC\'s</p><p>Nozzle 4 = 5050, SOP-8, SOIC, SOT</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Select the correct Nozzle number for the component size. </p><p>Nozzle 1 = 0402,0603, 0805</p><p>Nozzle 2 = 1206, 1210, 2512, 3528, 5630</p><p>Nozzle 3 = TQFP, IC\'s</p><p>Nozzle 4 = 5050, SOP-8, SOIC, SOT</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(2)
        item.setText(_translate("GenerateNeodenConfigDialog", "Name"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the name of the component. For example:</p><p>C1 =&gt; Capacitor 1</p><p>R10 =&gt; Resistor 10</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the name of the component. For example:</p><p>C1 =&gt; Capacitor 1</p><p>R10 =&gt; Resistor 10</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(3)
        item.setText(_translate("GenerateNeodenConfigDialog", "Value"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the value of the component. For example:</p><p>100nF, 10k, ESP32, etc</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the value of the component. For example:</p><p>100nF, 10k, ESP32, etc</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(4)
        item.setText(_translate("GenerateNeodenConfigDialog", "Footprint"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the footprint of the Component.</p><p>If this footprint is wrong, select the correct footprint from the list. Example:</p><p>- SOT223-3</p><p>- 0805</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the footprint of the Component.</p><p>If this footprint is wrong, select the correct footprint from the list. Example:</p><p>- SOT223-3</p><p>- 0805</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(5)
        item.setText(_translate("GenerateNeodenConfigDialog", "X Pos"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be X coordinate for the component. For example:</p><p>98.62</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be X coordinate for the component. For example:</p><p>98.62</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(6)
        item.setText(_translate("GenerateNeodenConfigDialog", "Y Pos"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be Y coordinate for the component. For example:</p><p>56.21</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the To-Be Y coordinate for the component. For example:</p><p>56.21</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(7)
        item.setText(_translate("GenerateNeodenConfigDialog", "Rotation"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the amount of degrees the component has to be rotated for placement.</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Displays the amount of degrees the component has to be rotated for placement.</p></body></html>"))
        item = self.tableBottomComponents.horizontalHeaderItem(8)
        item.setText(_translate("GenerateNeodenConfigDialog", "Skip"))
        item.setToolTip(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Display &quot;Yes&quot; if component needs to be skipped during the pick&amp;place proccess.</p><p>Select &quot;Yes&quot; if the component needs to be skipped or</p><p>select &quot;No&quot; if the component does not need to be skipped.</p><p>Default value = &quot;No&quot;</p></body></html>"))
        item.setWhatsThis(_translate("GenerateNeodenConfigDialog", "<html><head/><body><p>Display &quot;Yes&quot; if component needs to be skipped during the pick&amp;place proccess.</p><p>Select &quot;Yes&quot; if the component needs to be skipped or</p><p>select &quot;No&quot; if the component does not need to be skipped.</p><p>Default value = &quot;No&quot;</p></body></html>"))
        self.twContainerTabs.setTabText(self.twContainerTabs.indexOf(self.tbBackComponents), _translate("GenerateNeodenConfigDialog", "Components Bottom Side"))
