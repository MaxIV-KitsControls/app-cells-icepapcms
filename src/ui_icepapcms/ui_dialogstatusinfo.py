# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogstatusinfo.ui'
#
# Created: Mon Jan 22 17:46:46 2018
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogStatusInfo(object):
    def setupUi(self, DialogStatusInfo):
        DialogStatusInfo.setObjectName(_fromUtf8("DialogStatusInfo"))
        DialogStatusInfo.resize(428, 550)
        self.textBrowser = QtGui.QTextBrowser(DialogStatusInfo)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 411, 451))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.layoutWidget = QtGui.QWidget(DialogStatusInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 510, 411, 34))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnUpdate = QtGui.QPushButton(self.layoutWidget)
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnEsync = QtGui.QPushButton(self.layoutWidget)
        self.btnEsync.setObjectName(_fromUtf8("btnEsync"))
        self.horizontalLayout.addWidget(self.btnEsync)
        self.txt1Command = QtGui.QLineEdit(self.layoutWidget)
        self.txt1Command.setObjectName(_fromUtf8("txt1Command"))
        self.horizontalLayout.addWidget(self.txt1Command)

        self.retranslateUi(DialogStatusInfo)
        QtCore.QMetaObject.connectSlotsByName(DialogStatusInfo)

    def retranslateUi(self, DialogStatusInfo):
        DialogStatusInfo.setWindowTitle(_translate("DialogStatusInfo", "Status Info", None))
        self.btnUpdate.setText(_translate("DialogStatusInfo", "VSTATUS", None))
        self.btnEsync.setText(_translate("DialogStatusInfo", "ESYNC", None))

