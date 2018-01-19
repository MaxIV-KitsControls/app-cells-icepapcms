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

    def connectSignals(self):
        self.ui.btnUpdate.clicked.connect(self.doVstatus)
        self.ui.btnEsync.clicked.connect(self.doEsync)
        self.ui.txt1Command.returnPressed.connect(self.sendCommand)
        #self.ui.txt1Command.returnPressed()
        QtCore.QObject.connect(self.ui.txt1Command,QtCore.SIGNAL("editingFinished()"),self.sendCommand)
        QtCore.QObject.connect(self.ui.txt1Command,QtCore.SIGNAL("returnPressed()"),self.sendCommand)
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

