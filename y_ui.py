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
        self.count = 0

    def setupUi(self):
        '''初始化ui'''
        # 先初始化基类的ui
        super(tickets_ui, self).setupUi(self)
        # 再创建自已的UI信息
        # table行列定义
        self.tickets_display_table.setRowCount(0)    # 行
        self.tickets_display_table.setColumnCount(11)  # 列
        self.tickets_display_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设置只读
        self.tickets_display_table.setHorizontalHeaderLabels(['from', 'to', 'date', 'price', 'flyno', 'airtype', 'departuretime', 'arrivaltime', 'refer', 'url', 'airline'])  # 设置表头

    def set_table_show(self, ticket):
        '''表中插入票务信息'''
        row_count = self.tickets_display_table.rowCount()
        self.tickets_display_table.insertRow(row_count)
        self.tickets_display_table.setItem(row_count, 0, QTableWidgetItem(ticket['from']))
        self.tickets_display_table.setItem(row_count, 1, QTableWidgetItem(ticket['to']))
        self.tickets_display_table.setItem(row_count, 2, QTableWidgetItem(ticket['date']))
        self.tickets_display_table.setItem(row_count, 3, QTableWidgetItem('%d' % ticket['price']))
        self.tickets_display_table.setItem(row_count, 4, QTableWidgetItem(ticket['flyno']))
        self.tickets_display_table.setItem(row_count, 5, QTableWidgetItem(ticket['airtype']))
        self.tickets_display_table.setItem(row_count, 6, QTableWidgetItem(ticket['departuretime']))
        self.tickets_display_table.setItem(row_count, 7, QTableWidgetItem(ticket['arrivaltime']))
        self.tickets_display_table.setItem(row_count, 8, QTableWidgetItem(ticket['refer']))
        self.tickets_display_table.setItem(row_count, 9, QTableWidgetItem(ticket['url']))
        self.tickets_display_table.setItem(row_count, 10, QTableWidgetItem(ticket['airline']))

    def test_show_ticket1(self):
        ticket = {
            'from' : '武汉',
            'to' : '上海',
            'date' : '20200202',
            'price' : 12345,
            'airtype' : 'a330',
            'flytime' : '1h5m',
            'flyno' : 'h6576',
            'departuretime' : '12:36',
            'arrivaltime' : '17:12',
            'refer' : 'chunqiu',
            'url' : 'www.sina.com.cn',
            'airline' : '春秋',
        }
        self.set_table_show(ticket)
        ticket['price'] = 234566
        self.set_table_show(ticket)
        ticket['price'] = 345566
        self.set_table_show(ticket)
        
    def test_show_ticket2(self):
        ticket = {
            'from' : '北京',
            'to' : '成都',
            'date' : '20200202',
            'price' : 97856,
            'airtype' : 'a330',
            'flytime' : '1h5m',
            'flyno' : 'c88573',
            'departuretime' : '12:36',
            'arrivaltime' : '17:12',
            'refer' : 'chunqiu',
            'url' : 'www.sina.com.cn',
            'airline' : '春秋',
        }
        self.set_table_show(ticket)
        ticket['price'] = 86754
        self.set_table_show(ticket)
        ticket['price'] = 642523
        self.set_table_show(ticket)
        ticket['price'] = 534421
        self.set_table_show(ticket)
        ticket['price'] = 4321
        self.set_table_show(ticket)
        ticket['price'] = 12341
        self.set_table_show(ticket)
        ticket['price'] = 534435676
        self.set_table_show(ticket)
        ticket['price'] = 9345762
        self.set_table_show(ticket)
        ticket['price'] = 12957
        self.set_table_show(ticket)
        ticket['price'] = 53646
        self.set_table_show(ticket)
        ticket['price'] = 6543158
        self.set_table_show(ticket)
        ticket['price'] = 35679
        self.set_table_show(ticket)
        ticket['price'] = 97887456
        self.set_table_show(ticket)
        ticket['price'] = 1546
        self.set_table_show(ticket)
        ticket['price'] = 345646
        self.set_table_show(ticket)

    @pyqtSlot()
    def on_tickets_display_table_cellEntered(self, row, column):
        '''显示表格的click信号处理槽函数'''
        w2l.info('table clieck at {} {}'.format(row, column))

    @pyqtSlot()
    def on_query_button_clicked(self):
        '''查询按钮'''
        w2l.info('press button')
        # 点击查询，先清空显示列表
        self.tickets_display_table.clearContents()
        self.tickets_display_table.setRowCount(0)
        # 获取对话框输入的地址
        from_city = self.from_lineedit.text()
        to_city = self.to_lineedit.text()
        w2l.error('input  from \'%s\'   to \'%s\'  ' % (from_city, to_city))
        if from_city == '' or to_city == '':
            # 如果输入是空，则提示以后退出查询
            #reply = QMessageBox.about(self, '提示', '请输入出发地和目的地', QMessageBox.Yes)
            #if reply == QMessageBox.Yes:
            #    return
            QMessageBox.about(self, '提示', '请输入出发地和目的地')
            return
        
        if self.count == 0:
            self.test_show_ticket2()
        else:
            self.test_show_ticket1()
            
        self.count = self.count + 1
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
