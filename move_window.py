import sqlite3 as sl

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QHeaderView, QMessageBox

from BD import workBD
from datetime import datetime, timezone

con = sl.connect('warehouseDB.db', check_same_thread=False)


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(822, 664)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 60, 191, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 30, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        warehouse_names = workBD.get_warehouse_name()

        for i in warehouse_names:
            self.comboBox_3.addItem(i,i)

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tableWidget_4 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 90, 801, 211))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(7)
        self.tableWidget_4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 340, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        for i in warehouse_names:
            self.comboBox_4.addItem(i, i)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(220, 340, 191, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(220, 320, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 310, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget_5 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 370, 801, 211))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 590, 131, 21))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 310, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 620, 801, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        warehouse_products = workBD.get_products_from_warehouse(warehouse_names[0])
        self.table_filling(warehouse_products,self.tableWidget_4,[4,5],[6,7])
        self.tableWidget_4.horizontalHeader().sectionClicked.connect(lambda: self.sort_table(self.tableWidget_4))
        self.tableWidget_4.verticalHeader().sectionClicked.connect(self.search_product)
        self.tableWidget_4.verticalHeader().sectionClicked.connect(self.set_max_count)

        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_5.horizontalHeader().sectionClicked.connect(lambda: self.sort_table_down(self.tableWidget_5))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_5.setText(_translate("Dialog", "Загрузить"))
        self.label_6.setText(_translate("Dialog", "Переместить со склада:"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Найти"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название товара"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Артикул"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Стоимость"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Дата доставки"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Срок годности"))
        self.label_8.setText(_translate("Dialog", "Переместить на склад:"))
        self.label_9.setText(_translate("Dialog", "Количество:"))
        self.pushButton.setText(_translate("Dialog", "Переместить "))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название товара"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Артикул"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Стоимость"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Дата доставки"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Срок годности"))
        self.checkBox.setText(_translate("Dialog", "Создать накладную"))
        self.pushButton_2.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))

        self.pushButton_5.clicked.connect(lambda :self.download(self.tableWidget_4,self.table_filling,workBD.get_products_from_warehouse(self.comboBox_3.currentText()),[4,5],[6,7]))
        self.pushButton.clicked.connect(self.move_down)
        self.pushButton_2.clicked.connect(self.move_cancel)
        self.pushButton_3.clicked.connect(self.move_save)



    @staticmethod
    def table_filling(data: list, table_widget: PyQt5.QtWidgets.QTableWidget, didgit_list: list,
                      date_list: list) -> None:
        """
        Метод для заполнения таблицы tableWidget.

        :param data: Список кортежей.
        :param table_widget: экземпляр класса QTableWidget.
        :return: None.
        """
        # установка количества строк в таблице равное длине полученного списка
        table_widget.setRowCount(len(data) + 1)

        for row, itm in enumerate(data):

            item = QtWidgets.QTableWidgetItem(str(itm[0]))
            table_widget.setVerticalHeaderItem(row + 1, item)

            # заполнение значениями всех столбцов
            for i in range(1, len(itm)):

                if i in didgit_list:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole, itm[i])
                    table_widget.setItem(row + 1, i - 1, item)
                elif i in date_list:

                    itm[i] = itm[i].split(".")
                    itm[i] = QDate(int(itm[i][2]), int(itm[i][0]), int(itm[i][1]))

                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.DisplayRole, itm[i])
                    table_widget.setItem(row + 1, i - 1, item)
                else:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole, str(itm[i]))
                    table_widget.setItem(row + 1, i - 1, item)

    @staticmethod
    def download(table_widget: PyQt5.QtWidgets.QTableWidget, table_filling, method, digit_list: list,
                 date_list: list) -> None:
        """
        Метод для загрузки продуктов по выбранному складу.
        :return: None
        """
        data = method
        table_widget.setRowCount(len(data) + 1)
        table_filling(data, table_widget, digit_list, date_list)

    @staticmethod
    def sort_table(table_widget: PyQt5.QtWidgets.QTableWidget):
        table_widget.setSortingEnabled(True)

        table_widget.setSortingEnabled(False)
        for i in reversed(range(1, table_widget.rowCount())):
            for j in range(table_widget.columnCount()):
                if i == 1:
                    table_widget.setItem(i, j, QtWidgets.QTableWidgetItem(table_widget.item(i - 1, j)))
                    table_widget.setItem(0, j, None)
                else:
                    table_widget.setItem(i, j, QtWidgets.QTableWidgetItem(table_widget.item(i - 1, j)))

    @staticmethod
    def sort_table_down(table_widget: PyQt5.QtWidgets.QTableWidget):
        table_widget.setSortingEnabled(True)
        table_widget.setSortingEnabled(False)

    def search_product(self, e):
        warehouses = workBD.get_warehouse_name()
        if self.tableWidget_4.verticalHeaderItem(e).text() == "Найти":
            try:
                if self.comboBox_3.currentText() in warehouses:

                    data = workBD.search_products_in_warehouse(self.comboBox_3.currentText(),
                                                               product_name=self.tableWidget_4.item(0, 0),
                                                               category=self.tableWidget_4.item(0, 1),
                                                               vendor_code=self.tableWidget_4.item(0, 2),
                                                               quantity=self.tableWidget_4.item(0, 3),
                                                               price=self.tableWidget_4.item(0, 4),
                                                               delivery_date=self.tableWidget_4.item(0, 5),
                                                               expiration_date=self.tableWidget_4.item(0, 6))

                    if data == []:
                        self.warning_message()
                    else:
                        self.table_filling(data, self.tableWidget_4, [4, 5], [6, 7])
            except:
                self.warning_message()

    def set_max_count(self,e):
        if self.tableWidget_4.verticalHeaderItem(e).text() != "Найти":
            self.spinBox.setMaximum(int(self.tableWidget_4.item(self.tableWidget_4.currentRow(),3).text()))

    def move_down(self):
        self.tableWidget_5.setRowCount(self.tableWidget_5.rowCount() + 1)
        item = QtWidgets.QTableWidgetItem(self.comboBox_3.currentText())
        self.tableWidget_5.setVerticalHeaderItem(self.tableWidget_5.rowCount() - 1, item)

        for i in range(self.tableWidget_4.columnCount()):
            if i==3:
                item_1 = QtWidgets.QTableWidgetItem()
                item_1.setData(Qt.EditRole, int(self.spinBox.text()))
                self.tableWidget_5.setItem(self.tableWidget_5.rowCount()-1, i , item_1)

            else:
                self.tableWidget_5.setItem(self.tableWidget_5.rowCount()-1, i, QtWidgets.QTableWidgetItem(self.tableWidget_4.item(self.tableWidget_4.currentRow(), i)))

    def move_save(self):
        data=[]
        for i in range(self.tableWidget_5.rowCount()):
            a=[self.tableWidget_5.verticalHeaderItem(i).text()]
            for j in range(self.tableWidget_5.columnCount()):
                a.append(self.tableWidget_5.item(i,j).text())
            data.append(a)

        for i in data:

            s = f"""
                    INSERT INTO warehouseProduct (warehouse_id,products_id, quantity,delivery_date,expiration_date)
                    SELECT (SELECT id FROM warehouse WHERE warehouse_name='{self.comboBox_4.currentText()}'),(SELECT id FROM products WHERE product_name='{i[1]}'), {i[4]},{int(datetime.strptime(i[6],"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())},{int(datetime.strptime(i[7],"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())};
                """
            for j in range(1,self.tableWidget_4.rowCount()):

                if i[3]==self.tableWidget_4.item(j,2).text() and i[6]==self.tableWidget_4.item(j,5).text():
                    if int(self.tableWidget_4.item(j,3).text()) - int(i[4])==0:
                        s1=f"""
                        DELETE FROM warehouseProduct
                        WHERE products_id=(SELECT id FROM products WHERE product_name='{i[1]}') AND delivery_date='{int(datetime.strptime(i[6],"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())}' AND expiration_date='{int(datetime.strptime(i[7],"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())}'
                        """
                    else:
                        s1=f"""
                            UPDATE warehouseProduct
                            SET quantity = "{int(self.tableWidget_4.item(j,3).text())-int(i[4])}"
                            WHERE warehouse_id=(SELECT id FROM warehouse WHERE warehouse_name='{i[0]}') AND products_id=(SELECT id FROM products WHERE product_name='{i[1]}') AND delivery_date='{int(datetime.strptime(i[6],"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())}' AND expiration_date='{int(datetime.strptime(i[7],"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())}'
                        """
            with con:
                con.execute(s)
                con.execute(s1)
        self.tableWidget_5.setRowCount(0)

    def move_cancel(self):
        self.tableWidget_5.removeRow(self.tableWidget_5.currentRow())
    def warning_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!")
        msg.setText("По заданным параметрам ничего не найдено!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
