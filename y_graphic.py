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
        tickets_main_window.resize(788, 626)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/animal_bird_sc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tickets_main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(tickets_main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 560, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.tickets_display_table = QtWidgets.QTableWidget(self.centralwidget)
        self.tickets_display_table.setObjectName("tickets_display_table")
        self.tickets_display_table.setColumnCount(0)
        self.tickets_display_table.setRowCount(0)
        self.horizontalLayout.addWidget(self.tickets_display_table)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        tickets_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tickets_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 23))
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

