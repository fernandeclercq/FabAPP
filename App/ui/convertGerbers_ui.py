# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConvertGerbers_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConvertGerbersDialog(object):
    def setupUi(self, ConvertGerbersDialog):
        ConvertGerbersDialog.setObjectName("ConvertGerbersDialog")
        ConvertGerbersDialog.resize(1024, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConvertGerbersDialog.sizePolicy().hasHeightForWidth())
        ConvertGerbersDialog.setSizePolicy(sizePolicy)
        ConvertGerbersDialog.setMinimumSize(QtCore.QSize(1024, 470))
        ConvertGerbersDialog.setMaximumSize(QtCore.QSize(1024, 470))
        ConvertGerbersDialog.setStyleSheet("QLabel > lblConvertGerbers{\n"
"\n"
"border: 4px dashed #aaa;\n"
"\n"
"}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(ConvertGerbersDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ledImportGerbers = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ledImportGerbers.setObjectName("ledImportGerbers")
        self.horizontalLayout.addWidget(self.ledImportGerbers)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnImportGerbers = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnImportGerbers.setObjectName("btnImportGerbers")
        self.horizontalLayout.addWidget(self.btnImportGerbers)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnRemoveGerbers = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRemoveGerbers.setObjectName("btnRemoveGerbers")
        self.horizontalLayout.addWidget(self.btnRemoveGerbers)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(ConvertGerbersDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 350, 1001, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.ledExportGerberPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.ledExportGerberPath.setObjectName("ledExportGerberPath")
        self.horizontalLayout_2.addWidget(self.ledExportGerberPath)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.btnExportGerbers = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExportGerbers.sizePolicy().hasHeightForWidth())
        self.btnExportGerbers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnExportGerbers.setFont(font)
        self.btnExportGerbers.setStyleSheet("padding: 10px")
        self.btnExportGerbers.setObjectName("btnExportGerbers")
        self.horizontalLayout_2.addWidget(self.btnExportGerbers)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(ConvertGerbersDialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 400, 1001, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.btnRenameGerbers = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnRenameGerbers.setFont(font)
        self.btnRenameGerbers.setObjectName("btnRenameGerbers")
        self.horizontalLayout_3.addWidget(self.btnRenameGerbers)
        spacerItem8 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayoutWidget = QtWidgets.QWidget(ConvertGerbersDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 1001, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblConvertGerbersDisplayChanges = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblConvertGerbersDisplayChanges.setFont(font)
        self.lblConvertGerbersDisplayChanges.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConvertGerbersDisplayChanges.setObjectName("lblConvertGerbersDisplayChanges")
        self.verticalLayout.addWidget(self.lblConvertGerbersDisplayChanges)
        self.lblConvertGerbers = QtWidgets.QLabel(ConvertGerbersDialog)
        self.lblConvertGerbers.setEnabled(True)
        self.lblConvertGerbers.setGeometry(QtCore.QRect(10, 230, 198, 99))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblConvertGerbers.setFont(font)
        self.lblConvertGerbers.setStyleSheet("QLabel {\n"
"    border: 4px dashed #aaa\n"
" }")
        self.lblConvertGerbers.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConvertGerbers.setObjectName("lblConvertGerbers")

        self.retranslateUi(ConvertGerbersDialog)
        QtCore.QMetaObject.connectSlotsByName(ConvertGerbersDialog)

    def retranslateUi(self, ConvertGerbersDialog):
        _translate = QtCore.QCoreApplication.translate
        ConvertGerbersDialog.setWindowTitle(_translate("ConvertGerbersDialog", "Convert Gerbers"))
        self.ledImportGerbers.setPlaceholderText(_translate("ConvertGerbersDialog", "Import the zip-file containing the gerbers or drag-and-drop the zip-file"))
        self.btnImportGerbers.setText(_translate("ConvertGerbersDialog", "Import..."))
        self.btnRemoveGerbers.setText(_translate("ConvertGerbersDialog", "Remove...."))
        self.ledExportGerberPath.setPlaceholderText(_translate("ConvertGerbersDialog", "Select a destination folder to export converted gerber files...."))
        self.btnExportGerbers.setText(_translate("ConvertGerbersDialog", "Select export folder"))
        self.btnRenameGerbers.setText(_translate("ConvertGerbersDialog", "Rename\n"
"Layers"))
        self.lblConvertGerbersDisplayChanges.setText(_translate("ConvertGerbersDialog", "No gerbers were imported yet...."))
        self.lblConvertGerbers.setText(_translate("ConvertGerbersDialog", "<html><head/><body><p>Drag and drop </p><p>compressed gerber files here</p></body></html>"))
