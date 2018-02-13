# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogcurves.ui'
#
# Created: Fri Feb  9 13:20:40 2018
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
        self.gridLayout_2 = QtGui.QGridLayout(DialogCurves)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cbDriver = QtGui.QComboBox(DialogCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDriver.sizePolicy().hasHeightForWidth())
        self.cbDriver.setSizePolicy(sizePolicy)
        self.cbDriver.setObjectName(_fromUtf8("cbDriver"))
        self.verticalLayout_2.addWidget(self.cbDriver)
        self.cbSignals = QtGui.QComboBox(DialogCurves)
        self.cbSignals.setObjectName(_fromUtf8("cbSignals"))
        self.verticalLayout_2.addWidget(self.cbSignals)
        self.cbPlotAxis = QtGui.QComboBox(DialogCurves)
        self.cbPlotAxis.setObjectName(_fromUtf8("cbPlotAxis"))
        self.verticalLayout_2.addWidget(self.cbPlotAxis)
        self.btnAdd = QtGui.QPushButton(DialogCurves)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnShift = QtGui.QPushButton(DialogCurves)
        self.btnShift.setObjectName(_fromUtf8("btnShift"))
        self.verticalLayout_2.addWidget(self.btnShift)
        self.btnRemove = QtGui.QPushButton(DialogCurves)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.verticalLayout_2.addWidget(self.btnRemove)
        self.listCurves = QtGui.QListWidget(DialogCurves)
        self.listCurves.setObjectName(_fromUtf8("listCurves"))
        self.verticalLayout_2.addWidget(self.listCurves)
        self.btnCLoop = QtGui.QPushButton(DialogCurves)
        self.btnCLoop.setObjectName(_fromUtf8("btnCLoop"))
        self.verticalLayout_2.addWidget(self.btnCLoop)
        self.btnCurrents = QtGui.QPushButton(DialogCurves)
        self.btnCurrents.setObjectName(_fromUtf8("btnCurrents"))
        self.verticalLayout_2.addWidget(self.btnCurrents)
        self.btnPause = QtGui.QPushButton(DialogCurves)
        self.btnPause.setObjectName(_fromUtf8("btnPause"))
        self.verticalLayout_2.addWidget(self.btnPause)
        self.btnClear = QtGui.QPushButton(DialogCurves)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.verticalLayout_2.addWidget(self.btnClear)
        self.btnAutoRange = QtGui.QPushButton(DialogCurves)
        self.btnAutoRange.setObjectName(_fromUtf8("btnAutoRange"))
        self.verticalLayout_2.addWidget(self.btnAutoRange)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_2.setColumnMinimumWidth(0, 40)

        self.retranslateUi(DialogCurves)
        QtCore.QMetaObject.connectSlotsByName(DialogCurves)

    def retranslateUi(self, DialogCurves):
        DialogCurves.setWindowTitle(_translate("DialogCurves", "Dummy Window Title", None))
        self.btnAdd.setText(_translate("DialogCurves", "Add", None))
        self.btnShift.setText(_translate("DialogCurves", "Shift", None))
        self.btnRemove.setText(_translate("DialogCurves", "Remove", None))
        self.btnCLoop.setText(_translate("DialogCurves", "CLoop", None))
        self.btnCurrents.setText(_translate("DialogCurves", "Currents", None))
        self.btnPause.setText(_translate("DialogCurves", "Pause", None))
        self.btnClear.setText(_translate("DialogCurves", "Clear", None))
        self.btnAutoRange.setText(_translate("DialogCurves", "Autorange Ys", None))

