from PyQt4 import QtGui, QtCore
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController


class DialogCurves(QtGui.QDialog):

    def __init__(self, parent, systemName, address):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DialogCurves()
        # self.manager = MainManager()
        self.theIcepapController = IcepapController()
        self.icepapSystemName = systemName
        self.icepapAddress = address
        self.connect(self, QtCore.SIGNAL('finished(int)'), parent.removeDialogCurves)
        self.ui.setupUi(self)
        self.show()
        self.pw = pg.PlotWidget()
        self.ui.gridLayout.addWidget(self.pw)
        self.arrayTime = []
        self.arrayPos = []
        self.arrayEnc = []

    def updateCurves(self, timeVal):
        pos_sel = 'Axis'
        enc_sel = 'AbsEnc'
        positionVal = self.theIcepapController.iPaps[self.icepapSystemName].getPositionFromBoard(self.icepapAddress, pos_sel)
        encoderVal = self.theIcepapController.iPaps[self.icepapSystemName].getEncoder(self.icepapAddress, enc_sel)
        myPositionVal = float(positionVal)
        myEncoderVal = float(encoderVal)
        self.arrayTime.append(timeVal)
        self.arrayPos.append(myPositionVal)
        self.arrayEnc.append(myEncoderVal)
        self.pw.plot(y=self.arrayPos, x=self.arrayTime)
        self.pw.plot(y=self.arrayEnc, x=self.arrayTime)
