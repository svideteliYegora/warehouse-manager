from BD import workBD
from PyQt5 import QtCore, QtGui, QtWidgets
from dialog_product_cart import Ui_ProductCart


class Ui_Dialog(object):
    def __init__(self):
        self.warehouses = workBD.get_warehouse_name()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 590)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 60, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 471, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 540, 121, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 120, 191, 22))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(240, 120, 191, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("введите текст")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 50, 471, 281))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(72, 30, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(172, 30, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_5.setGeometry(QtCore.QRect(272, 30, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_6.setGeometry(QtCore.QRect(372, 30, 109, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(9, 29, 65, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 340, 231, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 340, 231, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 540, 121, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_3, "")

        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.download)
        self.tableWidget.cellDoubleClicked.connect(self.double_click)
        self.pushButton_4.clicked.connect(self.search_by)
        self.pushButton_3.clicked.connect(lambda: self.dialog_close(Dialog))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Список складов"))

        for itm in self.warehouses:
            self.comboBox.addItem(itm, userData=itm)

        self.label.setText(_translate("Dialog", "Склады:"))
        self.pushButton.setText(_translate("Dialog", "Загрузить"))
        self.pushButton_2.setText(_translate("Dialog", "Обновить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название товара"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Артикул"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Стоимость"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Дата доставки"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Срок годности"))

        self.label_2.setText(_translate("Dialog", "Список товаров по заданному складу:"))
        self.pushButton_3.setText(_translate("Dialog", "Выход"))

        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, _translate("Dialog", "Категория"))
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(1, _translate("Dialog", "Название товара"))
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(2, _translate("Dialog", "Артикул"))


        self.label_3.setText(_translate("Dialog", "Поиск:"))
        self.pushButton_4.setText(_translate("Dialog", "Найти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Склад"))

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Фамилия"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Имя"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Отчество"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Адресс"))
        self.label_4.setText(_translate("Dialog", "Список покупателей"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Фамилии"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Имена"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Отчества"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "Адреса"))
        self.pushButton_5.setText(_translate("Dialog", "Найти"))
        self.pushButton_6.setText(_translate("Dialog", "Добавить клиента"))
        self.pushButton_7.setText(_translate("Dialog", "Удалить клиента"))
        self.pushButton_8.setText(_translate("Dialog", "Выход"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Клиенты"))

    def download(self) -> None:
        """
        Метод для заполнения таблицы.

        :return: None
        """
        if self.comboBox.currentData() is not None:
            # получаем список с данными для заполнения таблицы
            data = workBD.get_products_from_warehouse(self.comboBox.currentText())
            # устанавливаем количество строк в таблице равное длине полученного списка
            self.tableWidget.setRowCount(len(data))
            # заполняем таблицу
            self.table_filling(data)

    def double_click(self) -> None:
        # получаем id продукта из названия вертикального заголовка
        current_row = self.tableWidget.currentRow()
        product_id = int(self.tableWidget.verticalHeaderItem(current_row).text())

        # создаем экземпляр диалогового окна и передаем полученный product_id
        Dialog = QtWidgets.QDialog()
        ui_product_cart = Ui_ProductCart()
        ui_product_cart.product_id = product_id
        ui_product_cart.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def search_by(self) -> None:
        """
        Метод реализующий поиск в таблице.

        :return: None
        """
        if self.comboBox.currentData():
            crit_dict = {
                "Категория": "category",
                "Название товара": "product_name",
                "Артикул": "vendor_code"
            }
            # получаем нужные данные для формирования запроса на поиск
            warehouse = self.comboBox.currentText()
            crit = crit_dict[self.comboBox_2.currentText()]
            value = self.lineEdit.text()
            # выполняем запрос
            data = workBD.search_by_param(warehouse, **{crit: value})
            # полученный результат используем для заполнения таблицы
            if data:
                self.table_filling(data)
            else:
                # удаляем содержимое ячеек
                self.tableWidget.clearContents()
                # удаляем строки
                while self.tableWidget.rowCount() > 0:
                    self.tableWidget.removeRow(0)

    def show_clients(self) -> None:
        """
        Метод для заполнения таблицы данными о клиентах.

        :return: None
        """
        # получаем информацию о клиентах из БД
        data = workBD.get_all_users()


    def table_filling(self, data: list) -> None:
        """
        Метод для заполнения таблицы tableWidget.

        :param data: Список кортежей.
        :return: None.
        """
        # устанавливаем количество строк в таблице равное длине полученного списка
        self.tableWidget.setRowCount(len(data))

        for row, itm in enumerate(data):
            # устанавливаем значение вертикального заголовка как id
            item = QtWidgets.QTableWidgetItem(str(itm[0]))
            self.tableWidget.setVerticalHeaderItem(row, item)

            # заполняем значениями все столбцы
            for i in range(1, len(itm)):
                item = QtWidgets.QTableWidgetItem(itm[i])
                self.tableWidget.setItem(row, i-1, item)

    @staticmethod
    def dialog_close(Dialog) -> None:
        Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
