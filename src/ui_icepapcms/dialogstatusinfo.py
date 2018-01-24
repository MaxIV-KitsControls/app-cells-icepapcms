from PyQt4 import QtGui
from ui_dialogstatusinfo import Ui_DialogStatusInfo
from lib_icepapcms import IcepapController
from PyQt4 import QtCore, Qt


class DialogStatusInfo(QtGui.QDialog):

    def __init__(self, parent, drv):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DialogStatusInfo()
        self.driver = IcepapController().iPaps[drv.icepapsystem_name]
        self.icepapAddress = drv.addr
        self.ui.setupUi(self)
        self.setWindowTitle('Status Info  |  ' + drv.icepapsystem_name + '  |  ' + str(self.icepapAddress) + ' ' + drv.name)
        self.show()
        self.connectSignals()
        self.doVstatus()
        self.allDriversCommands = ['?cfg extdisable', '?ver info', '?power',
                                   '?positions', '?warning', '?isg ?ssierrtoggles',
                                   '#isg ssiwarningrst', 'm ?ver info', 'm ?rdispol'
                                   ]
        for cmd in self.allDriversCommands:
            self.ui.cbAllDrivers.addItem(cmd)


    def connectSignals(self):
        self.ui.btnUpdate.clicked.connect(self.doVstatus)
        self.ui.btnEsync.clicked.connect(self.doEsync)
        self.ui.btnUpdate.setDefault(False)
        self.ui.btnEsync.setDefault(False)
        self.ui.btnUpdate.setAutoDefault(False)
        self.ui.btnEsync.setAutoDefault(False)
        self.ui.txt1Command.returnPressed.connect(self.sendCommand)
        #self.ui.txt1Command.returnPressed.connect(lambda: self.sendCommand())
        #self.ui.txt1Command.returnPressed()
        QtCore.QObject.connect(self.ui.txt1Command,QtCore.SIGNAL("editingFinished()"),self.sendCommand)
        self.ui.cbAllDrivers.activated.connect(self.sendCommandToDrivers)
        #QtCore.QObject.connect(self.ui.txt1Command,QtCore.SIGNAL("returnPressed()"),self.sendCommand)
        #self.ui.btnCommand.clicked.connect(self.sendCommand)



    def doVstatus(self):
        val = ""
        try:
            val = self.driver.getVStatus(self.icepapAddress)
        except Exception, e:
            print(e)
        self.ui.textBrowser.setText(val)

    def doEsync(self):
        try:
            self.driver.syncEncoders(self.icepapAddress)
        except Exception, e:
            print(e)

    def sendCommand(self):
        val = ""
        comm = ""
        try:

            #val = self.ui.txt1Command.text()
            comm = "" + str(self.ui.txt1Command.text())
            print comm
            val = self.driver.getVStatus(self.icepapAddress)
            val = self.driver.sendWriteReadCommand(comm)
            #val = IcepapController().iPaps[self.icepap_driver.icepapsystem_name].
            print val
        except Exception, e:
            print(e)
        self.ui.textBrowser.setText(comm + "\n" + val)

    def sendCommandToDrivers(self):
        sel = '%s'%self.ui.cbAllDrivers.currentText()
        print sel
        txt = ''
        if sel == '?positions':
            print 'pos'
            header = 'dr name axis absenc encin inpos tgtenc'
            txt = header + '\n'
            for driver in self.driver.getDriversAlive():
                try:
                    val0 = self.driver.getName(driver)
                    val1 = self.driver.getPositionFromBoard(driver, 'AXIS')
                    val2 = self.driver.getEncoder(driver, 'ABSENC')
                    val3 = self.driver.getEncoder(driver, 'ENCIN')
                    val4 = self.driver.getEncoder(driver, 'INPOS')
                    val5 = self.driver.getCfgParameter(driver, 'TGTENC')
                    if val0 == '': val0 = 'noname'
                    txt = txt + '%s '%driver + '%s '%val0 + '%s '%val1 + '%s '%val2 + '%s '%val3 + '%s '%val4 + '%s '%val5 + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
        elif sel == '?ver info':
            for driver in self.driver.getDriversAlive():
                try:
                    val = self.driver.getVersionInfoDict(driver)
                    txt = txt + '%s '%driver + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel == 'm ?ver info':
            for contr in self.driver.getRacksAlive():
                try:
                    val = self.driver.getVersionInfoDict(contr)
                    txt = txt + '%s '%contr + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel.startswith('m '):
            print 'master'
            contr_comm = sel.replace('m ', '')
            for contr in self.driver.getRacksAlive():
                try:
                    comm = ('%s:%s')%(contr, contr_comm)
                    val = self.driver.sendWriteReadCommand(comm)
                    txt = txt + '%s '%contr + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        else:
            for driver in self.driver.getDriversAlive():
                try:
                    comm = ('%s:%s')%(driver, self.ui.cbAllDrivers.currentText())
                    val = self.driver.sendWriteReadCommand(comm)
                    txt = txt + '%s '%driver + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)



