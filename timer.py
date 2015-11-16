# -*- coding: utf-8 -*-

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(628, 691)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setNumDigits(2)
        self.lcdNumber_2.setProperty("intValue", 60)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.horizontalLayout.addWidget(self.lcdNumber_2)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setNumDigits(2)
        self.lcdNumber.setProperty("intValue", 60)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.tstart = QtGui.QPushButton(self.centralwidget)
        self.tstart.setObjectName(_fromUtf8("tstart"))
        self.verticalLayout_3.addWidget(self.tstart)
        self.tpause = QtGui.QPushButton(self.centralwidget)
        self.tpause.setObjectName(_fromUtf8("tpause"))
        self.verticalLayout_3.addWidget(self.tpause)
        self.tstop = QtGui.QPushButton(self.centralwidget)
        self.tstop.setObjectName(_fromUtf8("tstop"))
        self.verticalLayout_3.addWidget(self.tstop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.wifi = QtGui.QPushButton(self.centralwidget)
        self.wifi.setObjectName(_fromUtf8("wifi"))
        self.verticalLayout_2.addWidget(self.wifi)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.mchanger = QtGui.QPushButton(self.centralwidget)
        self.mchanger.setObjectName(_fromUtf8("mchanger"))
        self.verticalLayout_2.addWidget(self.mchanger)
        self.mreset = QtGui.QPushButton(self.centralwidget)
        self.mreset.setObjectName(_fromUtf8("mreset"))
        self.verticalLayout_2.addWidget(self.mreset)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MaC-Changer", None))
        self.label.setText(_translate("MainWindow", "Aki iria un log en toda esta sexion", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.tstart.setText(_translate("MainWindow", "start", None))
        self.tpause.setText(_translate("MainWindow", "PushButton", None))
        self.tstop.setText(_translate("MainWindow", "stop and reset", None))
        self.wifi.setText(_translate("MainWindow", "put down wlan0", None))
        self.pushButton.setText(_translate("MainWindow", "put up wlan0", None))
        self.mchanger.setText(_translate("MainWindow", "random mac", None))
        self.mreset.setText(_translate("MainWindow", "default mac", None))
