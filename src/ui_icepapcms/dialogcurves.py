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
        self.colorAxis = QtGui.QColor(255, 255, 0)       # Yellow
        self.colorShftEnc = QtGui.QColor(255, 0, 0)      # Red
        self.colorTgtEnc = QtGui.QColor(0, 255, 0)       # Lime
        self.colorEncIn = QtGui.QColor(255, 255, 255)    # White
        self.colorInPos = QtGui.QColor(51, 153, 255)     # <Light blue>
        self.colorAbsEnc = QtGui.QColor(0, 255, 255)     # Aqua
        self.colorMeasure = QtGui.QColor(255, 0, 255)    # Fuchsia
        self.colorCtrlEnc = QtGui.QColor(255, 153, 204)  # <Pink>
        self.colorMotor = QtGui.QColor(204, 153, 102)    # <Light brown>
        self.colorDelta1 = QtGui.QColor(255, 204, 0)     # <Dark yellow>
        self.colorDelta2 = QtGui.QColor(153, 255, 153)   # <Light green>
        self.connectSignals()
        self.ticker.start(self.tickInterval)

    def connectSignals(self):
        QtCore.QObject.connect(self.ticker, QtCore.SIGNAL("timeout()"), self.tick)
        self.ui.radioButtonAxis.toggled.connect(self.radioButtonsToggled)
        #self.ui.checkBoxAxis.setPalette(QtGui.QPalette(self.colorAxis))
        self.ui.groupBoxCurves.setStyleSheet("background-color: rgb(0, 0, 0)")
        #self.ui.checkBoxAxis.setStyleSheet("color: rgb(255, 255, 0)")
        #self.ui.checkBoxAxis.setStyleSheet("color: self.colorAxis")
        #self.ui.checkBoxAxis.setStyleSheet(self.colorAxis)
        self.ui.checkBoxAxis.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAxis, 'Axis', 1))
        self.ui.checkBoxShiftEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxShiftEnc, 'ShftEnc', 1))
        self.ui.checkBoxTgtEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxTgtEnc, 'TgtEnc', 1))
        self.ui.checkBoxEncIn.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxEncIn, 'EncIn', 1))
        self.ui.checkBoxInPos.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxInPos, 'InPos', 1))
        self.ui.checkBoxAbsEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAbsEnc, 'AbsEnc', 1))
        self.ui.checkBoxMeasure.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMeasure, 'Measure', 1))
        self.ui.checkBoxCtrlEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxCtrlEnc, 'CtrlEnc', 1))
        self.ui.checkBoxMotor.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMotor, 'Motor', 1))
        self.ui.checkBoxDelta1.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta1, 'Delta1', 2))
        self.ui.checkBoxDelta2.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta2, 'Delta2', 2))

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

    def selectedCurve(self, cb, source, width):
        checked = cb.checkState()
        if checked == 2:
            (ok, val) = self.getVal(source)
            if ok:
                col = cb.palette().color(cb.palette().Active, cb.palette().Text)
                ci = CurveItem(self.pw, source, col, width)
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

    def tick(self):
        now = time.time()
        self.pw.setXRange(now - self.xTimeLength, now)

        for ci in self.curveItems:
            (ok, val) = self.getVal(ci.source)
            if ok:
                ci.arrayTime.append(now)
                ci.arrayVal.append(val)
                numVisibleTicks = self.xTimeLength * 1000 / self.tickInterval
                if len(ci.arrayTime) < numVisibleTicks:
                    ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
                else:
                    ci.curve.setData(x=ci.arrayTime[-numVisibleTicks:], y=ci.arrayVal[-numVisibleTicks:])
            else:
                print('Failed to update curve for ' + ci.source + '!')

        self.ticker.start(self.tickInterval)
