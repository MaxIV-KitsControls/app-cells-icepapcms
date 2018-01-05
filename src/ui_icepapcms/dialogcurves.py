from PyQt4 import QtGui, QtCore, Qt
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController
import numpy as np
import time


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
        self.tickInterval = 500  # [milliseconds]
        self.xTimeLength = 60  # [seconds]
        # Todo: Create an n-dimentional array that includes time and other curves?
        # Todo: Also look at list-of-dicts and dict-of-lists.
        self.arrayTime = np.empty(self.xTimeLength * 1000 / self.tickInterval)
        self.pw = pg.PlotWidget()
        self.vb = self.pw.getViewBox()
        self.vb.disableAutoRange(axis=self.vb.XAxis)
        self.vb.enableAutoRange(axis=self.vb.YAxis)
        self.arrayAxis = np.empty(self.xTimeLength * 1000 / self.tickInterval)
        self.arrayShiftEnc = np.empty(self.xTimeLength * 1000 / self.tickInterval)
        self.arrayTargetEnc = np.empty(self.xTimeLength * 1000 / self.tickInterval)
        self.curveAxis = self.pw.plot(x=self.arrayTime, y=self.arrayAxis, pen={'color':"FF0", 'width':1})
        self.curveShiftEnc = self.pw.plot(x=self.arrayTime, y=self.arrayAxis, pen={'color':"F00", 'width':1})
        self.curveTargetEnc = self.pw.plot(x=self.arrayTime, y=self.arrayAxis, pen={'color':"0F0", 'width':1})
        self.ui.gridLayout.addWidget(self.pw)
        self.connectSignals()
        self.initCurves()
        #self.arrayPosAxis = []
        #self.arrayPosIndexer = []
        #self.arrayPosExtErr = []
        #self.arrayPosShftEnc = []
        #self.arrayPosTgtEnc = []
        #self.arrayPosEncIn = []
        #self.arrayPosInPos = []
        #self.arrayPosAbsEnc = []
        #self.arrayEncAxis = []
        #self.arrayEncIndexer = []
        #self.arrayEncExtErr = []
        #self.arrayEncShftEnc = []
        #self.arrayEncTgtEnc = []
        #self.arrayEncEncIn = []
        #self.arrayEncInPos = []
        #self.arrayEncAbsEnc = []

    def connectSignals(self):
        QtCore.QObject.connect(self.ticker, QtCore.SIGNAL("timeout()"), self.tick)
        self.ui.checkBoxAxis.stateChanged.connect(self.signalAxis)
        self.ui.checkBoxShiftEnc.stateChanged.connect(self.signalShiftEnc)
        self.ui.checkBoxTgtEnc.stateChanged.connect(self.signalTargetEnc)

    def initCurves(self):
        now = time.time()
        self.arrayTime.fill(None)
        self.arrayTime[-1] = now
        self.pw.setXRange(now - self.xTimeLength, now)
        self.arrayAxis.fill(None)
        self.arrayAxis[-1] = 1  # Get some strange warnings if not set to value != 0.
        self.curveAxis.setData(x=self.arrayTime, y=self.arrayAxis)
        self.ticker.start(self.tickInterval)

    def signalAxis(self, checked):
        self.arrayAxis.fill(None)
        if checked == 2:
            self.ac.append('Axis')
            try:
                self.arrayAxis[-1] = float(self.thing.getPositionFromBoard(self.icepapAddress, 'Axis'))
            except:
                self.ac.remove('Axis')
                print('Init error for Axis!')
        else:
            if 'Axis' in self.ac: self.ac.remove('Axis')
        print(self.ac)
        self.curveAxis.setData(x=self.arrayTime, y=self.arrayAxis)

    def signalShiftEnc(self, checked):
        self.arrayShiftEnc.fill(None)
        if checked == 2:
            self.ac.append('ShftEnc')
            try:
                self.arrayShiftEnc[-1] = float(self.thing.getPositionFromBoard(self.icepapAddress, 'ShftEnc'))
            except:
                self.ac.remove('ShftEnc')
                print('Init error for ShftEnc!')
        else:
            if 'ShftEnc' in self.ac: self.ac.remove('ShftEnc')
        print(self.ac)
        self.curveShiftEnc.setData(x=self.arrayTime, y=self.arrayShiftEnc)

    def signalTargetEnc(self, checked):
        self.arrayTargetEnc.fill(None)
        if checked == 2:
            self.ac.append('TgtEnc')
            try:
                self.arrayTargetEnc[-1] = float(self.thing.getPositionFromBoard(self.icepapAddress, 'TgtEnc'))
            except:
                self.ac.remove('TgtEnc')
                print('Init error for TgtEnc!')
        else:
            if 'TgtEnc' in self.ac: self.ac.remove('TgtEnc')
        print(self.ac)
        self.curveTargetEnc.setData(x=self.arrayTime, y=self.arrayTargetEnc)

    def tick(self):
        now = time.time()
        e1 = np.empty_like(self.arrayTime)
        e1[:-1] = self.arrayTime[1:]
        e1[-1] = now
        self.arrayTime = e1
        self.pw.setXRange(now - self.xTimeLength, now)

        if 'Axis' in self.ac:
            try:
                newVal = float(self.thing.getPositionFromBoard(self.icepapAddress, 'Axis'))
            except:
                print('Failed to update Axis!')
            e2 = np.empty_like(self.arrayAxis)
            e2[:-1] = self.arrayAxis[1:]
            e2[-1] = newVal
            self.arrayAxis = e2
            # if self.ui.checkBoxAxis.isChecked():
            #    curveAxis = self.pw.plot(x=self.arrayTime, y=self.arrayAxis)
            self.curveAxis.setData(x=self.arrayTime, y=self.arrayAxis)
            # Todo: Try letting array grow and only display last bit. Saves us from the shifting each tick.

        if 'ShftEnc' in self.ac:
            try:
                newVal = float(self.thing.getPositionFromBoard(self.icepapAddress, 'ShftEnc'))
            except:
                print('Failed to update ShftEnc!')
            e2 = np.empty_like(self.arrayShiftEnc)
            e2[:-1] = self.arrayShiftEnc[1:]
            e2[-1] = newVal
            self.arrayShiftEnc = e2
            self.curveShiftEnc.setData(x=self.arrayTime, y=self.arrayShiftEnc)

        if 'TgtEnc' in self.ac:
            try:
                newVal = float(self.thing.getPositionFromBoard(self.icepapAddress, 'TgtEnc'))
            except:
                print('Failed to update TgtEnc!')
            e2 = np.empty_like(self.arrayTargetEnc)
            e2[:-1] = self.arrayTargetEnc[1:]
            e2[-1] = newVal
            self.arrayTargetEnc = e2
            self.curveTargetEnc.setData(x=self.arrayTime, y=self.arrayTargetEnc)

        #p1 = self.thing.getPositionFromBoard(self.icepapAddress, 'AXIS')
        #p2 = self.thing.getPositionFromBoard(self.icepapAddress, 'SHFTENC')
        #p3 = self.thing.getPositionFromBoard(self.icepapAddress, 'TGTENC')
        #p4 = self.thing.getPositionFromBoard(self.icepapAddress, 'ENCIN')
        #p5 = self.thing.getPositionFromBoard(self.icepapAddress, 'INPOS')
        #p6 = self.thing.getPositionFromBoard(self.icepapAddress, 'ABSENC')
        #p7 = self.thing.getPositionFromBoard(self.icepapAddress, 'MEASURE')
        #p8 = self.thing.getPositionFromBoard(self.icepapAddress, 'CTRLENC')
        #p9 = self.thing.getPositionFromBoard(self.icepapAddress, 'MOTOR')
        #e1 = self.thing.getEncoder(self.icepapAddress, 'AXIS')
        #e2 = self.thing.getEncoder(self.icepapAddress, 'SHFTENC')
        #e3 = self.thing.getEncoder(self.icepapAddress, 'TGTENC')
        #e4 = self.thing.getEncoder(self.icepapAddress, 'ENCIN')
        #e5 = self.thing.getEncoder(self.icepapAddress, 'INPOS')
        #e6 = self.thing.getEncoder(self.icepapAddress, 'ABSENC')
        #e7 = self.thing.getEncoder(self.icepapAddress, 'MEASURE')
        #e8 = self.thing.getEncoder(self.icepapAddress, 'CTRLENC')
        #e9 = self.thing.getEncoder(self.icepapAddress, 'MOTOR')

        # self.arrayPosAxis.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'Axis')))
        # self.arrayPosIndexer.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'Indexer')))
        # self.arrayPosExtErr.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'ExtErr')))
        # self.arrayPosShftEnc.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'ShftEnc')))
        # self.arrayPosTgtEnc.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'TgtEnc')))
        # self.arrayPosEncIn.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'EncIn')))
        # self.arrayPosInPos.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'InPos')))
        # self.arrayPosAbsEnc.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'AbsEnc')))

        # if self.ui.checkBoxAxis.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosAxis)
        # if self.ui.checkBox_2.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosIndexer)
        # if self.ui.checkBox.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosExtErr)
        # if self.ui.checkBox_4.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosShftEnc)
        # if self.ui.checkBox_5.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosTgtEnc)
        # if self.ui.checkBox_6.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosEncIn)
        # if self.ui.checkBox_7.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosInPos)
        # if self.ui.checkBox_8.isChecked():
        #     self.pw.plot(x=self.arrayTime, y=self.arrayPosAbsEnc)
        # myEncoderVal = float(self.thing.getEncoder(self.icepapAddress, 'AbsEnc'))
        # self.arrayEncAxis.append(myEncoderVal)
        # self.pw.plot(x=self.arrayTime, y=self.arrayEncAxis)

        self.ticker.start(self.tickInterval)
