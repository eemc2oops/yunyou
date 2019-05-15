import y_log
import y_air_ticket

w2l = y_log.clog(__name__ == "__main__")

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

import air

class Ico(QWidget):

    def __init__(self):
        super().__init__()
    
        self.initUI()    
    
    def initUI(self):
    
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧出品')
        self.setWindowIcon(QIcon('animal_bird_sc.ico'))
    
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setGeometry(70, 30, 50, 50)
        #qbtn.resize(70,30)
        #qbtn.move(50, 50)
    
        self.show()

def test_gui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = air.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    #app = QApplication(sys.argv)
    #ex = Ico()
    #sys.exit(app.exec_())

class airgui:
    def __init__(self):
        pass

    def test(self):
        pass

def run_entry():
    w2l.info("{0} run.".format(__name__))

    test_gui()

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()
