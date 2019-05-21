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
        tickets_main_window.resize(1279, 597)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/animal_bird_sc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tickets_main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(tickets_main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tickets_display_table = QtWidgets.QTableWidget(self.centralwidget)
        self.tickets_display_table.setGeometry(QtCore.QRect(35, 220, 1211, 321))
        self.tickets_display_table.setGridStyle(QtCore.Qt.DotLine)
        self.tickets_display_table.setObjectName("tickets_display_table")
        self.tickets_display_table.setColumnCount(0)
        self.tickets_display_table.setRowCount(0)
        self.query_button = QtWidgets.QPushButton(self.centralwidget)
        self.query_button.setGeometry(QtCore.QRect(910, 180, 75, 23))
        self.query_button.setObjectName("query_button")
        self.from_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.from_lineedit.setGeometry(QtCore.QRect(130, 28, 113, 20))
        self.from_lineedit.setObjectName("from_lineedit")
        self.from_label = QtWidgets.QLabel(self.centralwidget)
        self.from_label.setGeometry(QtCore.QRect(80, 30, 54, 21))
        self.from_label.setObjectName("from_label")
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(280, 30, 54, 21))
        self.to_label.setObjectName("to_label")
        self.to_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.to_lineedit.setGeometry(QtCore.QRect(330, 28, 113, 20))
        self.to_lineedit.setObjectName("to_lineedit")
        tickets_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tickets_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1279, 23))
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
        self.from_label.setText(_translate("tickets_main_window", "出发地："))
        self.to_label.setText(_translate("tickets_main_window", "目的地："))

