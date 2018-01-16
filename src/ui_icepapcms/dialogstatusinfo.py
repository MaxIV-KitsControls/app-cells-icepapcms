from PyQt4 import QtGui
from ui_dialogstatusinfo import Ui_DialogStatusInfo
from lib_icepapcms import IcepapController


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
        self.ui.btnUpdate.pressed.connect(self.doVstatus)
        self.ui.btnEsync.pressed.connect(self.doEsync)

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
