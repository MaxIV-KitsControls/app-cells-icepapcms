# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor.ui'
#
# Created: Fri Jan 19 16:32:07 2018
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

class Ui_motor(object):
    def setupUi(self, motor):
        motor.setObjectName(_fromUtf8("motor"))
        motor.resize(477, 470)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(motor.sizePolicy().hasHeightForWidth())
        motor.setSizePolicy(sizePolicy)
        motor.setMinimumSize(QtCore.QSize(477, 470))
        self.gridlayout = QtGui.QGridLayout(motor)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.motor_frame = QtGui.QFrame(motor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motor_frame.sizePolicy().hasHeightForWidth())
        self.motor_frame.setSizePolicy(sizePolicy)
        self.motor_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.motor_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.motor_frame.setObjectName(_fromUtf8("motor_frame"))
        self.gridLayout = QtGui.QGridLayout(self.motor_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.motor_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 115))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(80, 22))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(110, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.cfgMOTPHASES = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgMOTPHASES.sizePolicy().hasHeightForWidth())
        self.cfgMOTPHASES.setSizePolicy(sizePolicy)
        self.cfgMOTPHASES.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgMOTPHASES.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgMOTPHASES.setObjectName(_fromUtf8("cfgMOTPHASES"))
        self.hboxlayout.addWidget(self.cfgMOTPHASES)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(110, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hboxlayout1.addWidget(self.label_2)
        self.cfgMOTPOLES = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgMOTPOLES.sizePolicy().hasHeightForWidth())
        self.cfgMOTPOLES.setSizePolicy(sizePolicy)
        self.cfgMOTPOLES.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgMOTPOLES.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgMOTPOLES.setMaximum(999999999)
        self.cfgMOTPOLES.setObjectName(_fromUtf8("cfgMOTPOLES"))
        self.hboxlayout1.addWidget(self.cfgMOTPOLES)
        self.verticalLayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(110, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.hboxlayout2.addWidget(self.label_3)
        self.cfgMREGMODE = QtGui.QComboBox(self.groupBox)
        self.cfgMREGMODE.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgMREGMODE.setObjectName(_fromUtf8("cfgMREGMODE"))
        self.hboxlayout2.addWidget(self.cfgMREGMODE)
        self.verticalLayout.addLayout(self.hboxlayout2)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName(_fromUtf8("hboxlayout3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(150, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.hboxlayout3.addWidget(self.label_4)
        self.cfgNRES = QtGui.QDoubleSpinBox(self.groupBox)
        self.cfgNRES.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgNRES.setMaximum(999999999.0)
        self.cfgNRES.setSingleStep(0.01)
        self.cfgNRES.setObjectName(_fromUtf8("cfgNRES"))
        self.hboxlayout3.addWidget(self.cfgNRES)
        self.verticalLayout.addLayout(self.hboxlayout3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.motor_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(166, 96))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout.setContentsMargins(15, 5, -1, -1)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName(_fromUtf8("hboxlayout4"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(33, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.hboxlayout4.addWidget(self.label_10)
        self.cfgCURRGAIN = QtGui.QComboBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgCURRGAIN.sizePolicy().hasHeightForWidth())
        self.cfgCURRGAIN.setSizePolicy(sizePolicy)
        self.cfgCURRGAIN.setMinimumSize(QtCore.QSize(110, 22))
        self.cfgCURRGAIN.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgCURRGAIN.setObjectName(_fromUtf8("cfgCURRGAIN"))
        self.hboxlayout4.addWidget(self.cfgCURRGAIN)
        self.vboxlayout.addLayout(self.hboxlayout4)
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setContentsMargins(10, -1, -1, -1)
        self.hboxlayout5.setObjectName(_fromUtf8("hboxlayout5"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(60, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.hboxlayout5.addWidget(self.label_11)
        self.cfgMREGP = QtGui.QDoubleSpinBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgMREGP.sizePolicy().hasHeightForWidth())
        self.cfgMREGP.setSizePolicy(sizePolicy)
        self.cfgMREGP.setMinimumSize(QtCore.QSize(60, 22))
        self.cfgMREGP.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgMREGP.setMaximum(999999999.0)
        self.cfgMREGP.setSingleStep(0.01)
        self.cfgMREGP.setObjectName(_fromUtf8("cfgMREGP"))
        self.hboxlayout5.addWidget(self.cfgMREGP)
        self.vboxlayout.addLayout(self.hboxlayout5)
        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setContentsMargins(10, -1, -1, -1)
        self.hboxlayout6.setObjectName(_fromUtf8("hboxlayout6"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(60, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.hboxlayout6.addWidget(self.label_12)
        self.cfgMREGI = QtGui.QDoubleSpinBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgMREGI.sizePolicy().hasHeightForWidth())
        self.cfgMREGI.setSizePolicy(sizePolicy)
        self.cfgMREGI.setMinimumSize(QtCore.QSize(60, 22))
        self.cfgMREGI.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgMREGI.setMaximum(999999999.0)
        self.cfgMREGI.setSingleStep(0.01)
        self.cfgMREGI.setObjectName(_fromUtf8("cfgMREGI"))
        self.hboxlayout6.addWidget(self.cfgMREGI)
        self.vboxlayout.addLayout(self.hboxlayout6)
        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setContentsMargins(10, -1, -1, -1)
        self.hboxlayout7.setObjectName(_fromUtf8("hboxlayout7"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(60, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.hboxlayout7.addWidget(self.label_13)
        self.cfgMREGD = QtGui.QDoubleSpinBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgMREGD.sizePolicy().hasHeightForWidth())
        self.cfgMREGD.setSizePolicy(sizePolicy)
        self.cfgMREGD.setMinimumSize(QtCore.QSize(60, 22))
        self.cfgMREGD.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgMREGD.setMaximum(999999999.0)
        self.cfgMREGD.setSingleStep(0.01)
        self.cfgMREGD.setObjectName(_fromUtf8("cfgMREGD"))
        self.hboxlayout7.addWidget(self.cfgMREGD)
        self.vboxlayout.addLayout(self.hboxlayout7)
        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.motor_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(250, 60))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setContentsMargins(-1, 5, -1, -1)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName(_fromUtf8("hboxlayout8"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(110, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.hboxlayout8.addWidget(self.label_5)
        self.cfgNVOLT = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgNVOLT.sizePolicy().hasHeightForWidth())
        self.cfgNVOLT.setSizePolicy(sizePolicy)
        self.cfgNVOLT.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgNVOLT.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgNVOLT.setMaximum(999999999.0)
        self.cfgNVOLT.setSingleStep(0.01)
        self.cfgNVOLT.setObjectName(_fromUtf8("cfgNVOLT"))
        self.hboxlayout8.addWidget(self.cfgNVOLT)
        self.vboxlayout1.addLayout(self.hboxlayout8)
        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName(_fromUtf8("hboxlayout9"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(110, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.hboxlayout9.addWidget(self.label_6)
        self.cfgIVOLT = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgIVOLT.sizePolicy().hasHeightForWidth())
        self.cfgIVOLT.setSizePolicy(sizePolicy)
        self.cfgIVOLT.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgIVOLT.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgIVOLT.setMaximum(999999999.0)
        self.cfgIVOLT.setSingleStep(0.01)
        self.cfgIVOLT.setObjectName(_fromUtf8("cfgIVOLT"))
        self.hboxlayout9.addWidget(self.cfgIVOLT)
        self.vboxlayout1.addLayout(self.hboxlayout9)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(215, 43, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.motor_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(250, 75))
        self.groupBox_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout2.setContentsMargins(-1, 5, -1, -1)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.hboxlayout10 = QtGui.QHBoxLayout()
        self.hboxlayout10.setObjectName(_fromUtf8("hboxlayout10"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(140, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.hboxlayout10.addWidget(self.label_7)
        self.cfgNCURR = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgNCURR.sizePolicy().hasHeightForWidth())
        self.cfgNCURR.setSizePolicy(sizePolicy)
        self.cfgNCURR.setMinimumSize(QtCore.QSize(45, 22))
        self.cfgNCURR.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgNCURR.setMaximum(999999999.0)
        self.cfgNCURR.setSingleStep(0.01)
        self.cfgNCURR.setObjectName(_fromUtf8("cfgNCURR"))
        self.hboxlayout10.addWidget(self.cfgNCURR)
        self.vboxlayout2.addLayout(self.hboxlayout10)
        self.hboxlayout11 = QtGui.QHBoxLayout()
        self.hboxlayout11.setObjectName(_fromUtf8("hboxlayout11"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(160, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.hboxlayout11.addWidget(self.label_8)
        self.cfgICURR = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgICURR.sizePolicy().hasHeightForWidth())
        self.cfgICURR.setSizePolicy(sizePolicy)
        self.cfgICURR.setMinimumSize(QtCore.QSize(45, 22))
        self.cfgICURR.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgICURR.setMaximum(999999999)
        self.cfgICURR.setObjectName(_fromUtf8("cfgICURR"))
        self.hboxlayout11.addWidget(self.cfgICURR)
        self.vboxlayout2.addLayout(self.hboxlayout11)
        self.hboxlayout12 = QtGui.QHBoxLayout()
        self.hboxlayout12.setObjectName(_fromUtf8("hboxlayout12"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(210, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.hboxlayout12.addWidget(self.label_9)
        self.cfgBCURR = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgBCURR.sizePolicy().hasHeightForWidth())
        self.cfgBCURR.setSizePolicy(sizePolicy)
        self.cfgBCURR.setMinimumSize(QtCore.QSize(45, 22))
        self.cfgBCURR.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgBCURR.setMaximum(999999999)
        self.cfgBCURR.setObjectName(_fromUtf8("cfgBCURR"))
        self.hboxlayout12.addWidget(self.cfgBCURR)
        self.vboxlayout2.addLayout(self.hboxlayout12)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(229, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.gridlayout.addWidget(self.motor_frame, 0, 0, 1, 1)

        self.retranslateUi(motor)
        QtCore.QMetaObject.connectSlotsByName(motor)

    def retranslateUi(self, motor):
        motor.setWindowTitle(_translate("motor", "Dialog", None))
        self.groupBox.setTitle(_translate("motor", "Motor type", None))
        self.label.setText(_translate("motor", "Number of phases", None))
        self.label_2.setText(_translate("motor", "Number of pole pairs", None))
        self.label_3.setText(_translate("motor", "Regulation mode", None))
        self.label_4.setText(_translate("motor", "Phase resistance (ohms)", None))
        self.groupBox_4.setTitle(_translate("motor", "Current regulation (PID)", None))
        self.label_10.setText(_translate("motor", "Gain:", None))
        self.label_11.setText(_translate("motor", "Proportional", None))
        self.label_12.setText(_translate("motor", "Integral", None))
        self.label_13.setText(_translate("motor", "Derivative", None))
        self.groupBox_2.setTitle(_translate("motor", "Working voltages", None))
        self.label_5.setText(_translate("motor", "Nominal Voltage (V)", None))
        self.label_6.setText(_translate("motor", "Idle voltage (V)", None))
        self.groupBox_3.setTitle(_translate("motor", "Motor current", None))
        self.label_7.setText(_translate("motor", "Nominal current (A)", None))
        self.label_8.setText(_translate("motor", "Idle current (% of nominal)", None))
        self.label_9.setText(_translate("motor", "Boost overcurrent (% of nominal)", None))

