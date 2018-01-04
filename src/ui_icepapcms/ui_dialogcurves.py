# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogcurves.ui'
#
# Created: Tue Jan  2 09:37:31 2018
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
        DialogCurves.resize(641, 382)
        DialogCurves.setMinimumSize(QtCore.QSize(50, 0))
        self.gridLayoutWidget = QtGui.QWidget(DialogCurves)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 361))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBoxResolution = QtGui.QGroupBox(DialogCurves)
        self.groupBoxResolution.setGeometry(QtCore.QRect(509, 10, 121, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxResolution.sizePolicy().hasHeightForWidth())
        self.groupBoxResolution.setSizePolicy(sizePolicy)
        self.groupBoxResolution.setObjectName(_fromUtf8("groupBoxResolution"))
        self.radioButtonAxis = QtGui.QRadioButton(self.groupBoxResolution)
        self.radioButtonAxis.setGeometry(QtCore.QRect(10, 20, 109, 25))
        self.radioButtonAxis.setChecked(True)
        self.radioButtonAxis.setObjectName(_fromUtf8("radioButtonAxis"))
        self.radioButtonEncoder = QtGui.QRadioButton(self.groupBoxResolution)
        self.radioButtonEncoder.setGeometry(QtCore.QRect(10, 40, 109, 25))
        self.radioButtonEncoder.setObjectName(_fromUtf8("radioButtonEncoder"))
        self.groupBoxCurves = QtGui.QGroupBox(DialogCurves)
        self.groupBoxCurves.setGeometry(QtCore.QRect(510, 90, 121, 281))
        self.groupBoxCurves.setObjectName(_fromUtf8("groupBoxCurves"))
        self.checkBoxDelta2 = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxDelta2.setGeometry(QtCore.QRect(10, 262, 119, 17))
        self.checkBoxDelta2.setObjectName(_fromUtf8("checkBoxDelta2"))
        self.checkBoxMeasure = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxMeasure.setGeometry(QtCore.QRect(10, 170, 119, 17))
        self.checkBoxMeasure.setObjectName(_fromUtf8("checkBoxMeasure"))
        self.checkBoxDelta1 = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxDelta1.setGeometry(QtCore.QRect(10, 239, 119, 17))
        self.checkBoxDelta1.setObjectName(_fromUtf8("checkBoxDelta1"))
        self.checkBoxTgtEnc = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxTgtEnc.setGeometry(QtCore.QRect(10, 77, 119, 17))
        self.checkBoxTgtEnc.setObjectName(_fromUtf8("checkBoxTgtEnc"))
        self.checkBoxMotor = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxMotor.setGeometry(QtCore.QRect(10, 216, 119, 17))
        self.checkBoxMotor.setObjectName(_fromUtf8("checkBoxMotor"))
        self.checkBoxShiftEnc = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxShiftEnc.setGeometry(QtCore.QRect(10, 54, 119, 17))
        self.checkBoxShiftEnc.setObjectName(_fromUtf8("checkBoxShiftEnc"))
        self.checkBoxAbsEnc = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxAbsEnc.setGeometry(QtCore.QRect(10, 146, 119, 18))
        self.checkBoxAbsEnc.setObjectName(_fromUtf8("checkBoxAbsEnc"))
        self.checkBoxInPos = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxInPos.setGeometry(QtCore.QRect(10, 123, 119, 17))
        self.checkBoxInPos.setObjectName(_fromUtf8("checkBoxInPos"))
        self.checkBoxAxis = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxAxis.setGeometry(QtCore.QRect(10, 30, 119, 18))
        self.checkBoxAxis.setObjectName(_fromUtf8("checkBoxAxis"))
        self.checkBoxCtrlEnc = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxCtrlEnc.setGeometry(QtCore.QRect(10, 193, 119, 17))
        self.checkBoxCtrlEnc.setObjectName(_fromUtf8("checkBoxCtrlEnc"))
        self.checkBoxEncIn = QtGui.QCheckBox(self.groupBoxCurves)
        self.checkBoxEncIn.setGeometry(QtCore.QRect(10, 100, 119, 17))
        self.checkBoxEncIn.setObjectName(_fromUtf8("checkBoxEncIn"))

        self.retranslateUi(DialogCurves)
        QtCore.QMetaObject.connectSlotsByName(DialogCurves)

    def retranslateUi(self, DialogCurves):
        DialogCurves.setWindowTitle(_translate("DialogCurves", "Dummy Window Title", None))
        self.groupBoxResolution.setTitle(_translate("DialogCurves", "Resolution", None))
        self.radioButtonAxis.setText(_translate("DialogCurves", "Axis", None))
        self.radioButtonEncoder.setText(_translate("DialogCurves", "Encoder", None))
        self.groupBoxCurves.setTitle(_translate("DialogCurves", "Select Curves", None))
        self.checkBoxDelta2.setText(_translate("DialogCurves", "Axis - Motor", None))
        self.checkBoxMeasure.setText(_translate("DialogCurves", "Measure", None))
        self.checkBoxDelta1.setText(_translate("DialogCurves", "Axis - TgtEnc", None))
        self.checkBoxTgtEnc.setText(_translate("DialogCurves", "TgtEnc", None))
        self.checkBoxMotor.setText(_translate("DialogCurves", "Motor", None))
        self.checkBoxShiftEnc.setText(_translate("DialogCurves", "ShftEnc", None))
        self.checkBoxAbsEnc.setText(_translate("DialogCurves", "AbsEnc", None))
        self.checkBoxInPos.setText(_translate("DialogCurves", "InPos", None))
        self.checkBoxAxis.setText(_translate("DialogCurves", "Axis", None))
        self.checkBoxCtrlEnc.setText(_translate("DialogCurves", "CtrlEnc", None))
        self.checkBoxEncIn.setText(_translate("DialogCurves", "EncIn", None))

