from PyQt4 import QtGui
from ui_trajectory import Ui_trajectory
from lib_icepapcms import MainManager


# A tab used for displaying motor position information etc.
class TabTrajectory(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_trajectory()
        self.ui.setupUi(self)

    def update_status(self, icepap_driver, pos_sel, enc_sel):
        manager = MainManager()
        (status, power, position) = manager.getDriverTestStatus(icepap_driver.icepapsystem_name, icepap_driver.addr, pos_sel, enc_sel)

