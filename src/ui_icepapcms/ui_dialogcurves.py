# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogcurves.ui'
#
# Created: Tue Jan 23 13:45:20 2018
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

class Ui_DialogCurves(object):
    def setupUi(self, DialogCurves):
        DialogCurves.setObjectName(_fromUtf8("DialogCurves"))
        DialogCurves.resize(641, 666)
        DialogCurves.setMinimumSize(QtCore.QSize(50, 0))
        self.gridLayoutWidget = QtGui.QWidget(DialogCurves)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 651))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnPause = QtGui.QPushButton(DialogCurves)
        self.btnPause.setGeometry(QtCore.QRect(510, 630, 121, 28))
        self.btnPause.setObjectName(_fromUtf8("btnPause"))
        self.verticalLayoutWidget = QtGui.QWidget(DialogCurves)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 0, 121, 411))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cbDriver = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cbDriver.setObjectName(_fromUtf8("cbDriver"))
        self.verticalLayout_2.addWidget(self.cbDriver)
        self.cbSignals = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cbSignals.setObjectName(_fromUtf8("cbSignals"))
        self.verticalLayout_2.addWidget(self.cbSignals)
        self.cbPlotAxis = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cbPlotAxis.setObjectName(_fromUtf8("cbPlotAxis"))
        self.verticalLayout_2.addWidget(self.cbPlotAxis)
        self.btnAdd = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnShift = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnShift.setObjectName(_fromUtf8("btnShift"))
        self.verticalLayout_2.addWidget(self.btnShift)
        self.btnRemove = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.verticalLayout_2.addWidget(self.btnRemove)
        self.listCurves = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listCurves.setObjectName(_fromUtf8("listCurves"))
        self.verticalLayout_2.addWidget(self.listCurves)
        self.btnCLoop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCLoop.setObjectName(_fromUtf8("btnCLoop"))
        self.verticalLayout_2.addWidget(self.btnCLoop)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(DialogCurves)
        QtCore.QMetaObject.connectSlotsByName(DialogCurves)

    def retranslateUi(self, DialogCurves):
        DialogCurves.setWindowTitle(_translate("DialogCurves", "Dummy Window Title", None))
        self.btnPause.setText(_translate("DialogCurves", "Pause", None))
        self.btnAdd.setText(_translate("DialogCurves", "Add", None))
        self.btnShift.setText(_translate("DialogCurves", "Shift", None))
        self.btnRemove.setText(_translate("DialogCurves", "Remove", None))
        self.btnCLoop.setText(_translate("DialogCurves", "CLoop", None))

