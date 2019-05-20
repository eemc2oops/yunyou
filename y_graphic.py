# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tickets_main_window(object):
    def setupUi(self, tickets_main_window):
        tickets_main_window.setObjectName("tickets_main_window")
        tickets_main_window.resize(1188, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/animal_bird_sc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tickets_main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(tickets_main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tickets_display_table = QtWidgets.QTableWidget(self.centralwidget)
        self.tickets_display_table.setGeometry(QtCore.QRect(35, 220, 1121, 321))
        self.tickets_display_table.setGridStyle(QtCore.Qt.DotLine)
        self.tickets_display_table.setObjectName("tickets_display_table")
        self.tickets_display_table.setColumnCount(0)
        self.tickets_display_table.setRowCount(0)
        self.query_button = QtWidgets.QPushButton(self.centralwidget)
        self.query_button.setGeometry(QtCore.QRect(890, 170, 75, 23))
        self.query_button.setObjectName("query_button")
        tickets_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tickets_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 23))
        self.menubar.setObjectName("menubar")
        tickets_main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tickets_main_window)
        self.statusbar.setObjectName("statusbar")
        tickets_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(tickets_main_window)
        QtCore.QMetaObject.connectSlotsByName(tickets_main_window)

    def retranslateUi(self, tickets_main_window):
        _translate = QtCore.QCoreApplication.translate
        tickets_main_window.setWindowTitle(_translate("tickets_main_window", "票"))
        self.query_button.setText(_translate("tickets_main_window", "查询"))

