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

    def __init__(self, parent, system_name, address, name):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DialogCurves()
        self.driver = IcepapController().iPaps[system_name]
        self.icepapAddress = address
        self.ui.setupUi(self)
        driver_name = name if name else str(self.icepapAddress)
        self.setWindowTitle('Curves  |  ' + system_name + '  |  ' + driver_name)
        self.show()
        self.ticker = Qt.QTimer(self)
        self.tickInterval = 100  # [milliseconds]
        self.xTimeLength = 60  # [seconds]
        self.pw = pg.PlotWidget()
        self.vb = self.pw.getViewBox()
        self.vb.disableAutoRange(axis=self.vb.XAxis)
        self.vb.enableAutoRange(axis=self.vb.YAxis)
        self.curveItems = []
        self.ui.gridLayout.addWidget(self.pw)
        self.setCheckBoxBackground()
        self.connectSignals()
        self.ticker.start(self.tickInterval)

    def connectSignals(self):
        QtCore.QObject.connect(self.ticker, QtCore.SIGNAL("timeout()"), self.tick)
        self.ui.radioButtonAxis.toggled.connect(self.radioButtonsToggled)
        self.ui.checkBoxAxis.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAxis, 'Axis'))
        self.ui.checkBoxShiftEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxShiftEnc, 'ShftEnc'))
        self.ui.checkBoxTgtEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxTgtEnc, 'TgtEnc'))
        self.ui.checkBoxEncIn.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxEncIn, 'EncIn'))
        self.ui.checkBoxInPos.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxInPos, 'InPos'))
        self.ui.checkBoxAbsEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAbsEnc, 'AbsEnc'))
        self.ui.checkBoxMeasure.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMeasure, 'Measure'))
        self.ui.checkBoxCtrlEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxCtrlEnc, 'CtrlEnc'))
        self.ui.checkBoxMotor.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMotor, 'Motor'))
        self.ui.checkBoxDelta1.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta1, 'Delta1'))
        self.ui.checkBoxDelta2.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta2, 'Delta2'))
        self.ui.buttonPause.pressed.connect(self.pauseButtonPressed)

    def setCheckBoxBackground(self):
        self.ui.groupBoxCurves.setAutoFillBackground(True)
        gbp = self.ui.groupBoxCurves.palette()
        gbp.setColor(self.ui.groupBoxCurves.backgroundRole(), QtGui.QColor.fromRgb(0, 0, 0))
        self.ui.groupBoxCurves.setPalette(gbp)

    def getVal(self, source):
        f = self.driver.getPositionFromBoard if self.ui.radioButtonAxis.isChecked() else self.driver.getEncoder
        ok = True
        val = 0.0
        try:
            if source == 'Delta1':
                val = float(f(self.icepapAddress, 'Axis')) - float(f(self.icepapAddress, 'TgtEnc'))
            elif source == 'Delta2':
                val = float(f(self.icepapAddress, 'Axis')) - float(f(self.icepapAddress, 'Motor'))
            else:
                val = float(f(self.icepapAddress, source))
        except:
            ok = False
        return ok, val

    def radioButtonsToggled(self):
        for curveItem in self.curveItems:
            curveItem.arrayTime = []
            curveItem.arrayVal = []

    def selectedCurve(self, cb, source):
        checked = cb.checkState()
        if checked == 2:
            (ok, val) = self.getVal(source)
            if ok:
                col = cb.palette().color(cb.palette().Active, cb.palette().WindowText)
                w = 2 if source == 'Delta1' or source == 'Delta2' else 1
                ci = CurveItem(self.pw, source, col, w)
                self.curveItems.append(ci)
                ci.arrayTime = [time.time()]
                ci.arrayVal = [val]
                ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
            else:
                print('Failed to create curve for ' + source + '!')
        else:
            for ci in self.curveItems:
                if ci.source == source:
                    self.vb.removeItem(ci.curve)
                    self.curveItems.remove(ci)

    def pauseButtonPressed(self):
        if self.ticker.isActive():
            self.ticker.stop()
            self.ui.buttonPause.setText('Run')
        else:
            self.ticker.start(self.tickInterval)
            self.ui.buttonPause.setText('Pause')

    def tick(self):
        now = time.time()
        self.pw.setXRange(now - self.xTimeLength, now)

        for ci in self.curveItems:
            (ok, val) = self.getVal(ci.source)
            if ok:
                ci.arrayTime.append(now)
                ci.arrayVal.append(val)
                count = self.xTimeLength * 1000 / self.tickInterval
                if len(ci.arrayTime) < count:
                    ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
                else:
                    ci.curve.setData(x=ci.arrayTime[-count:], y=ci.arrayVal[-count:])
            else:
                print('Failed to update curve for ' + ci.source + '!')

        self.ticker.start(self.tickInterval)
