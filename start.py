import sys
import os
import time
from timer import *
from PyQt4 import QtGui

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """self.ui.tstart.clicked.connect(self.timer_start)"""
        self.ui.mchanger.clicked.connect(self.mac_randomizer)
        self.ui.wifi.clicked.connect(self.wifi_off)
        self.ui.mreset.clicked.connect(self.mac_default)
        self.ui.tstart.clicked.connect(self.timer_start)

    def timer_start(self):
        sec = 60
        mt = 60
        while mt > 0 and mt <= 60:
            time.sleep(1)
            sec = sec - 1
            print sec
            if sec == 0:
                mt = mt - 1
                sec = 60
                print mt
            if mt == 0:
                os.system("'gksu' 'macchanger -r wlan0'")
                """ tambien se puede usar la clase ya creada mac_randomizer"""
                mt == 60


    def mac_default(self):
        os.system("'gksu' 'macchanger -p wlan0'")



    def wifi_off(self):
        os.system("'gksu' 'ifconfig wlan0 down'")

    def mac_randomizer(self):
        os.system("'gksu' 'macchanger -r wlan0'")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

