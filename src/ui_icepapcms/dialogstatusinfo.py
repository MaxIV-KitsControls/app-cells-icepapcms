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
        self.getStatusInfo()

    def connectSignals(self):
        self.ui.btnUpdate.pressed.connect(self.getStatusInfo)
        self.ui.btnUpdate.pressed.connect(self.resetReg)

    def getStatusInfo(self):
        val = self.driver.getVStatus(self.icepapAddress)
        self.ui.textBrowser.setText(val)

    def resetReg(self):
        pass
