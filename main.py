import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

import gui  # Это наш конвертированный файл дизайна
import db_backend as db


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.tblChargSt.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblChargSt.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblCars.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblCars.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblCustomers.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblCustomers.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblOrders.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblOrders.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblPayment.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblPayment.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblWorkshop.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblWorkshop.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblParts.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblParts.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblProviders.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblProviders.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblDetails.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblDetails.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblRepairs.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblRepairs.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblChargSt.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblChargSt.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblCharges.horizontalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.tblCharges.verticalHeader().sectionResizeMode(QHeaderView.ResizeToContents)
        self.init_cars()
        self.init_customers()
        self.init_orders()
        self.init_payment()
        self.init_workshop()
        self.init_parts()
        self.init_providers()
        self.init_details()
        self.init_repairs()
        self.init_charging_station()
        self.init_charges()

    def init_cars(self):
        ans = db.cars_select()
        self.tblCars.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblCars.setItem(i, j, QTableWidgetItem(value))

    def init_customers(self):
        ans = db.customers_select()
        self.tblCustomers.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblCustomers.setItem(i, j, QTableWidgetItem(value))

    def init_orders(self):
        ans = db.orders_select()
        self.tblOrders.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblOrders.setItem(i, j, QTableWidgetItem(str(value)))

    def init_payment(self):
        ans = db.payment_select()
        self.tblPayment.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblPayment.setItem(i, j, QTableWidgetItem(str(value)))

    def init_workshop(self):
        ans = db.workshops_select()
        self.tblWorkshop.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblWorkshop.setItem(i, j, QTableWidgetItem(str(value)))

    def init_parts(self):
        ans = db.parts_in_workshop_select()
        self.tblParts.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblParts.setItem(i, j, QTableWidgetItem(str(value)))

    def init_providers(self):
        ans = db.parts_providers_select()
        self.tblProviders.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblProviders.setItem(i, j, QTableWidgetItem(str(value)))

    def init_details(self):
        ans = db.can_provide_select()
        self.tblDetails.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblDetails.setItem(i, j, QTableWidgetItem(str(value)))

    def init_repairs(self):
        ans = db.repairs_select()
        self.tblRepairs.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblRepairs.setItem(i, j, QTableWidgetItem(str(value)))

    def init_charging_station(self):
        ans = db.charging_stations_select()
        self.tblChargSt.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                if j == 1:
                    value = str(value).split("; ")
                    table = QtWidgets.QTableWidget()
                    table.setRowCount(len(value))
                    table.setColumnCount(2)
                    for k, smth  in enumerate(value):
                        smth = smth.split("-")
                        table.setItem(k, 0, QTableWidgetItem(smth[0]))
                        table.setItem(k, 1, QTableWidgetItem(smth[1]))
                    self.tblChargSt.setCellWidget(i, j, table)

                else:
                    self.tblChargSt.setItem(i, j, QTableWidgetItem(str(value)))
        #table.verticalHeader().setStretchLastSection(True)

    def init_charges(self):
        ans = db.charges_select()
        self.tblCharges.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblCharges.setItem(i, j, QTableWidgetItem(str(value)))


def main():
    db.init()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()