from PyQt4 import QtGui, QtCore, Qt
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController
import time


class CurveItem:

    def __init__(self, widget, source, col, width, signal='', driver=0, plotAxis=0):
        self.source = source
        self.arrayTime = []
        self.arrayVal = []
        self.signal = signal
        self.driver = driver
        self.plotAxis = plotAxis
        self.col = col
        self.getCommand()
        print self.command, self.params
        self.curve = widget.plot(x=self.arrayTime, y=self.arrayVal, pen={'color': col, 'width': width})

    def getText(self):
        return '%s:%s:%s'%(self.driver, self.signal, self.plotAxis)

    def getCommand(self):
        if self.signal.startswith('Pos'):
            self.command = 'POS'
            self.params = [self.signal.replace('Pos', '')]
        elif self.signal.startswith('Enc'):
            self.command = 'ENC'
            self.params = [self.signal.replace('Enc', '')]
        elif self.signal.startswith('Dif'):
            self.command = 'POS'
            self.params = ['Axis', self.signal.replace('DifAx', '')]
        elif self.signal.startswith('Meas'):
            self.command = 'MEAS'
            self.params = [self.signal.replace('Meas', '')]
        elif self.signal.startswith('Stat'):
            self.command = 'STATUS'
            self.params = [self.signal.replace('Stat', '')]


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
        self.last_now = None

        self.label = pg.LabelItem(justify='right')
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.pw.addItem(self.vLine, ignoreBounds=True)
        self.pw.addItem(self.hLine, ignoreBounds=True)
        self.pw.addItem(self.label)

        self.signals = ['PosAxis', 'PosTgtenc', 'PosShftenc',
                      'PosEncin', 'PosAbsenc', 'PosInpos',
                      'PosMotor', 'PosMeas', 'PosCtrlenc',
                      'DifAxMotor', 'DifAxTgtenc', 'DifAxShftenc',
                      'DifAxCtrlenc',
                      'EncEncin', 'EncAbsenc', 'EncInpos',
                      'StatReady', 'StatMoving', 'StatSettling',
                      'StatOutofwin', 'StatStopcode',
                      'MeasI', 'MeasIa', 'MeasIb',
                      'MeasVm'
                      ]
        self.colors = [QtGui.QColor(255, 255, 0), QtGui.QColor(255, 0, 0), QtGui.QColor(0, 255, 0),
            QtGui.QColor(255, 255, 255), QtGui.QColor(51, 153, 255), QtGui.QColor(0, 255, 255),
            QtGui.QColor(255, 0, 255), QtGui.QColor(255, 153, 204), QtGui.QColor(204, 153, 102),
            QtGui.QColor(255, 204, 0), QtGui.QColor(153, 255, 153), QtGui.QColor(255, 170, 0),
            QtGui.QColor(255, 0, 0),
            QtGui.QColor(0, 255, 255), QtGui.QColor(255, 170, 255), QtGui.QColor(255, 255, 127),
            QtGui.QColor(255, 255, 0), QtGui.QColor(255, 0, 0), QtGui.QColor(0, 255, 0),
            QtGui.QColor(255, 255, 255), QtGui.QColor(51, 153, 255),
            QtGui.QColor(255, 0, 255), QtGui.QColor(255, 153, 204), QtGui.QColor(204, 153, 102),
            QtGui.QColor(255, 204, 0)
            ]

        self.maxDrivers = 128
        self.maxPlotAxes = 4
        for i in range(1, self.maxDrivers +1):
            self.ui.cbDriver.addItem(str(i))
        for item in self.signals:
            self.ui.cbSignals.addItem(item)
        for i in range(1, self.maxPlotAxes +1):
            self.ui.cbPlotAxis.addItem(str(i))

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
        self.ui.btnAdd.clicked.connect(self.addButtonClicked)
        self.ui.btnShift.clicked.connect(self.shiftButtonClicked)
        self.ui.btnRemove.clicked.connect(self.removeButtonClicked)

        self.proxy = pg.SignalProxy(self.pw.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)


    def addButtonClicked(self):
        cb = self.ui.cbSignals
        color = cb.palette().color(cb.palette().Active, cb.palette().WindowText)
        ci = CurveItem(self.pw,
                       source='',
                       col=self.colors[self.ui.cbSignals.currentIndex()],
                       width=1,
                       signal=self.signals[self.ui.cbSignals.currentIndex()],
                       driver=self.ui.cbDriver.currentIndex() + 1,
                       plotAxis=self.ui.cbPlotAxis.currentIndex() + 1
                       )
        self.curveItems.append(ci)
        ci.arrayTime = [time.time() - self.refTime]
        ci.arrayVal = [1]
        ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
        #self.ui.cbCurves.addItem(ci.getText())
        self.ui.listCurves.addItem(ci.getText())
        self.ui.listCurves.setCurrentRow(len(self.curveItems) - 1)
        self.ui.listCurves.item(len(self.curveItems) - 1).setForeground(ci.col)
        self.ui.listCurves.item(len(self.curveItems) - 1).setBackground(QtGui.QColor(0,0,0))

        #self.ui.listCurves.setCurrentItem(ci.getText())

    def shiftButtonClicked(self):
        #ci = self.curveItems[self.ui.cbCurves.currentIndex()]
        index = self.ui.listCurves.currentRow()
        ci = self.curveItems[index]
        ci.plotAxis = ci.plotAxis%self.maxPlotAxes + 1
        #self.ui.cbCurves.setItemText(index, ci.getText())
        self.ui.listCurves.takeItem(index)
        self.ui.listCurves.insertItem(index, ci.getText())
        self.ui.listCurves.setCurrentRow(index)

    def removeButtonClicked(self):
        #self.curveItems.remove(self.curveItems[self.ui.cbCurves.currentIndex()])
        self.curveItems.remove(self.curveItems[self.ui.listCurves.currentRow()])
        #self.ui.cbCurves.removeItem(self.ui.cbCurves.currentIndex())
        self.ui.listCurves.takeItem(self.ui.listCurves.currentRow())

    def mouseMoved(self, evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.pw.sceneBoundingRect().contains(pos):
            mousePoint = self.vb.mapSceneToView(pos)
            index = mousePoint.x()
            viewRange = self.pw.viewRange()
            xMaxViewed = viewRange[0][1]
            xMinViewed = viewRange[0][0]
            print "index, xmaxv, xminv ", index, xMaxViewed, xMinViewed
            txt = '' + "%0.2f"%(index)
            for i in range(0, len(self.curveItems)):
                if index > self.curveItems[i].arrayTime[0] and index < self.curveItems[i].arrayTime[-1]:
                    aTimeIndex = self.findIndexInTimes(self.curveItems[i].arrayTime, index)
                    txt = txt + ' ' + str(i)
                    txt = txt + ' ' + "%0.2f"%(self.curveItems[i].arrayTime[aTimeIndex])
                    txt = txt + ' ' + str(self.curveItems[i].arrayVal[aTimeIndex])
            self.pw.setTitle(
                   "<span style='font-size: 10pt; color: red;'>%s</span>" % (
                    txt))
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())

    def findIndexInTimes(self, aList, value):
        for i in range(0, len(aList)):
            if aList[i] > value:
                return i
        return -1

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

    def getValue(self, ci):
        #f = self.driver.getPositionFromBoard if self.ui.radioButtonAxis.isChecked() else self.driver.getEncoder
        ok = True
        val = 0.0
        try:
            if ci.signal.startswith('Diff'):
                val = float(self.driver.getPosition(ci.driver)) - \
                      float(self.driver.getPositionFromBoard(ci.driver, ci.params[1]))
            elif ci.command == 'POS':
                val = float(self.driver.getPositionFromBoard(ci.driver, ci.params[0]))
            elif ci.command == 'ENC':
                val = float(self.driver.getEncoder(ci.driver, ci.params[0]))
            elif ci.params[0] in ['Moving', 'Settling', 'Outofwin', 'Ready', 'Stopcode']:
                val = float(self.driver.getDecodedStatus(ci.driver).get(str(ci.params[0].lower()))[0])
            elif ci.command == 'MEAS':
                val = float(self.driver.getMeas(ci.driver, ci.params[0]))
        except Exception, e:
            ok = False
            print(e)
        return ok, val

    def radioButtonsToggled(self):
        self.refTime = time.time()
        for curveItem in self.curveItems:
            curveItem.arrayTime = []
            curveItem.arrayVal = []

    def addedCurve(self, ci):
        checked = True
        source = ci.signal
        if checked == True:
            (ok, val) = self.getValue(ci)
            if ok:
                pal = self.ui.listCurves.palette()
                col = pal.color(pal.Active, pal.WindowText)
                if ci.signal.startswith('Diff'):
                    w = 2
                else:
                    w = 1
                # in ['Axis - TgtEnc', 'Axis - Motor'] else 1
                #ci = CurveItem(self.pw, source, col, w)
                #self.curveItems.append(ci)
                ci.arrayTime = [time.time() - self.refTime]
                ci.arrayVal = [val]
                ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
            else:
                print('Failed to create curve for ' + ci.signal + '!')
        else:
            for ci in self.curveItems:
                if ci.source == source:
                    self.vb.removeItem(ci.curve)
                    self.curveItems.remove(ci)

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
        #print "range:", self.pw.viewRange()
        if self.pw.viewRange()[0][1] >= self.last_now:
            self.pw.setXRange(now - self.xTimeLength, now)
        self.last_now = now

        for ci in self.curveItems:
            #(ok, val) = self.getVal(ci.source)
            (ok, val) = self.getValue(ci)
            if ok:
                ci.arrayTime.append(now)
                ci.arrayVal.append(val)
                displayedDataPoints = self.xTimeLength * 1000 / self.tickInterval
                if len(ci.arrayTime) > 1000 * displayedDataPoints: #this should be 100*
                    ci.arrayTime = ci.arrayTime[-(100 * displayedDataPoints):]
                    ci.arrayVal = ci.arrayVal[-(100 * displayedDataPoints):]
                ci.curve.setData(x=ci.arrayTime[-(100 * displayedDataPoints):], y=ci.arrayVal[-(100 * displayedDataPoints):])
            else:
                print('Failed to update curve for ' + ci.source + '!')

        self.ticker.start(self.tickInterval)
