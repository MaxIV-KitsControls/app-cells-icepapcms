# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogstatusinfo.ui'
#
# Created: Thu Jan 11 14:10:22 2018
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
        DialogStatusInfo.resize(428, 278)
        self.textBrowser = QtGui.QTextBrowser(DialogStatusInfo)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 411, 221))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.widget = QtGui.QWidget(DialogStatusInfo)
        self.widget.setGeometry(QtCore.QRect(10, 240, 411, 30))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnUpdate = QtGui.QPushButton(self.widget)
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnRegReset = QtGui.QPushButton(self.widget)
        self.btnRegReset.setObjectName(_fromUtf8("btnRegReset"))
        self.horizontalLayout.addWidget(self.btnRegReset)

        self.retranslateUi(DialogStatusInfo)
        QtCore.QMetaObject.connectSlotsByName(DialogStatusInfo)

    def retranslateUi(self, DialogStatusInfo):
        DialogStatusInfo.setWindowTitle(_translate("DialogStatusInfo", "Status Info", None))
        self.btnUpdate.setText(_translate("DialogStatusInfo", "Update", None))
        self.btnRegReset.setText(_translate("DialogStatusInfo", "Reset Registry", None))

