from PyQt4 import QtGui, QtCore, Qt
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController
import time


class CurveItem:

    def __init__(self, widget, source, col, width):
        self.source = source
        self.arrayTime = []
        self.arrayVal = []
        self.curve = widget.plot(x=self.arrayTime, y=self.arrayVal, pen={'color': col, 'width': width})


class DialogCurves(QtGui.QDialog):

    def __init__(self, parent, drv):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DialogCurves()
        self.driver = IcepapController().iPaps[drv.icepapsystem_name]
        self.icepapAddress = drv.addr
        self.ui.setupUi(self)
        self.setWindowTitle('Curves  |  ' + drv.icepapsystem_name + '  |  ' + str(self.icepapAddress) + ' ' + drv.name)
        self.show()
        self.refTime = time.time()
        self.ticker = Qt.QTimer(self)
        self.tickInterval = 100  # [milliseconds]
        self.xTimeLength = 60  # [seconds]
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
        self.ui.radioButtonAxis.toggled.connect(self.radioButtonsToggled)
        self.ui.checkBoxAxis.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAxis))
        self.ui.checkBoxShiftEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxShiftEnc))
        self.ui.checkBoxTgtEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxTgtEnc))
        self.ui.checkBoxEncIn.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxEncIn))
        self.ui.checkBoxInPos.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxInPos))
        self.ui.checkBoxAbsEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAbsEnc))
        self.ui.checkBoxMeasure.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMeasure))
        self.ui.checkBoxCtrlEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxCtrlEnc))
        self.ui.checkBoxMotor.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMotor))
        self.ui.checkBoxDelta1.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta1))
        self.ui.checkBoxDelta2.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta2))
        self.ui.checkBoxMoving.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMoving))
        self.ui.checkBoxSettling.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxSettling))
        self.ui.checkBoxOutOfWin.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxOutOfWin))
        self.ui.checkBoxReady.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxReady))
        self.ui.checkBoxStopcode.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxStopcode))
        self.ui.buttonPause.clicked.connect(self.pauseButtonClicked)

    def getVal(self, source):
        f = self.driver.getPositionFromBoard if self.ui.radioButtonAxis.isChecked() else self.driver.getEncoder
        ok = True
        val = 0.0
        try:
            if source == 'Axis - TgtEnc':
                val = float(f(self.icepapAddress, 'Axis')) - float(f(self.icepapAddress, 'TgtEnc'))
            elif source == 'Axis - Motor':
                val = float(f(self.icepapAddress, 'Axis')) - float(f(self.icepapAddress, 'Motor'))
            elif source in ['MOVING', 'SETTLING', 'OUTOFWIN', 'READY', 'STOPCODE']:
                val = float(self.driver.getDecodedStatus(self.icepapAddress).get(str(source.toLower()))[0])
            else:
                val = float(f(self.icepapAddress, source))
        except Exception, e:
            ok = False
            print(e)
        return ok, val

    def radioButtonsToggled(self):
        self.refTime = time.time()
        for curveItem in self.curveItems:
            curveItem.arrayTime = []
            curveItem.arrayVal = []

    def selectedCurve(self, cb):
        checked = cb.checkState()
        source = cb.text()
        if checked == 2:
            (ok, val) = self.getVal(source)
            if ok:
                col = cb.palette().color(cb.palette().Active, cb.palette().WindowText)
                w = 2 if source in ['Axis - TgtEnc', 'Axis - Motor'] else 1
                ci = CurveItem(self.pw, source, col, w)
                self.curveItems.append(ci)
                ci.arrayTime = [time.time() - self.refTime]
                ci.arrayVal = [val]
                ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
            else:
                print('Failed to create curve for ' + source + '!')
        else:
            for ci in self.curveItems:
                if ci.source == source:
                    self.vb.removeItem(ci.curve)
                    self.curveItems.remove(ci)

    def pauseButtonClicked(self):
        if self.ticker.isActive():
            self.ticker.stop()
            self.ui.buttonPause.setText('Run')
        else:
            self.ticker.start(self.tickInterval)
            self.ui.buttonPause.setText('Pause')

    def tick(self):
        now = time.time() - self.refTime
        self.pw.setXRange(now - self.xTimeLength, now)

        for ci in self.curveItems:
            (ok, val) = self.getVal(ci.source)
            if ok:
                ci.arrayTime.append(now)
                ci.arrayVal.append(val)
                count = self.xTimeLength * 1000 / self.tickInterval
                if len(ci.arrayTime) > 1000 * count:
                    ci.arrayTime = ci.arrayTime[-(100 * count):]
                    ci.arrayVal = ci.arrayVal[-(100 * count):]
                ci.curve.setData(x=ci.arrayTime[-(100 * count):], y=ci.arrayVal[-(100 * count):])
            else:
                print('Failed to update curve for ' + ci.source + '!')

        self.ticker.start(self.tickInterval)
