import y_log
import y_air_ticket

w2l = y_log.clog(__name__ == "__main__")

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from random import randint
import sys

from y_graphic import Ui_tickets_main_window


class tickets_ui(QMainWindow, Ui_tickets_main_window):
    def __init__(self, parent=None):
        super(tickets_ui, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        '''初始化ui'''
        # 先初始化基类的ui
        super(tickets_ui, self).setupUi(self)
        
        # 再创建自已的UI信息

    @pyqtSlot()
    def on_tickets_display_table_cellEntered(self, row, column):
        '''显示表格的click信号处理槽函数'''
        w2l.info('table clieck at {} {}'.format(row, column))
        pass

def test_designer():
    app = QApplication(sys.argv)
    ui = tickets_ui()
    ui.show()
    sys.exit(app.exec_())

def test_gui():
    test_designer()

class airgui:
    def __init__(self):
        pass

    def test(self):
        pass

def test_data():
    names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

    positions = [(i,j) for i in range(4,9) for j in range(4,8)]
    for position, name in zip(positions, names):
        print(position, name)

def run_entry():
    w2l.info("{0} run.".format(__name__))

    test_data()
    test_gui()

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()
