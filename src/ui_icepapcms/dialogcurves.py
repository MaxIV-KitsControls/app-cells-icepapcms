from PyQt4 import QtGui, QtCore, Qt
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController
import time


class CurveItem:

    #def __init__(self, widget, source, col, width, signal='', driver=0, plotAxisNb=0, plotAxis=None):
    def __init__(self, widget, source, col, width, style=QtCore.Qt.SolidLine, signal='', driver=0, plotAxisNb=0):
        self.source = source
        self.arrayTime = []
        self.arrayVal = []
        self.signal = signal
        self.driver = driver
        self.plotAxisNb = plotAxisNb
        self.style = style
        self.col = col
        self.width = width
        self.getCommand()
        print self.command, self.params
        #self.curve = widget.plot(x=self.arrayTime, y=self.arrayVal, pen={'color': col, 'width': width})
        #self.curve has to be a PlotDataItem,
        #self.curve = plotAxis.plot(x=self.arrayTime, y=self.arrayVal, pen={'color': col, 'width': width})

    def renewCurve(self, plotAxis):
        self.curve = plotAxis.plot(x=self.arrayTime, y=self.arrayVal, pen={'color': self.col, 'width': self.width, 'style': self.style})

    def getText(self):
        return '%s:%s:%s'%(self.driver, self.signal, self.plotAxisNb)

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
        #print self.command
        #print self.params


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
        self.xTimeLength = 120  # [seconds]
        self.pw = pg.PlotWidget()
        self.vb = self.pw.getViewBox()
        self.vb.disableAutoRange(axis=self.vb.XAxis)
        self.vb.enableAutoRange(axis=self.vb.YAxis)
        self.curveItems = []
        self.ui.gridLayout.addWidget(self.pw)

        self.last_now = None

        self.axes = []
        self.axes.append(self.pw.getPlotItem())
        self.axes.append(pg.ViewBox())
        self.axes[0].showAxis('right')
        self.axes[0].scene().addItem(self.axes[1])
        self.axes[0].getAxis('right').linkToView(self.axes[1])
        self.axes[1].setXLink(self.axes[0])
        self.axes[0].getAxis('right').setLabel('axis2')
        self.axes.append(pg.ViewBox())
        self.ax3 = pg.AxisItem('right')
        self.axes[0].layout.addItem(self.ax3, 2, 3)
        self.axes[0].scene().addItem(self.axes[2])
        self.ax3.linkToView(self.axes[2])
        self.axes[2].setXLink(self.axes[0])
        self.ax3.setZValue(-10000)
        #ax3.setLabel('axis 3', color='#ff0000')
        self.ax3.setLabel('axis 3')

        self.axes[1].disableAutoRange(axis=self.axes[1].XAxis)
        self.axes[1].enableAutoRange(axis=self.axes[1].YAxis)
        self.axes[2].disableAutoRange(axis=self.axes[2].XAxis)
        self.axes[2].enableAutoRange(axis=self.axes[2].YAxis)

        self.label = pg.LabelItem(justify='right')
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        #self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.pw.addItem(self.vLine, ignoreBounds=True)
        #self.pw.addItem(self.hLine, ignoreBounds=True)
        self.pw.addItem(self.label)


        self.signals = ['PosAxis', 'PosTgtenc', 'PosShftenc',
                      'PosEncin', 'PosAbsenc', 'PosInpos',
                      'PosMotor', 'PosMeas', 'PosCtrlenc',
                      'DifAxMotor', 'DifAxTgtenc', 'DifAxShftenc',
                      'DifAxCtrlenc',
                      'EncEncin', 'EncAbsenc', 'EncInpos',
                      'StatReady', 'StatMoving', 'StatSettling',
                      'StatOutofwin', 'StatStopcode',
                      'StatWarning', 'StatLim+', 'StatLim-', 'StatHome',
                      'MeasI', 'MeasIa', 'MeasIb',
                      'MeasVm'
                      ]
        self.colors = [QtGui.QColor(255, 255, 0), QtGui.QColor(255, 0, 0), QtGui.QColor(0, 255, 0),
            QtGui.QColor(255, 255, 255), QtGui.QColor(51, 153, 255), QtGui.QColor(0, 255, 255),
            QtGui.QColor(255, 0, 255), QtGui.QColor(255, 153, 204), QtGui.QColor(204, 153, 102),
            QtGui.QColor(255, 204, 0), QtGui.QColor(153, 255, 153), QtGui.QColor(255, 170, 0),
            QtGui.QColor(255, 0, 0),
            QtGui.QColor(0, 255, 255), QtGui.QColor(255, 170, 255), QtGui.QColor(255, 255, 127),
            QtGui.QColor(255, 0, 0), QtGui.QColor(255, 0, 0), QtGui.QColor(0, 255, 0),
            QtGui.QColor(255, 255, 255), QtGui.QColor(51, 153, 255),
            QtGui.QColor(255, 0, 255), QtGui.QColor(255, 153, 204), QtGui.QColor(204, 153, 102), QtGui.QColor(255, 204, 0),
            QtGui.QColor(255, 0, 255), QtGui.QColor(255, 153, 204), QtGui.QColor(204, 153, 102),
            QtGui.QColor(255, 204, 0)
            ]
        self.penWidths = [1, 1, 1,
                      1, 1, 1,
                      1, 1, 1,
                      1, 3, 2,
                      3,
                      1, 1, 1,
                      5, 1, 3,
                      2, 1,
                      1, 1, 1, 1,
                      1, 1, 1,
                      1]
        self.penStyles = [QtCore.Qt.SolidLine, QtCore.Qt.SolidLine, QtCore.Qt.SolidLine,
                          QtCore.Qt.SolidLine, QtCore.Qt.SolidLine, QtCore.Qt.SolidLine,
                          QtCore.Qt.SolidLine, QtCore.Qt.SolidLine, QtCore.Qt.SolidLine,
                          QtCore.Qt.SolidLine, QtCore.Qt.DotLine, QtCore.Qt.DashLine,
                          QtCore.Qt.DashLine,
                          QtCore.Qt.DotLine, QtCore.Qt.DashLine, QtCore.Qt.DashLine,
                          QtCore.Qt.DotLine, QtCore.Qt.DashLine, QtCore.Qt.DotLine,
                          QtCore.Qt.SolidLine, QtCore.Qt.DashLine,
                          QtCore.Qt.DashLine, QtCore.Qt.DashLine, QtCore.Qt.DashLine,
                          QtCore.Qt.DashLine, QtCore.Qt.DashLine, QtCore.Qt.DashLine, QtCore.Qt.DashLine,
                          QtCore.Qt.DashLine, QtCore.Qt.DashLine, QtCore.Qt.DashLine,
                          QtCore.Qt.DashLine]

        self.maxDrivers = 128
        self.maxPlotAxes = 3
        for i in range(1, self.maxDrivers +1):
            self.ui.cbDriver.addItem(str(i))
        for item in self.signals:
            self.ui.cbSignals.addItem(item)
        for i in range(1, self.maxPlotAxes +1):
            self.ui.cbPlotAxis.addItem(str(i))


        self.connectSignals()
        self.ticker.start(self.tickInterval)


    def connectSignals(self):
        QtCore.QObject.connect(self.ticker, QtCore.SIGNAL("timeout()"), self.tick)
        #self.ui.radioButtonAxis.toggled.connect(self.radioButtonsToggled)
        #self.ui.checkBoxAxis.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAxis))
        #self.ui.checkBoxShiftEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxShiftEnc))
        #self.ui.checkBoxTgtEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxTgtEnc))
        #self.ui.checkBoxEncIn.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxEncIn))
        #self.ui.checkBoxInPos.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxInPos))
        #self.ui.checkBoxAbsEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxAbsEnc))
        #self.ui.checkBoxMeasure.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMeasure))
        #self.ui.checkBoxCtrlEnc.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxCtrlEnc))
        #self.ui.checkBoxMotor.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMotor))
        #self.ui.checkBoxDelta1.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta1))
        #self.ui.checkBoxDelta2.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxDelta2))
        #self.ui.checkBoxMoving.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxMoving))
        #self.ui.checkBoxSettling.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxSettling))
        #self.ui.checkBoxOutOfWin.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxOutOfWin))
        #self.ui.checkBoxReady.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxReady))
        #self.ui.checkBoxStopcode.stateChanged.connect(lambda: self.selectedCurve(self.ui.checkBoxStopcode))
        self.ui.btnAdd.clicked.connect(self.addButtonClicked)
        self.ui.btnShift.clicked.connect(self.shiftButtonClicked)
        self.ui.btnRemove.clicked.connect(self.removeButtonClicked)
        self.ui.btnPause.clicked.connect(self.pauseButtonClicked)
        self.ui.btnCLoop.clicked.connect(self.prepareCloop)
        self.ui.btnCurrents.clicked.connect(self.prepareCurrents)

        self.proxy = pg.SignalProxy(self.pw.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)

        self.axes[0].vb.sigResized.connect(self.updateViews)

    def updateViews(self):
        ## view has resized; update auxiliary views to match

        self.axes[1].setGeometry(self.axes[0].vb.sceneBoundingRect())
        self.axes[2].setGeometry(self.axes[0].vb.sceneBoundingRect())

        ## need to re-update linked axes since this was called
        ## incorrectly while views had different shapes.
        ## (probably this should be handled in ViewBox.resizeEvent)
        self.axes[1].linkedViewChanged(self.axes[0].vb, self.axes[1].XAxis)
        self.axes[2].linkedViewChanged(self.axes[0].vb, self.axes[2].XAxis)


    def updatePlotAxesLabels(self):
        txt = ['', '', '']
        for ci in self.curveItems:
            #txt1 = txt1 + "<span style='font-size: 7pt; color: %s;'>%s </span>"%(self.curveItems[i].col.name(), self.curveItems[i].getText())
            txt[ci.plotAxisNb - 1] += "<span style='font-size: 8pt; color: %s;'>%s</span>"%(ci.col.name(), ci.getText())
        print txt
        self.axes[0].getAxis('left').setLabel(txt[0])
        self.axes[0].getAxis('right').setLabel(txt[1])
        self.ax3.setLabel(txt[2])
            
    def addButtonClicked(self):
        cb = self.ui.cbSignals
        color = cb.palette().color(cb.palette().Active, cb.palette().WindowText)
        ci = CurveItem(self.pw,
                       source='',
                       col=self.colors[self.ui.cbSignals.currentIndex()],
                       width=self.penWidths[self.ui.cbSignals.currentIndex()],
                       style=self.penStyles[self.ui.cbSignals.currentIndex()],
                       signal=self.signals[self.ui.cbSignals.currentIndex()],
                       driver=self.ui.cbDriver.currentIndex() + 1,
                       plotAxisNb=self.ui.cbPlotAxis.currentIndex() + 1,
                       #plotAxis = self.axes[self.ui.cbPlotAxis.currentIndex()]
                       #curve=self.get
                       )
        self.getCurve(ci)
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
        self.updatePlotAxesLabels()

    def addSignal(self, signalNb, plotAxisNb):
        ci = CurveItem(self.pw,
                       source='',
                       col=self.colors[signalNb],
                       width=self.penWidths[signalNb],
                       style=self.penStyles[signalNb],
                       signal=self.signals[signalNb],
                       driver=self.icepapAddress,
                       plotAxisNb=plotAxisNb,
                       #plotAxis = self.axes[self.ui.cbPlotAxis.currentIndex()]
                       #curve=self.get
                       )
        self.getCurve(ci)
        self.curveItems.append(ci)
        ci.arrayTime = [time.time() - self.refTime]
        ci.arrayVal = [1]
        ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
        #self.ui.cbCurves.addItem(ci.getText())
        self.ui.listCurves.addItem(ci.getText())
        self.ui.listCurves.setCurrentRow(len(self.curveItems) - 1)
        self.ui.listCurves.item(len(self.curveItems) - 1).setForeground(ci.col)
        self.ui.listCurves.item(len(self.curveItems) - 1).setBackground(QtGui.QColor(0,0,0))
        self.updatePlotAxesLabels()

    def shiftButtonClicked(self):
        #ci = self.curveItems[self.ui.cbCurves.currentIndex()]
        index = self.ui.listCurves.currentRow()
        ci = self.curveItems[index]

        self.removeCurve(ci)

        ci.plotAxisNb = ci.plotAxisNb%self.maxPlotAxes + 1
        #ci.plotAxis = self.axes[ci.plotAxisNb]
        self.getCurve(ci)
        #ci.renewCurve(self.axes[ci.plotAxisNb-1])

        #self.ui.cbCurves.setItemText(index, ci.getText())
        self.ui.listCurves.takeItem(index)
        self.ui.listCurves.insertItem(index, ci.getText())
        self.ui.listCurves.item(index).setForeground(ci.col)
        self.ui.listCurves.item(index).setBackground(QtGui.QColor(0,0,0))
        self.ui.listCurves.setCurrentRow(index)
        self.updatePlotAxesLabels()

    def getCurve(self, ci):
        if ci.plotAxisNb == 1:
            ci.curve = self.axes[0].plot(x=ci.arrayTime, y=ci.arrayVal, pen={'color': ci.col, 'width': ci.width, 'style' : ci.style})
        else:
            ci.curve = pg.PlotCurveItem(x=ci.arrayTime, y=ci.arrayVal, pen={'color': ci.col, 'width': ci.width, 'style' : ci.style})
            self.axes[ci.plotAxisNb - 1].addItem(ci.curve)

    def removeButtonClicked(self):
        self.removeSignal(self.ui.listCurves.currentRow())

    def removeSignal(self, n):
        self.removeCurve(self.curveItems[n])
        self.curveItems.remove(self.curveItems[n])
        #self.ui.cbCurves.removeItem(self.ui.cbCurves.currentIndex())
        self.ui.listCurves.takeItem(n)
        self.updatePlotAxesLabels()

    def mouseMoved(self, evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.pw.sceneBoundingRect().contains(pos):
            mousePoint = self.vb.mapSceneToView(pos)
            index = mousePoint.x()
            viewRange = self.pw.viewRange()
            xMaxViewed = viewRange[0][1]
            xMinViewed = viewRange[0][0]
            #print "index, xmaxv, xminv ", index, xMaxViewed, xMinViewed
            txt = "<span style='font-size: 10pt; color: white; font-weight: bold'>"
            txt = txt + "%0.2f"%(index)
            txt = txt + "</span>"
            txt1 = ''
            for i in range(0, len(self.curveItems)):
                if index > self.curveItems[i].arrayTime[0] and index < self.curveItems[i].arrayTime[-1]:
                    aTimeIndex = self.findIndexInTimes(self.curveItems[i].arrayTime, index)
                    txt = txt + "<span style='font-size: 8pt; color: %s; font-weight: bold'>"%(self.curveItems[i].col.name())
                    txt = txt + ' | '
                    #txt = txt + ' ' + "%0.2f"%(self.curveItems[i].arrayTime[aTimeIndex])
                    txt = txt + ' ' + str(self.curveItems[i].arrayVal[aTimeIndex])
                    txt = txt + "</span>"
                    #txt1 = txt1 + "<span style='font-size: 7pt; color: %s;'>%s </span>"%(self.curveItems[i].col.name(), self.curveItems[i].getText())
                    if i%4 == 3:
                        #txt1 = txt1 + "<br>"
                        txt = txt + "<br>"
	    #self.pw.setTitle("%s<br>%s" % (txt1,txt))
	    self.pw.setTitle("%s" % (txt))
            self.vLine.setPos(mousePoint.x())
            #self.hLine.setPos(mousePoint.y())

    def findIndexInTimes(self, aList, value):
        for i in range(0, len(aList)):
            if aList[i] > value:
                return i
        return -1


    def getValue(self, ci):
        #f = self.driver.getPositionFromBoard if self.ui.radioButtonAxis.isChecked() else self.driver.getEncoder
        ok = True
        val = 0.0 
        try:
            if ci.signal.startswith('Dif'):
		val = float(self.driver.getPositionFromBoard(ci.driver, 'AXIS')) - float(self.driver.getPositionFromBoard(ci.driver, ci.params[1]))
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

    def addedCurve(self, ci):
        (ok, val) = self.getValue(ci)
        if ok:
            ci.arrayTime = [time.time() - self.refTime]
            ci.arrayVal = [val]
            ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
        else:
            print('Failed to create curve for ' + ci.signal + '!')

    def removeCurve(self, ci):
        self.vb.removeItem(ci.curve)

    def prepareCloop(self):
        for i in range(0, self.ui.listCurves.count()):
            self.removeCurve(i)
        self.addSignal(0, 1)# signalNb, plotAxisNb)
        self.addSignal(9, 2)
        self.addSignal(10, 2)
        self.addSignal(16, 3)
        self.addSignal(18, 3)
        self.addSignal(19, 3)
        self.addSignal(20, 3)

    def prepareCurrents(self):
        for i in range(0, self.ui.listCurves.count()):
            self.removeCurve(i)
        self.addSignal(0, 1)# signalNb, plotAxisNb)
        self.addSignal(25, 2)
        self.addSignal(28, 3)

    def pauseButtonClicked(self):
        if self.ticker.isActive():
            self.ticker.stop()
            self.ui.btnPause.setText('Run')
        else:
            self.ticker.start(self.tickInterval)
            self.ui.btnPause.setText('Pause')

    def tick(self):
        now = time.time() - self.refTime
        #print now
        #print "range:", self.pw.viewRange()
        pwrange = self.pw.viewRange()
        pwXRangeLength = pwrange[0][1] - pwrange[0][0]
        if pwrange[0][1] >= self.last_now:
            #self.pw.setXRange(now - self.xTimeLength, now)
            self.pw.setXRange(now - pwXRangeLength, now, padding = 0)
            #self.pw.setXRange(self.pw.viewRange()[0][0],
            #                  now)
        self.last_now = now

        for ci in self.curveItems:
            #(ok, val) = self.getVal(ci.source)
            (ok, val) = self.getValue(ci)
            if ok:
                ci.arrayTime.append(now)
                ci.arrayVal.append(val)
                displayedDataPoints = self.xTimeLength * 1000 / self.tickInterval
                #if len(ci.arrayTime) > 1000 * displayedDataPoints: #this should be 100*
                #    ci.arrayTime = ci.arrayTime[-(100 * displayedDataPoints):]
                #    ci.arrayVal = ci.arrayVal[-(100 * displayedDataPoints):]
                #ci.curve.setData(x=ci.arrayTime[-(100 * displayedDataPoints):], y=ci.arrayVal[-(100 * displayedDataPoints):])
                ci.curve.setData(x=ci.arrayTime, y=ci.arrayVal)
            else:
                print('Failed to update curve for ' + ci.source + '!')

        self.ticker.start(self.tickInterval)
