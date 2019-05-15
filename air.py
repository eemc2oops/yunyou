# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'air.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("animal_panda.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.air_tickets_table = QtWidgets.QTableWidget(self.centralwidget)
        self.air_tickets_table.setGeometry(QtCore.QRect(50, 190, 681, 281))
        self.air_tickets_table.setObjectName("air_tickets_table")
        self.air_tickets_table.setColumnCount(0)
        self.air_tickets_table.setRowCount(0)
        self.quit_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_push_button.setGeometry(QtCore.QRect(120, 90, 75, 23))
        self.quit_push_button.setObjectName("quit_push_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quit_push_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "机票"))
        self.quit_push_button.setText(_translate("MainWindow", "quit"))

