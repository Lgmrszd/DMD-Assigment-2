# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query6.ui'
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
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tblFrom = QtWidgets.QTableWidget(self.centralwidget)
        self.tblFrom.setObjectName("tblFrom")
        self.tblFrom.setColumnCount(3)
        self.tblFrom.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblFrom.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblFrom.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblFrom.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tblFrom)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tblTo = QtWidgets.QTableWidget(self.centralwidget)
        self.tblTo.setObjectName("tblTo")
        self.tblTo.setColumnCount(3)
        self.tblTo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblTo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTo.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tblTo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "From:"))
        item = self.tblFrom.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Start time"))
        item = self.tblFrom.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "End time"))
        item = self.tblFrom.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        self.label_2.setText(_translate("MainWindow", "To:"))
        item = self.tblTo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Starit time"))
        item = self.tblTo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "End time"))
        item = self.tblTo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "location"))

