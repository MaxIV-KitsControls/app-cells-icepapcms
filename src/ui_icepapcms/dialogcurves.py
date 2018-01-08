from PyQt4 import QtGui, QtCore, Qt
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController
import time


class CurveItem():

    def __init__(self, plotWidget, source, myColor, myWidth):
        self.source = source
        self.arrayTime = []
        self.arrayVal = []
        self.curve = plotWidget.plot(x=self.arrayTime, y=self.arrayVal, pen={'color':myColor, 'width':myWidth})


class DialogCurves(QtGui.QDialog):

    def __init__(self, parent, system_name, address):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DialogCurves()
        # self.theIcepapController = IcepapController()
        self.thing = IcepapController().iPaps[system_name]
        # self.thing = self.theIcepapController.iPaps[self.icepapSystemName]
        self.icepapAddress = address
        self.ui.setupUi(self)
        self.setWindowTitle('Curves  |  ' + system_name + '  |  ' + str(self.icepapAddress))  # Use .name if not empty
        self.show()
        self.ac = []  # Active curves
        #self.myList = ['AXIS', 'INDEXER', 'EXTERR', 'SHFTENC', 'TGTENC', 'ENCIN', 'INPOS', 'ABSENC', 'MEASURE', 'PARAM', 'CTRLENC', 'MOTOR']
        self.ticker = Qt.QTimer(self)
        self.tickInterval = 100  # [milliseconds]
        self.xTimeLength = 60  # [seconds]
        self.numVisible = self.xTimeLength * 1000 / self.tickInterval
        self.pw = pg.PlotWidget()
        self.vb = self.pw.getViewBox()
        self.vb.disableAutoRange(axis=self.vb.XAxis)
        self.vb.enableAutoRange(axis=self.vb.YAxis)
        self.curveItems = []
        self.ui.gridLayout.addWidget(self.pw)
        self.connectSignals()
        self.ticker.start(self.tickInterval)

    def connectSignals(self):
        QtCore.QObject.connect(self.ticker, QtCore.SIGNAL("timeout()"), self.tick)
        self.ui.checkBoxAxis.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAxis.checkState(), 'Axis', "FFFF00", 1))  # Yellow
        self.ui.checkBoxShiftEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxShiftEnc.checkState(), 'ShftEnc', "FF0000", 1))  # Red
        self.ui.checkBoxTgtEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxTgtEnc.checkState(), 'TgtEnc', "00FF00", 1))  # Lime
        self.ui.checkBoxEncIn.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxEncIn.checkState(), 'EncIn', "FFFFFF", 1))  # White
        self.ui.checkBoxInPos.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxInPos.checkState(), 'InPos', "0000FF", 1))  # Blue
        self.ui.checkBoxAbsEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAbsEnc.checkState(), 'AbsEnc', "00FFFF", 1))  # Aqua
        self.ui.checkBoxMeasure.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMeasure.checkState(), 'Measure', "FF00FF", 1))  # Fuchsia
        self.ui.checkBoxCtrlEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxCtrlEnc.checkState(), 'CtrlEnc', "800000", 1))  # Maroon
        self.ui.checkBoxMotor.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMotor.checkState(), 'Motor', "996633", 1))  # <Brown>

    def selectedCurve(self, myCheckState, mySource, myColor, myWidth):
        if myCheckState == 2:
            curveItem = CurveItem(self.pw, mySource, myColor, myWidth)
            self.curveItems.append(curveItem)
            try:
                curveItem.arrayTime = [time.time()]
                curveItem.arrayVal = [float(self.thing.getPositionFromBoard(self.icepapAddress, mySource))]
                curveItem.curve.setData(x=curveItem.arrayTime, y=curveItem.arrayVal)
            except:
                if curveItem in self.curveItems:
                    self.vb.removeItem(curveItem.curve)
                    self.curveItems.remove(curveItem)
                print('Init error for ' + mySource + '!')
        else:
            for curveItem in self.curveItems:
                if curveItem.source == mySource:
                    self.vb.removeItem(curveItem.curve)
                    self.curveItems.remove(curveItem)

    def tick(self):
        now = time.time()
        self.pw.setXRange(now - self.xTimeLength, now)

        for curveItem in self.curveItems:
            curveItem.arrayTime.append(now)
            try:
                curveItem.arrayVal.append(float(self.thing.getPositionFromBoard(self.icepapAddress, curveItem.source)))
            except:
                print('Failed to update ' + curveItem.source + '!')
            if len(curveItem.arrayTime) < self.numVisible:
                curveItem.curve.setData(x=curveItem.arrayTime, y=curveItem.arrayVal)
            else:
                curveItem.curve.setData(x=curveItem.arrayTime[-self.numVisible:], y=curveItem.arrayVal[-self.numVisible:])

        #p1 = self.thing.getPositionFromBoard(self.icepapAddress, 'AXIS')
        #e1 = self.thing.getEncoder(self.icepapAddress, 'AXIS')

        self.ticker.start(self.tickInterval)
