# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'icepapcms.ui'
#
# Created: Wed Jan 24 17:07:49 2018
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IcepapCMS(object):
    def setupUi(self, IcepapCMS):
        IcepapCMS.setObjectName(_fromUtf8("IcepapCMS"))
        IcepapCMS.resize(1200, 720)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IcepapCMS.sizePolicy().hasHeightForWidth())
        IcepapCMS.setSizePolicy(sizePolicy)
        IcepapCMS.setMinimumSize(QtCore.QSize(1200, 720))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(101, 148, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 148, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        IcepapCMS.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/small_icons/IcepapCfg Icons/Icepapicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IcepapCMS.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(IcepapCMS)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(1)
        self.vboxlayout.setMargin(1)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 613))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.StartPage = QtGui.QWidget()
        self.StartPage.setObjectName(_fromUtf8("StartPage"))
        self.hboxlayout = QtGui.QHBoxLayout(self.StartPage)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.lblStartPage = QtGui.QLabel(self.StartPage)
        self.lblStartPage.setText(_fromUtf8(""))
        self.lblStartPage.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos/IcepapCfg Icons/IcepapBig.png")))
        self.lblStartPage.setObjectName(_fromUtf8("lblStartPage"))
        self.hboxlayout.addWidget(self.lblStartPage)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.StartPage)
        self.vboxlayout.addWidget(self.stackedWidget)
        IcepapCMS.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(IcepapCMS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuDriver = QtGui.QMenu(self.menubar)
        self.menuDriver.setObjectName(_fromUtf8("menuDriver"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        IcepapCMS.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(IcepapCMS)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMovable(False)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        IcepapCMS.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockTree = QtGui.QDockWidget(IcepapCMS)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockTree.sizePolicy().hasHeightForWidth())
        self.dockTree.setSizePolicy(sizePolicy)
        self.dockTree.setMinimumSize(QtCore.QSize(341, 347))
        self.dockTree.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockTree.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockTree.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockTree.setObjectName(_fromUtf8("dockTree"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(51, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cbLocation = QtGui.QComboBox(self.frame)
        self.cbLocation.setMinimumSize(QtCore.QSize(100, 0))
        self.cbLocation.setMaximumSize(QtCore.QSize(141, 16777215))
        self.cbLocation.setEditable(False)
        self.cbLocation.setObjectName(_fromUtf8("cbLocation"))
        self.horizontalLayout.addWidget(self.cbLocation)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btnTreeAdd = QtGui.QToolButton(self.frame)
        self.btnTreeAdd.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/small_icons/IcepapCFG Icons Petits/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTreeAdd.setIcon(icon1)
        self.btnTreeAdd.setIconSize(QtCore.QSize(16, 16))
        self.btnTreeAdd.setObjectName(_fromUtf8("btnTreeAdd"))
        self.horizontalLayout_2.addWidget(self.btnTreeAdd)
        self.btnTreeRemove = QtGui.QToolButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/small_icons/IcepapCFG Icons Petits/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTreeRemove.setIcon(icon2)
        self.btnTreeRemove.setIconSize(QtCore.QSize(16, 16))
        self.btnTreeRemove.setObjectName(_fromUtf8("btnTreeRemove"))
        self.horizontalLayout_2.addWidget(self.btnTreeRemove)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.treeView = QtGui.QTreeView(self.dockWidgetContents)
        self.treeView.setIconSize(QtCore.QSize(22, 22))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout_2.addWidget(self.treeView, 1, 0, 1, 1)
        self.dockTree.setWidget(self.dockWidgetContents)
        IcepapCMS.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockTree)
        self.statusbar = QtGui.QStatusBar(IcepapCMS)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IcepapCMS.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(IcepapCMS)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionTree_Explorer = QtGui.QAction(IcepapCMS)
        self.actionTree_Explorer.setCheckable(True)
        self.actionTree_Explorer.setChecked(True)
        self.actionTree_Explorer.setObjectName(_fromUtf8("actionTree_Explorer"))
        self.actionGoNext = QtGui.QAction(IcepapCMS)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/go-next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoNext.setIcon(icon3)
        self.actionGoNext.setObjectName(_fromUtf8("actionGoNext"))
        self.actionGoPrevious = QtGui.QAction(IcepapCMS)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/go-previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoPrevious.setIcon(icon4)
        self.actionGoPrevious.setObjectName(_fromUtf8("actionGoPrevious"))
        self.actionGoUp = QtGui.QAction(IcepapCMS)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/go-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoUp.setIcon(icon5)
        self.actionGoUp.setObjectName(_fromUtf8("actionGoUp"))
        self.actionRefresh = QtGui.QAction(IcepapCMS)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon6)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionPreferences = QtGui.QAction(IcepapCMS)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/gnome-settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon7)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionHelp = QtGui.QAction(IcepapCMS)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/help-browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon8)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionExport = QtGui.QAction(IcepapCMS)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/gnome-dev-floppy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon9)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionImport = QtGui.QAction(IcepapCMS)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon10)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionQuit = QtGui.QAction(IcepapCMS)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/gnome-logout.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon11)
        self.actionQuit.setStatusTip(_fromUtf8(""))
        self.actionQuit.setWhatsThis(_fromUtf8(""))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionToolbar = QtGui.QAction(IcepapCMS)
        self.actionToolbar.setCheckable(True)
        self.actionToolbar.setChecked(True)
        self.actionToolbar.setObjectName(_fromUtf8("actionToolbar"))
        self.actionSaveConfig = QtGui.QAction(IcepapCMS)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/sign.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveConfig.setIcon(icon12)
        self.actionSaveConfig.setObjectName(_fromUtf8("actionSaveConfig"))
        self.actionFirmwareUpgrade = QtGui.QAction(IcepapCMS)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/gnome-cpu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirmwareUpgrade.setIcon(icon13)
        self.actionFirmwareUpgrade.setObjectName(_fromUtf8("actionFirmwareUpgrade"))
        self.actionConsole = QtGui.QAction(IcepapCMS)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/gnome-terminal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConsole.setIcon(icon14)
        self.actionConsole.setObjectName(_fromUtf8("actionConsole"))
        self.actionHistoricCfg = QtGui.QAction(IcepapCMS)
        self.actionHistoricCfg.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/calendar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistoricCfg.setIcon(icon15)
        self.actionHistoricCfg.setObjectName(_fromUtf8("actionHistoricCfg"))
        self.actionTemplates = QtGui.QAction(IcepapCMS)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/IcepapCfg Icons/notes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTemplates.setIcon(icon16)
        self.actionTemplates.setObjectName(_fromUtf8("actionTemplates"))
        self.actionAddIcepap = QtGui.QAction(IcepapCMS)
        self.actionAddIcepap.setIcon(icon1)
        self.actionAddIcepap.setObjectName(_fromUtf8("actionAddIcepap"))
        self.actionDeleteIcepap = QtGui.QAction(IcepapCMS)
        self.actionDeleteIcepap.setIcon(icon2)
        self.actionDeleteIcepap.setObjectName(_fromUtf8("actionDeleteIcepap"))
        self.actionUser_manual = QtGui.QAction(IcepapCMS)
        self.actionUser_manual.setObjectName(_fromUtf8("actionUser_manual"))
        self.actionHardware_manual = QtGui.QAction(IcepapCMS)
        self.actionHardware_manual.setObjectName(_fromUtf8("actionHardware_manual"))
        self.actionAddLocation = QtGui.QAction(IcepapCMS)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/small_icons/IcepapCFG Icons Petits/template.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddLocation.setIcon(icon17)
        self.actionAddLocation.setObjectName(_fromUtf8("actionAddLocation"))
        self.actionDeleteLocation = QtGui.QAction(IcepapCMS)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/small_icons/IcepapCFG Icons Petits/process-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteLocation.setIcon(icon18)
        self.actionDeleteLocation.setObjectName(_fromUtf8("actionDeleteLocation"))
        self.actionSetExpertFlag = QtGui.QAction(IcepapCMS)
        self.actionSetExpertFlag.setCheckable(True)
        self.actionSetExpertFlag.setObjectName(_fromUtf8("actionSetExpertFlag"))
        self.actionCopy = QtGui.QAction(IcepapCMS)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(IcepapCMS)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.menuHelp.addAction(self.actionUser_manual)
        self.menuHelp.addAction(self.actionHardware_manual)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionTree_Explorer)
        self.menuView.addAction(self.actionToolbar)
        self.menuDriver.addAction(self.actionSaveConfig)
        self.menuDriver.addSeparator()
        self.menuDriver.addAction(self.actionHistoricCfg)
        self.menuDriver.addAction(self.actionTemplates)
        self.menuDriver.addSeparator()
        self.menuDriver.addAction(self.actionExport)
        self.menuDriver.addAction(self.actionImport)
        self.menuDriver.addSeparator()
        self.menuDriver.addAction(self.actionCopy)
        self.menuDriver.addAction(self.actionPaste)
        self.menuDriver.addSeparator()
        self.menuDriver.addAction(self.actionSetExpertFlag)
        self.menuFile.addAction(self.actionAddLocation)
        self.menuFile.addAction(self.actionDeleteLocation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAddIcepap)
        self.menuFile.addAction(self.actionDeleteIcepap)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFirmwareUpgrade)
        self.menuFile.addAction(self.actionConsole)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDriver.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionGoPrevious)
        self.toolBar.addAction(self.actionGoNext)
        self.toolBar.addAction(self.actionGoUp)
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionSaveConfig)
        self.toolBar.addAction(self.actionHistoricCfg)
        self.toolBar.addAction(self.actionTemplates)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addAction(self.actionConsole)
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(IcepapCMS)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IcepapCMS)

    def retranslateUi(self, IcepapCMS):
        IcepapCMS.setWindowTitle(_translate("IcepapCMS", "Icepap configuration", None))
        self.menuHelp.setTitle(_translate("IcepapCMS", "Help", None))
        self.menuView.setTitle(_translate("IcepapCMS", "View", None))
        self.menuDriver.setTitle(_translate("IcepapCMS", "Driver", None))
        self.menuFile.setTitle(_translate("IcepapCMS", "File", None))
        self.toolBar.setWindowTitle(_translate("IcepapCMS", "Toolbar", None))
        self.dockTree.setWindowTitle(_translate("IcepapCMS", "Tree Explorer", None))
        self.label.setText(_translate("IcepapCMS", "Location", None))
        self.label_2.setText(_translate("IcepapCMS", "Add / Remove Icepap System", None))
        self.btnTreeRemove.setText(_translate("IcepapCMS", "...", None))
        self.actionAbout.setText(_translate("IcepapCMS", "About", None))
        self.actionTree_Explorer.setText(_translate("IcepapCMS", "Tree Explorer", None))
        self.actionTree_Explorer.setShortcut(_translate("IcepapCMS", "F8", None))
        self.actionGoNext.setText(_translate("IcepapCMS", "Go Next", None))
        self.actionGoNext.setStatusTip(_translate("IcepapCMS", "444", None))
        self.actionGoNext.setWhatsThis(_translate("IcepapCMS", "5555", None))
        self.actionGoNext.setShortcut(_translate("IcepapCMS", "Alt+Right", None))
        self.actionGoPrevious.setText(_translate("IcepapCMS", "Go Previous", None))
        self.actionGoPrevious.setShortcut(_translate("IcepapCMS", "Alt+Left", None))
        self.actionGoUp.setText(_translate("IcepapCMS", "Go Up", None))
        self.actionGoUp.setShortcut(_translate("IcepapCMS", "Alt+Up", None))
        self.actionRefresh.setText(_translate("IcepapCMS", "Refresh", None))
        self.actionRefresh.setShortcut(_translate("IcepapCMS", "F5", None))
        self.actionPreferences.setText(_translate("IcepapCMS", "Preferences", None))
        self.actionHelp.setText(_translate("IcepapCMS", "Help", None))
        self.actionHelp.setShortcut(_translate("IcepapCMS", "F1", None))
        self.actionExport.setText(_translate("IcepapCMS", "Export configuration", None))
        self.actionExport.setIconText(_translate("IcepapCMS", "Export configuration", None))
        self.actionExport.setToolTip(_translate("IcepapCMS", "Export driver configuration to file", None))
        self.actionExport.setShortcut(_translate("IcepapCMS", "Ctrl+E", None))
        self.actionImport.setText(_translate("IcepapCMS", "Import configuration", None))
        self.actionImport.setIconText(_translate("IcepapCMS", "Import configuration", None))
        self.actionImport.setToolTip(_translate("IcepapCMS", "Import driver configuration from file", None))
        self.actionImport.setShortcut(_translate("IcepapCMS", "Ctrl+I", None))
        self.actionQuit.setText(_translate("IcepapCMS", "Quit", None))
        self.actionQuit.setShortcut(_translate("IcepapCMS", "Ctrl+Q", None))
        self.actionToolbar.setText(_translate("IcepapCMS", "Toolbar", None))
        self.actionToolbar.setShortcut(_translate("IcepapCMS", "F9", None))
        self.actionSaveConfig.setText(_translate("IcepapCMS", "Save Configuration", None))
        self.actionSaveConfig.setToolTip(_translate("IcepapCMS", "Save driver configuration", None))
        self.actionSaveConfig.setStatusTip(_translate("IcepapCMS", "Ctrl+s", None))
        self.actionSaveConfig.setShortcut(_translate("IcepapCMS", "Ctrl+S", None))
        self.actionFirmwareUpgrade.setText(_translate("IcepapCMS", "Firmware upgrade", None))
        self.actionFirmwareUpgrade.setToolTip(_translate("IcepapCMS", "Open Firmware upgrade dialog", None))
        self.actionConsole.setText(_translate("IcepapCMS", "Console", None))
        self.actionConsole.setToolTip(_translate("IcepapCMS", "Icepap Console", None))
        self.actionHistoricCfg.setText(_translate("IcepapCMS", "Historic Configurations", None))
        self.actionHistoricCfg.setIconText(_translate("IcepapCMS", "Historic Configurations", None))
        self.actionHistoricCfg.setToolTip(_translate("IcepapCMS", "Historic configurations per driver", None))
        self.actionHistoricCfg.setShortcut(_translate("IcepapCMS", "Ctrl+H", None))
        self.actionTemplates.setText(_translate("IcepapCMS", "Templates", None))
        self.actionTemplates.setToolTip(_translate("IcepapCMS", "Template managment", None))
        self.actionTemplates.setShortcut(_translate("IcepapCMS", "Ctrl+T", None))
        self.actionAddIcepap.setText(_translate("IcepapCMS", "Add Icepap", None))
        self.actionAddIcepap.setToolTip(_translate("IcepapCMS", "Add Icepap System to CMS Database", None))
        self.actionDeleteIcepap.setText(_translate("IcepapCMS", "Delete Icepap", None))
        self.actionDeleteIcepap.setToolTip(_translate("IcepapCMS", "Delete Icepap System from the CMS Database", None))
        self.actionUser_manual.setText(_translate("IcepapCMS", "User manual", None))
        self.actionHardware_manual.setText(_translate("IcepapCMS", "Hardware manual", None))
        self.actionAddLocation.setText(_translate("IcepapCMS", "Add location", None))
        self.actionAddLocation.setIconText(_translate("IcepapCMS", "Add location", None))
        self.actionAddLocation.setToolTip(_translate("IcepapCMS", "Add location", None))
        self.actionDeleteLocation.setText(_translate("IcepapCMS", "Delete location", None))
        self.actionDeleteLocation.setIconText(_translate("IcepapCMS", "Delete location", None))
        self.actionDeleteLocation.setToolTip(_translate("IcepapCMS", "Delete location", None))
        self.actionSetExpertFlag.setText(_translate("IcepapCMS", "Set Expert Flag", None))
        self.actionCopy.setText(_translate("IcepapCMS", "Copy configuration", None))
        self.actionCopy.setShortcut(_translate("IcepapCMS", "Ctrl+C", None))
        self.actionPaste.setText(_translate("IcepapCMS", "Paste configuration", None))
        self.actionPaste.setShortcut(_translate("IcepapCMS", "Ctrl+V", None))

import icepapcms_rc
