# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closedloop.ui'
#
# Created: Mon Jan 22 17:46:45 2018
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

class Ui_closedloop(object):
    def setupUi(self, closedloop):
        closedloop.setObjectName(_fromUtf8("closedloop"))
        closedloop.resize(409, 397)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(closedloop.sizePolicy().hasHeightForWidth())
        closedloop.setSizePolicy(sizePolicy)
        closedloop.setMinimumSize(QtCore.QSize(409, 397))
        self.gridlayout = QtGui.QGridLayout(closedloop)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.closedloop_frame = QtGui.QFrame(closedloop)
        self.closedloop_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.closedloop_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.closedloop_frame.setObjectName(_fromUtf8("closedloop_frame"))
        self.gridLayout = QtGui.QGridLayout(self.closedloop_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.closedloop_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setContentsMargins(20, -1, -1, -1)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 16))
        self.label.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.cfgPCLOOP = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLOOP.sizePolicy().hasHeightForWidth())
        self.cfgPCLOOP.setSizePolicy(sizePolicy)
        self.cfgPCLOOP.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgPCLOOP.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLOOP.setObjectName(_fromUtf8("cfgPCLOOP"))
        self.gridlayout1.addWidget(self.cfgPCLOOP, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 16))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout1.addWidget(self.label_3, 1, 0, 1, 1)
        self.cfgPCLTAU = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLTAU.sizePolicy().hasHeightForWidth())
        self.cfgPCLTAU.setSizePolicy(sizePolicy)
        self.cfgPCLTAU.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgPCLTAU.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLTAU.setMaximum(999999999.0)
        self.cfgPCLTAU.setSingleStep(0.01)
        self.cfgPCLTAU.setObjectName(_fromUtf8("cfgPCLTAU"))
        self.gridlayout1.addWidget(self.cfgPCLTAU, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(140, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout1.addWidget(self.label_2, 2, 0, 1, 1)
        self.cfgPCLERROR = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLERROR.sizePolicy().hasHeightForWidth())
        self.cfgPCLERROR.setSizePolicy(sizePolicy)
        self.cfgPCLERROR.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgPCLERROR.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLERROR.setMaximum(999999999)
        self.cfgPCLERROR.setObjectName(_fromUtf8("cfgPCLERROR"))
        self.gridlayout1.addWidget(self.cfgPCLERROR, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(100, 16))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout1.addWidget(self.label_4, 3, 0, 1, 1)
        self.cfgPCLDEADBD = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLDEADBD.sizePolicy().hasHeightForWidth())
        self.cfgPCLDEADBD.setSizePolicy(sizePolicy)
        self.cfgPCLDEADBD.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgPCLDEADBD.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLDEADBD.setMaximum(999999999)
        self.cfgPCLDEADBD.setObjectName(_fromUtf8("cfgPCLDEADBD"))
        self.gridlayout1.addWidget(self.cfgPCLDEADBD, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(100, 16))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout1.addWidget(self.label_6, 4, 0, 1, 1)
        self.cfgPCLSETLW = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLSETLW.sizePolicy().hasHeightForWidth())
        self.cfgPCLSETLW.setSizePolicy(sizePolicy)
        self.cfgPCLSETLW.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgPCLSETLW.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLSETLW.setMaximum(999999999)
        self.cfgPCLSETLW.setObjectName(_fromUtf8("cfgPCLSETLW"))
        self.gridlayout1.addWidget(self.cfgPCLSETLW, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 16))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout1.addWidget(self.label_5, 5, 0, 1, 1)
        self.cfgPCLSETLT = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLSETLT.sizePolicy().hasHeightForWidth())
        self.cfgPCLSETLT.setSizePolicy(sizePolicy)
        self.cfgPCLSETLT.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgPCLSETLT.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLSETLT.setMaximum(1000000000.0)
        self.cfgPCLSETLT.setSingleStep(0.01)
        self.cfgPCLSETLT.setObjectName(_fromUtf8("cfgPCLSETLT"))
        self.gridlayout1.addWidget(self.cfgPCLSETLT, 5, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QtCore.QSize(100, 16))
        self.label_61.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridlayout1.addWidget(self.label_61, 6, 0, 1, 1)
        self.cfgSTRTVEL = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgSTRTVEL.sizePolicy().hasHeightForWidth())
        self.cfgSTRTVEL.setSizePolicy(sizePolicy)
        self.cfgSTRTVEL.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgSTRTVEL.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgSTRTVEL.setMaximum(1000000000.0)
        self.cfgSTRTVEL.setSingleStep(0.01)
        self.cfgSTRTVEL.setObjectName(_fromUtf8("cfgSTRTVEL"))
        self.gridlayout1.addWidget(self.cfgSTRTVEL, 6, 1, 1, 1)
        self.cfgPCLMODE = QtGui.QFrame(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLMODE.sizePolicy().hasHeightForWidth())
        self.cfgPCLMODE.setSizePolicy(sizePolicy)
        self.cfgPCLMODE.setFrameShape(QtGui.QFrame.NoFrame)
        self.cfgPCLMODE.setFrameShadow(QtGui.QFrame.Plain)
        self.cfgPCLMODE.setObjectName(_fromUtf8("cfgPCLMODE"))
        self.verticalLayout = QtGui.QVBoxLayout(self.cfgPCLMODE)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.cfgPCLMODE_SIMPLECHK = QtGui.QCheckBox(self.cfgPCLMODE)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgPCLMODE_SIMPLECHK.sizePolicy().hasHeightForWidth())
        self.cfgPCLMODE_SIMPLECHK.setSizePolicy(sizePolicy)
        self.cfgPCLMODE_SIMPLECHK.setMinimumSize(QtCore.QSize(150, 16))
        self.cfgPCLMODE_SIMPLECHK.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgPCLMODE_SIMPLECHK.setObjectName(_fromUtf8("cfgPCLMODE_SIMPLECHK"))
        self.horizontalLayout_1.addWidget(self.cfgPCLMODE_SIMPLECHK)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.gridlayout1.addWidget(self.cfgPCLMODE, 7, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(65, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.closedloop_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(220, 92))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setSpacing(5)
        self.vboxlayout1.setContentsMargins(-1, 10, -1, -1)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setContentsMargins(20, -1, -1, -1)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(100, 16))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridlayout2.addWidget(self.label_7, 0, 0, 1, 1)
        self.cfgCTRLENC = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgCTRLENC.sizePolicy().hasHeightForWidth())
        self.cfgCTRLENC.setSizePolicy(sizePolicy)
        self.cfgCTRLENC.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgCTRLENC.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgCTRLENC.setObjectName(_fromUtf8("cfgCTRLENC"))
        self.gridlayout2.addWidget(self.cfgCTRLENC, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(145, 16))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridlayout2.addWidget(self.label_8, 1, 0, 1, 1)
        self.cfgCTRLERROR = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgCTRLERROR.sizePolicy().hasHeightForWidth())
        self.cfgCTRLERROR.setSizePolicy(sizePolicy)
        self.cfgCTRLERROR.setMinimumSize(QtCore.QSize(70, 22))
        self.cfgCTRLERROR.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgCTRLERROR.setMaximum(999999999)
        self.cfgCTRLERROR.setObjectName(_fromUtf8("cfgCTRLERROR"))
        self.gridlayout2.addWidget(self.cfgCTRLERROR, 1, 1, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout2)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(65, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 42, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridlayout.addWidget(self.closedloop_frame, 0, 0, 1, 1)

        self.retranslateUi(closedloop)
        QtCore.QMetaObject.connectSlotsByName(closedloop)

    def retranslateUi(self, closedloop):
        closedloop.setWindowTitle(_translate("closedloop", "Dialog", None))
        self.groupBox.setTitle(_translate("closedloop", "Position closed loop", None))
        self.label.setText(_translate("closedloop", "Closed loop encoder", None))
        self.label_3.setText(_translate("closedloop", "Time constant (s)", None))
        self.label_2.setText(_translate("closedloop", "Maximum error (steps)", None))
        self.label_4.setText(_translate("closedloop", "Deadband (steps)", None))
        self.label_6.setText(_translate("closedloop", "Settle window (steps)", None))
        self.label_5.setText(_translate("closedloop", "Settle time (s)", None))
        self.label_61.setText(_translate("closedloop", "Max regulation speed (steps/s)", None))
        self.cfgPCLMODE_SIMPLECHK.setText(_translate("closedloop", "Simple check mode", None))
        self.groupBox_2.setTitle(_translate("closedloop", "Position control", None))
        self.label_7.setText(_translate("closedloop", "Control encoder", None))
        self.label_8.setText(_translate("closedloop", "Maximum error (steps)", None))

