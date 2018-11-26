import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

import gui  # Это наш конвертированный файл дизайна
import query1
import query2
import query3
import query4
import query5
import query6
import query7
import query8
import query9
import query10
import db_backend as db



class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
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
        self.tblChargSt.resizeColumnsToContents()
        self.tblCars.resizeColumnsToContents()
        self.tblCustomers.resizeColumnsToContents()
        self.tblOrders.resizeColumnsToContents()
        self.tblPayment.resizeColumnsToContents()
        self.tblWorkshop.resizeColumnsToContents()
        self.tblParts.resizeColumnsToContents()
        self.tblProviders.resizeColumnsToContents()
        self.tblDetails.resizeColumnsToContents()
        self.tblRepairs.resizeColumnsToContents()
        self.tblChargSt.resizeColumnsToContents()
        self.tblChargSt.resizeRowsToContents()
        self.tblCharges.resizeColumnsToContents()
        self.btnQ1.clicked.connect(self.show_query_1)
        self.btnQ2.clicked.connect(self.show_query_2)
        self.btnQ3.clicked.connect(self.show_query_3)
        self.btnQ4.clicked.connect(self.show_query_4)
        self.btnQ5.clicked.connect(self.show_query_5)
        self.btnQ6.clicked.connect(self.show_query_6)
        self.btnQ7.clicked.connect(self.show_query_7)
        self.btnQ8.clicked.connect(self.show_query_8)
        self.btnQ9.clicked.connect(self.show_query_9)
        self.btnQ10.clicked.connect(self.show_query_10)

    def show_query_1(self):
        self.q1 = Query1()
        self.q1.show()

    def show_query_2(self):
        self.q2 = Query2()
        self.q2.show()

    def show_query_3(self):
        self.q3 = Query3()
        self.q3.show()

    def show_query_4(self):
        self.q4 = Query4()
        self.q4.show()

    def show_query_5(self):
        self.q5 = Query5()
        self.q5.show()

    def show_query_6(self):
        self.q6 = Query6()
        self.q6.show()

    def show_query_7(self):
        self.q7 = Query7()
        self.q7.show()

    def show_query_8(self):
        self.q8 = Query8()
        self.q8.show()

    def show_query_9(self):
        self.q9 = Query9()
        self.q9.show()

    def show_query_10(self):
        self.q10 = Query10()
        self.q10.show()

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
                    for k, smth in enumerate(value):
                        smth = smth.split("-")
                        table.setItem(k, 0, QTableWidgetItem(smth[0]))
                        table.setItem(k, 1, QTableWidgetItem(smth[1]))
                    self.tblChargSt.setCellWidget(i, j, table)

                else:
                    self.tblChargSt.setItem(i, j, QTableWidgetItem(str(value)))

    def init_charges(self):
        ans = db.charges_select()
        self.tblCharges.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tblCharges.setItem(i, j, QTableWidgetItem(str(value)))


class Query1(QtWidgets.QMainWindow, query1.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 1')
        self.setupUi(self)
        val = db.query1()
        for i in range(len(val)):
            self.textBrowser.append(val[i][0])


class Query2(QtWidgets.QMainWindow, query2.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 2')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        ans = db.query2(self.lineEdit.text())
        self.tableWidget.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()


class Query3(QtWidgets.QMainWindow, query3.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 3')
        self.setupUi(self)


class Query4(QtWidgets.QMainWindow, query4.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 4')
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.search)

    def search(self):
        ans = db.query4(self.lineEdit.text())
        self.tbl.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tbl.setItem(i, j, QTableWidgetItem(str(value)))
        self.tbl.resizeRowsToContents()
        self.tbl.resizeColumnsToContents()


class Query5(QtWidgets.QMainWindow, query5.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 5')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        ans = db.query5(self.lineEdit.text())
        self.tableWidget.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()


class Query6(QtWidgets.QMainWindow, query6.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 6')
        self.setupUi(self)


class Query7(QtWidgets.QMainWindow, query7.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 7')
        self.setupUi(self)
        val = db.query7()
        for i in range(len(val)):
            self.textBrowser.append(val[i][0])


class Query8(QtWidgets.QMainWindow, query8.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 8')
        self.setupUi(self)


class Query9(QtWidgets.QMainWindow, query9.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 9')
        self.setupUi(self)


class Query10(QtWidgets.QMainWindow, query10.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Query 10')
        self.setupUi(self)


def main():
    db.init()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()