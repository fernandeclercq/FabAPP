# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowDialog(object):
    def setupUi(self, MainWindowDialog):
        MainWindowDialog.setObjectName("MainWindowDialog")
        MainWindowDialog.resize(457, 147)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowDialog.sizePolicy().hasHeightForWidth())
        MainWindowDialog.setSizePolicy(sizePolicy)
        MainWindowDialog.setMinimumSize(QtCore.QSize(457, 147))
        MainWindowDialog.setMaximumSize(QtCore.QSize(457, 147))
        MainWindowDialog.setSizeGripEnabled(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindowDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnConvertGrb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnConvertGrb.setMinimumSize(QtCore.QSize(207, 77))
        self.btnConvertGrb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnConvertGrb.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnConvertGrb.setFont(font)
        self.btnConvertGrb.setObjectName("btnConvertGrb")
        self.horizontalLayout.addWidget(self.btnConvertGrb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnGenerateNeodenFile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnGenerateNeodenFile.setMinimumSize(QtCore.QSize(184, 77))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnGenerateNeodenFile.setFont(font)
        self.btnGenerateNeodenFile.setObjectName("btnGenerateNeodenFile")
        self.horizontalLayout.addWidget(self.btnGenerateNeodenFile)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(MainWindowDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindowDialog)

    def retranslateUi(self, MainWindowDialog):
        _translate = QtCore.QCoreApplication.translate
        MainWindowDialog.setWindowTitle(_translate("MainWindowDialog", "Main Windows"))
        self.btnConvertGrb.setText(_translate("MainWindowDialog", "Convert\n"
"Geber\n"
"Files"))
        self.btnGenerateNeodenFile.setText(_translate("MainWindowDialog", "Generate\n"
"Pick and Place\n"
"File"))
