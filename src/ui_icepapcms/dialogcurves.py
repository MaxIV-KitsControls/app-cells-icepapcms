from PyQt4 import QtGui, QtCore, Qt
from ui_dialogcurves import Ui_DialogCurves
import pyqtgraph as pg
from lib_icepapcms import IcepapController
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
        self.tickInterval = 100  # [milliseconds]
        self.xTimeLength = 60  # [seconds]
        self.numVisible = self.xTimeLength * 1000 / self.tickInterval
        # Todo: Create an n-dimentional array that includes time and other curves?
        # Todo: Also look at list-of-dicts and dict-of-lists.
        self.pw = pg.PlotWidget()
        self.vb = self.pw.getViewBox()
        self.vb.disableAutoRange(axis=self.vb.XAxis)
        self.vb.enableAutoRange(axis=self.vb.YAxis)
        self.arrayAxisTime = []
        self.arrayShiftEncTime = []
        self.arrayTargetEncTime = []
        self.arrayAxis = []
        self.arrayShiftEnc = []
        self.arrayTargetEnc = []
        self.curveAxis = self.pw.plot(x=self.arrayAxisTime, y=self.arrayAxis, pen={'color':"FF0", 'width':1})
        self.curveShiftEnc = self.pw.plot(x=self.arrayShiftEncTime, y=self.arrayShiftEnc, pen={'color':"F00", 'width':1})
        self.curveTargetEnc = self.pw.plot(x=self.arrayTargetEncTime, y=self.arrayTargetEnc, pen={'color':"0F0", 'width':1})
        self.ui.gridLayout.addWidget(self.pw)
        self.connectSignals()
        self.ticker.start(self.tickInterval)

    def connectSignals(self):
        QtCore.QObject.connect(self.ticker, QtCore.SIGNAL("timeout()"), self.tick)
        self.ui.checkBoxAxis.stateChanged.connect(self.signalAxis)
        self.ui.checkBoxShiftEnc.stateChanged.connect(self.signalShiftEnc)
        self.ui.checkBoxTgtEnc.stateChanged.connect(self.signalTargetEnc)

    def signalAxis(self, checked):
        if checked == 2:
            try:
                if 'Axis' not in self.ac: self.ac.append('Axis')
                self.arrayAxisTime = [time.time()]
                self.arrayAxis =[float(self.thing.getPositionFromBoard(self.icepapAddress, 'Axis'))]
            except:
                if 'Axis' in self.ac: self.ac.remove('Axis')
                self.arrayAxisTime = []
                self.arrayAxis = []
                print('Init error for Axis!')
        else:
            if 'Axis' in self.ac: self.ac.remove('Axis')
            self.arrayAxisTime = []
            self.arrayAxis = []
        print(self.ac)
        self.curveAxis.setData(x=self.arrayAxisTime, y=self.arrayAxis)

    def signalShiftEnc(self, checked):
        if checked == 2:
            try:
                if 'ShftEnc' not in self.ac: self.ac.append('ShftEnc')
                self.arrayShiftEncTime = [time.time()]
                self.arrayShiftEnc =[float(self.thing.getPositionFromBoard(self.icepapAddress, 'ShftEnc'))]
            except:
                if 'ShftEnc' in self.ac: self.ac.remove('ShftEnc')
                self.arrayShiftEncTime = []
                self.arrayShiftEnc = []
                print('Init error for ShftEnc!')
        else:
            if 'ShftEnc' in self.ac: self.ac.remove('ShftEnc')
            self.arrayShiftEncTime = []
            self.arrayShiftEnc = []
        print(self.ac)
        self.curveShiftEnc.setData(x=self.arrayShiftEncTime, y=self.arrayShiftEnc)

    def signalTargetEnc(self, checked):
        if checked == 2:
            try:
                if 'TgtEnc' not in self.ac: self.ac.append('TgtEnc')
                self.arrayTargetEncTime = [time.time()]
                self.arrayTargetEnc =[float(self.thing.getPositionFromBoard(self.icepapAddress, 'TgtEnc'))]
            except:
                if 'TgtEnc' in self.ac: self.ac.remove('TgtEnc')
                self.arrayTargetEncTime = []
                self.arrayTargetEnc = []
                print('Init error for TgtEnc!')
        else:
            if 'TgtEnc' in self.ac: self.ac.remove('TgtEnc')
            self.arrayTargetEncTime = []
            self.arrayTargetEnc = []
        print(self.ac)
        self.curveTargetEnc.setData(x=self.arrayTargetEncTime, y=self.arrayTargetEnc)

    def tick(self):
        now = time.time()
        self.pw.setXRange(now - self.xTimeLength, now)

        if 'Axis' in self.ac:
            try:
                self.arrayAxisTime.append(now)
                self.arrayAxis.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'Axis')))
            except:
                print('Failed to update Axis!')
            # if self.ui.checkBoxAxis.isChecked():
            #    curveAxis = self.pw.plot(x=self.arrayTime, y=self.arrayAxis)
            if len(self.arrayAxisTime) < self.numVisible:
                self.curveAxis.setData(x=self.arrayAxisTime, y=self.arrayAxis)
            else:
                self.curveAxis.setData(x=self.arrayAxisTime[-self.numVisible:], y=self.arrayAxis[-self.numVisible:])

        if 'ShftEnc' in self.ac:
            try:
                self.arrayShiftEncTime.append(now)
                self.arrayShiftEnc.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'ShftEnc')))
            except:
                print('Failed to update ShftEnc!')
            if len(self.arrayShiftEncTime) < self.numVisible:
                self.curveShiftEnc.setData(x=self.arrayShiftEncTime, y=self.arrayShiftEnc)
            else:
                self.curveShiftEnc.setData(x=self.arrayShiftEncTime[-self.numVisible:], y=self.arrayShiftEnc[-self.numVisible:])

        if 'TgtEnc' in self.ac:
            try:
                self.arrayTargetEncTime.append(now)
                self.arrayTargetEnc.append(float(self.thing.getPositionFromBoard(self.icepapAddress, 'TgtEnc')))
            except:
                print('Failed to update TgtEnc!')
            if len(self.arrayTargetEncTime) < self.numVisible:
                self.curveTargetEnc.setData(x=self.arrayTargetEncTime, y=self.arrayTargetEnc)
            else:
                self.curveTargetEnc.setData(x=self.arrayTargetEncTime[-self.numVisible:], y=self.arrayTargetEnc[-self.numVisible:])

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
