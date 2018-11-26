# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.verticalLayout.addWidget(self.btnSearch)
        self.tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl.setObjectName("tbl")
        self.tbl.setColumnCount(2)
        self.tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tbl)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        item = self.tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Car ID"))

