import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QHeaderView, QMessageBox, QVBoxLayout

import sqlite3
from BD import workBD

from window1 import Ui_Dialog

class Ui_Dialogg(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(823, 557)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        layout=QVBoxLayout()
        self.sklad = QtWidgets.QTabWidget(Dialog)
        self.sklad.setGeometry(QtCore.QRect(0, 0, 851, 601))
        self.sklad.setObjectName("sklad")
        self.Sklad = QtWidgets.QWidget()
        self.Sklad.setObjectName("Sklad")
        self.comboBox = QtWidgets.QComboBox(self.Sklad)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItem("Все склады", "Все склады")
        warehouse_names = workBD.get_warehouse_name()
        for i in warehouse_names:
            self.comboBox.addItem(i, i)

        self.tableWidget = QtWidgets.QTableWidget(self.Sklad)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 801, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        self.label = QtWidgets.QLabel(self.Sklad)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Sklad)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.Sklad)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 191, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.Sklad)
        self.pushButton.setGeometry(QtCore.QRect(620, 10, 191, 21))
        self.pushButton.setObjectName("pushButton")
        self.sklad.addTab(self.Sklad, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 30, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_2.addItem("Все склады", "Все склады")
        for i in warehouse_names:
            self.comboBox_2.addItem(i, i)

        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 110, 801, 411))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.sklad.addTab(self.tab, "")
        self.Clients = QtWidgets.QWidget()
        self.Clients.setObjectName("Clients")
        self.label_2 = QtWidgets.QLabel(self.Clients)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Clients)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 30, 801, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.pushButton_13 = QtWidgets.QPushButton(self.Clients)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 500, 201, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_15 = QtWidgets.QPushButton(self.Clients)
        self.pushButton_15.setGeometry(QtCore.QRect(620, 500, 191, 28))
        self.pushButton_15.setObjectName("pushButton_15")
        self.sklad.addTab(self.Clients, "")
        self.Tab3 = QtWidgets.QWidget()
        self.Tab3.setObjectName("Tab3")
        self.label_10 = QtWidgets.QLabel(self.Tab3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 123, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_10 = QtWidgets.QPushButton(self.Tab3)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 500, 191, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.Tab3)
        self.tableWidget_7.setGeometry(QtCore.QRect(10, 30, 801, 461))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(6)
        self.tableWidget_7.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        self.pushButton_11 = QtWidgets.QPushButton(self.Tab3)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 500, 201, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.Tab3)
        self.pushButton_12.setGeometry(QtCore.QRect(220, 500, 201, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.sklad.addTab(self.Tab3, "")

        #Добавляю новую кнопку (Сохранить)
        self.pushButton_14 = QtWidgets.QPushButton(self.Tab3)
        self.pushButton_14.setGeometry(QtCore.QRect(425, 500, 191, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setText("Сохранить")

        self.retranslateUi(Dialog)
        self.sklad.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        layout.addWidget(self.tableWidget)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        warehouse_products = workBD.get_products_from_all_warehouse()
        self.table_filling(warehouse_products, self.tableWidget, [4, 5], [6, 7])
        self.tableWidget.horizontalHeader().sectionClicked.connect(lambda: self.sort_table(self.tableWidget))
        self.tableWidget.verticalHeader().sectionClicked.connect(self.search_product)

        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        deliveryes = workBD.get_info_deliveryes_all_warehouse()
        self.table_filling(deliveryes, self.tableWidget_3, [], [3])
        self.tableWidget_3.horizontalHeader().sectionClicked.connect(lambda: self.sort_table(self.tableWidget_3))
        self.tableWidget_3.verticalHeader().sectionClicked.connect(self.search_deliveryes)

        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.setSpan(0,0,1,3)
        users=workBD.get_all_users()
        self.table_filling(users,self.tableWidget_2,[],[4])
        self.tableWidget_2.horizontalHeader().sectionClicked.connect(lambda: self.sort_table(self.tableWidget_2))
        self.tableWidget_2.verticalHeader().sectionClicked.connect(self.search_user)

        self.tableWidget_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_7.setSpan(0, 0, 1, 3)
        staff=workBD.get_staff()
        self.table_filling(staff,self.tableWidget_7,[],[])
        self.tableWidget_7.horizontalHeader().sectionClicked.connect(lambda: self.sort_table(self.tableWidget_7))
        self.tableWidget_7.verticalHeader().sectionClicked.connect(self.search_staf)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Найти"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Склад"))
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
        self.label.setText(_translate("Dialog", "Склады:"))
        self.label_3.setText(_translate("Dialog", "Список товаров на складе:"))
        self.pushButton_3.setText(_translate("Dialog", "Загрузить"))
        self.pushButton.setText(_translate("Dialog", "Настройки"))
        self.sklad.setTabText(self.sklad.indexOf(self.Sklad), _translate("Dialog", "Товар"))
        self.label_4.setText(_translate("Dialog", "Склады:"))
        self.pushButton_4.setText(_translate("Dialog", "Загрузить"))
        self.label_5.setText(_translate("Dialog", "Список поставок на склад:"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Найти"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Склад"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Поставщик"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Дата поставкки"))
        self.sklad.setTabText(self.sklad.indexOf(self.tab), _translate("Dialog", "Поставки"))
        self.label_2.setText(_translate("Dialog", "Список Клиентов:"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Найти"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Фамилия"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Имя"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Отчество"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Дата рождения"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Адрес"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Почта"))
        self.pushButton_13.setText(_translate("Dialog", "Добавить клиента"))
        self.pushButton_15.setText(_translate("Dialog", "Обновить таблицу"))
        self.sklad.setTabText(self.sklad.indexOf(self.Clients), _translate("Dialog", "Клиенты"))
        self.label_10.setText(_translate("Dialog", "Список сотрудников:"))
        self.pushButton_10.setText(_translate("Dialog", "Обновить таблицу"))
        item = self.tableWidget_7.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Найти"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Фамилия"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Имя"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Отчество"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Логин"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Пароль"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Уровень доступа"))
        self.pushButton_11.setText(_translate("Dialog", "Добавить сотрудника"))
        self.pushButton_12.setText(_translate("Dialog", "Удалить сотрудника"))
        self.sklad.setTabText(self.sklad.indexOf(self.Tab3), _translate("Dialog", "Персонал"))

        self.pushButton_3.clicked.connect(lambda : self.download_products_or_deliverys(self.tableWidget, self.comboBox, self.table_filling,
                                                                                       workBD.get_products_from_warehouse(
                                                                     self.comboBox.currentText()),
                                                                                       workBD.get_products_from_all_warehouse(), [4,5], [6,7]))

        self.pushButton_4.clicked.connect(lambda :self.download_products_or_deliverys(self.tableWidget_3, self.comboBox_2, self.table_filling,
                                                                                      workBD.get_info_deliveryes_on_warehoouse(
                                                                    self.comboBox_2.currentText()),
                                                                                      workBD.get_info_deliveryes_all_warehouse(), [], [3]))
        self.pushButton_15.clicked.connect(
            lambda :self.download(self.tableWidget_2,self.table_filling, workBD.get_all_users(),[], [4]))

        self.pushButton_10.clicked.connect(
            lambda: self.download(self.tableWidget_7, self.table_filling, workBD.get_staff(), [], []))

        self.pushButton_13.clicked.connect(self.add_clients)

        # Двойной клик
        self.tableWidget_2.cellDoubleClicked.connect(lambda: self.get_detail(self.tableWidget_2, flag=True))

        # Кнопки добавления и удаления персонала
        self.pushButton_11.clicked.connect(lambda: self.add_staff(self.tableWidget_7))
        self.pushButton_12.clicked.connect(self.del_staff)

        # Добавляю новую кнопку сохранить
        self.pushButton_14.clicked.connect(self.save_staff)

        self.pushButton.clicked.connect(self.open_win1)

    def open_win1(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    @staticmethod
    def table_filling(data: list, table_widget: PyQt5.QtWidgets.QTableWidget,didgit_list:list,date_list:list) -> None:
        """
        Метод для заполнения таблицы

        :rtype: object
        :param data: список списков/кортежей с данными для заполнения таблицы
        :param table_widget: имя таблицы
        :param didgit_list: список номеров колонок (№_+1) с числовым типом
        :param date_list: список номеров колонок (№_+1) с типом данных дата
        :return: -
        """
        # установка количества строк в таблице равное длине полученного списка
        table_widget.setRowCount(len(data)+1)

        for row, itm in enumerate(data):
            # устанавливаем значение вертикального заголовка как id
            item = QtWidgets.QTableWidgetItem(str(itm[0]))
            table_widget.setVerticalHeaderItem(row+1, item)

            # заполнение значениями всех столбцов
            for i in range(1, len(itm)):

                if i in didgit_list:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole,itm[i])
                    table_widget.setItem(row + 1, i-1, item)
                elif i in date_list:

                    itm[i]=itm[i].split(".")
                    itm[i]=QDate(int(itm[i][2]),int(itm[i][0]),int(itm[i][1]))

                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.DisplayRole,itm[i])
                    table_widget.setItem(row + 1, i-1, item)
                else:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole,str(itm[i]))
                    table_widget.setItem(row+1, i-1, item)

    @staticmethod
    def download_products_or_deliverys(table_widget:PyQt5.QtWidgets.QTableWidget, combobox:PyQt5.QtWidgets.QComboBox, table_filling, method_1, method_2, digit_list:list, date_list:list) -> None:
        """
        Метод для заполнеия таблицы по указанному складу или обновления таблицы по указанному складу
        :param table_widget: имя таблицы продуктов или поставок
        :param combobox: имя выпадающего списка
        :param table_filling: метод для заполения таблицы
        :param method_1: метод получения данных о товарах/поставках по одному складу
        :param method_2: метод получения данных о товарах/поставках по всем складам
        :param digit_list: список номеров колонок (№_+1) с числовым типом данных
        :param date_list: список номеров колонок (№_+1) с типом данных дата
        :return: -
        """
        if combobox.currentData() is not None:

            # получение списка с данными для заполнения таблицы
            if combobox.currentText()=="Все склады":
                data=method_2
            else:
                data = method_1
            # установка количества строк в таблице равное длине полученного списка
            table_widget.setRowCount(len(data)+1)

            # заполнение таблицы
            table_filling(data, table_widget,digit_list,date_list)

    @staticmethod
    def download(table_widget:PyQt5.QtWidgets.QTableWidget, table_filling, method,digit_list:list, date_list:list) -> None:
        """
        Такой же метод как и выше только для всех остальных таблиц(клиенты и персонал
        :param table_widget: имя таблицы
        :param table_filling: метод заполнения таблицы
        :param method: метод получения данных для заполнения таблицы из файла BD
        :param digit_list: список номеров колонок (№_+1) с числовым типом данных
        :param date_list: список номеров колонок (№_+1) с типом данных дата
        :return: -
        """

        data=method

        table_widget.setRowCount(len(data)+1)
        table_filling(data, table_widget,digit_list,date_list)

    @staticmethod
    def sort_table(table_widget:PyQt5.QtWidgets.QTableWidget):
        """
        Метод для сортировки таблицы
        :param table_widget: имя таблицы
        :return: -
        """
        table_widget.setSortingEnabled(True)

        table_widget.setSortingEnabled(False)
        for i in reversed(range(1,table_widget.rowCount())):
            for j in range(table_widget.columnCount()):
                if i==1:
                    table_widget.setItem(i, j, QtWidgets.QTableWidgetItem(table_widget.item(i - 1, j)))
                    table_widget.setItem(0, j, None)
                else:
                    table_widget.setItem(i,j,QtWidgets.QTableWidgetItem(table_widget.item(i-1,j)))
    def search_product(self,e):
        """
        Поиск таблицы товаров
        :param e: вспомогательная, забей. кода вызываешь метод, ее в методпередавать не надо
        :return: -
        """
        warehouses=workBD.get_warehouse_name()
        if self.tableWidget.verticalHeaderItem(e).text()=="Найти":
            try:
                if self.comboBox.currentText()=="Все склады":
                    data = workBD.search_products_in_all_warehouse(product_name=self.tableWidget.item(0, 0),
                                           category=self.tableWidget.item(0, 1),
                                           vendor_code=self.tableWidget.item(0, 2),
                                           quantity=self.tableWidget.item(0, 3),
                                           price=self.tableWidget.item(0, 4),
                                           delivery_date=self.tableWidget.item(0, 5),
                                           expiration_date=self.tableWidget.item(0, 6))

                    if data==[]:
                        self.warning_message()
                    else:
                        self.table_filling(data, self.tableWidget, [4, 5], [6, 7])

                elif self.comboBox.currentText() in warehouses:

                    data=workBD.search_products_in_warehouse(self.comboBox.currentText(),
                                         product_name=self.tableWidget.item(0,0),
                                         category=self.tableWidget.item(0,1),
                                         vendor_code=self.tableWidget.item(0,2),
                                         quantity=self.tableWidget.item(0,3),
                                         price=self.tableWidget.item(0,4),
                                         delivery_date=self.tableWidget.item(0,5),
                                         expiration_date=self.tableWidget.item(0,6))

                    if data == []:
                        self.warning_message()
                    else:
                        self.table_filling(data,self.tableWidget,[4,5],[6,7])
            except:
                self.warning_message()
    def search_deliveryes(self,e):
        """
        Поиск в таблиц поставок
        :param e: забей
        :return: -
        """
        warehouses = workBD.get_warehouse_name()
        if self.tableWidget_3.verticalHeaderItem(e).text() == "Найти":
            try:
                if self.comboBox_2.currentText() == "Все склады":

                    data = workBD.search_deliveryes_all_warehouse(warehouse_name=self.tableWidget_3.item(0,0),
                                                                  provider=self.tableWidget_3.item(0,1),
                                                                  delivery_date=self.tableWidget_3.item(0,2))

                    if data == []:
                        self.warning_message()
                    else:
                        self.table_filling(data, self.tableWidget_3, [], [3])

                elif self.comboBox_2.currentText() in warehouses:

                    data = workBD.search_deliveryes_on_warehouse(self.comboBox_2.currentText(),
                                                                 warehouse_name=self.tableWidget_3.item(0,0),
                                                                  provider=self.tableWidget_3.item(0,1),
                                                                  delivery_date=self.tableWidget_3.item(0,2))
                    if data == []:
                        self.warning_message()
                    else:
                        self.table_filling(data, self.tableWidget_3, [], [3])
            except:
                self.warning_message()

    def search_user(self,e):
        """
        поиск в табице клиентов
        :param e: забей
        :return: -
        """
        if self.tableWidget_2.verticalHeaderItem(e).text() == "Найти":
            try:
                data=workBD.search_users(full_name=self.tableWidget_2.item(0,0),
                                       birthday=self.tableWidget_2.item(0,3),
                                       address=self.tableWidget_2.item(0,4),
                                       email=self.tableWidget_2.item(0,5))

                if data == []:
                    self.warning_message()
                else:
                    self.table_filling(data, self.tableWidget_2, [], [4])
            except:
                self.warning_message()

    def search_staf(self,e):
        """
        Поиск в таблице сотрудников
        :param e: забей
        :return: -
        """
        if self.tableWidget_7.verticalHeaderItem(e).text() == "Найти":
            try:
                data=workBD.search_staff(full_name=self.tableWidget_7.item(0,0),
                                       login=self.tableWidget_7.item(0,3),
                                       password=self.tableWidget_7.item(0,4),
                                       access_level=self.tableWidget_7.item(0,5))

                if data == []:
                    self.warning_message()
                else:
                    self.table_filling(data, self.tableWidget_7, [], [])
            except:
                self.warning_message()
    def warning_message(self):
        """
        Метод для окошка ошибки
        :return: -
        """
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!")
        msg.setText("По заданным параметрам ничего не найдено!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def del_staff(self) -> None:
        """
        Удаление выделенной записи из БД и из экземпляра QTableWidget.

        :return: None.
        """
        # проверка на наличие выделенной строки
        row_index = self.tableWidget_7.currentRow()
        if row_index:
            # получение данных из вертикального заголовка выделенной записи
            user_id = self.tableWidget_7.verticalHeaderItem(row_index).text()
            try:
                # удаление записи из бд
                workBD.del_record("staff", id=user_id)
                # удаление записи из таблицы QTableWidget
                self.tableWidget_7.removeRow(row_index)
            except Exception as e:
                print(e)

    def add_staff(self, table_widget: QtWidgets.QTableWidget):
        rowPosition = table_widget.rowCount()

        if rowPosition:
            last_vert_header = table_widget.verticalHeaderItem(rowPosition - 1).text()
            if last_vert_header != "New":
                table_widget.insertRow(rowPosition)
        else:
            table_widget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem('New')
        table_widget.setVerticalHeaderItem(rowPosition, item)

    def save_staff(self):
        row_count = self.tableWidget_7.rowCount()
        column_count = self.tableWidget_7.columnCount()
        list_params = ['first_name', 'last_name', 'surname', 'login', 'password', "access_level"]

        for row in range(row_count):
            if self.tableWidget_7.verticalHeaderItem(row).text() == 'New':
                dict_for_add = {}
                for column in range(column_count):
                    item = self.tableWidget_7.item(row, column)
                    if item:
                        new_data = item.text()
                    else:
                        new_data = None
                    dict_for_add[list_params[column]] = new_data
                print(dict_for_add)

                if all(list(dict_for_add.values())):
                    try:
                        workBD.add_record('staff', **dict_for_add)
                        data = workBD.get_staff()
                        self.table_filling(data, self.tableWidget_7,[],[])
                    except Exception as e:
                        print(e)

    def add_clients(self) -> None:
        """
        Вызов окна для добавления нового клиента.
        :return: None.
        """
        Dialog1 = QtWidgets.QDialog()
        ui = Ui_UserCart()
        ui.setupUi(Dialog1)
        Dialog1.show()
        Dialog1.exec_()
        data = workBD.get_all_users()
        self.table_filling(data, self.tableWidget_2,[],[])

    @staticmethod
    def get_detail(table_widget: PyQt5.QtWidgets.QTableWidget, flag=False) -> None:
        """
        Получение карты товара или клиента, в зависимости от указанного параметра.

        :param flag: Булево значение, default=False - создание карточки товара, True - создание карточки пользователя.
        :param table_widget: Экземпляр класса QTableWidget.
        :return: None
        """
        # получение id из названия вертикального заголовка

        current_row = table_widget.currentRow()
        if current_row != 0:
            id_ = int(table_widget.verticalHeaderItem(current_row).text())

            # создание экземпляра диалогового окна и передача полученного id
            Dialog1 = QtWidgets.QDialog()
            ui_cart = Ui_UserDetail()
            setattr(ui_cart, "user_id", id_)
            ui_cart.setupUi(Dialog1)
            Dialog1.show()
            Dialog1.exec_()

class Ui_UserCart(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog")
        Dialog1.resize(410, 531)
        self.dialog = Dialog1
        self.lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 371, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 110, 371, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 180, 371, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 250, 371, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 320, 371, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 390, 371, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog1)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog1)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog1)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 71, 31))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 470, 371, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_7 = QtWidgets.QLabel(Dialog1)
        self.label_7.setGeometry(QtCore.QRect(20, 430, 401, 20))
        self.label_7.setObjectName("label_7")
        self.label_7.setVisible(False)

        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(lambda: self.dialog.close())

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Имя*</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Фамилия*</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Отчество*</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Возраст*</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Адрес*</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Email*</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Cоздать"))
        self.pushButton_2.setText(_translate("Dialog", "Отменить"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:7pt; color:#ff0000;\">Для добавления новой записи необходимо заполнить все поля!</span></p></body></html>"))

    def create(self) -> None:
        """
        Создание записи нового пользователя.

        :return: None.
        """
        check_data = {}
        if self.checker_fields():
            try:
                # Attempt to retrieve user input
                check_data['first_name'] = self.lineEdit.text()
                check_data['last_name'] = self.lineEdit_2.text()
                check_data['surname'] = self.lineEdit_3.text()
                check_data['birthday'] = int(self.lineEdit_4.text())
                check_data['address'] = self.lineEdit_5.text()
                check_data['email'] = self.lineEdit_6.text()

                if not isinstance(check_data['birthday'], int):
                    raise ValueError("День рождения должен быть целым числом.")

                elif isinstance(check_data['birthday'], int):
                    workBD.add_record('users', **check_data)
                    self.dialog.close()

            except ValueError as e:
                error_message = str(e)
                self.lineEdit_4.setStyleSheet("color: red;")

            except Exception as e:
                error_message = str(e)

    def checker_fields(self) -> bool:
        """
        Метод проверяет корректность заполненных полей, возвращает True, если да и False, в противном случае.
        :return: None.
        """
        if all(
            [
                self.lineEdit.text(), self.lineEdit_2.text(),
                self.lineEdit_3.text(), self.lineEdit_4.text(),
                self.lineEdit_5.text(), self.lineEdit_6.text()
            ]
        ):
            return True
        else:
            return False

class Ui_UserDetail(object):
    user_id = None
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog")
        Dialog1.resize(614, 433)
        self.groupBox = QtWidgets.QGroupBox(Dialog1)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 571, 231))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_8.setGeometry(QtCore.QRect(10, 20, 551, 192))
        self.tableWidget_8.setObjectName("tableWidget")
        self.tableWidget_8.setColumnCount(3)
        self.tableWidget_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)

        self.groupBox_2 = QtWidgets.QGroupBox(Dialog1)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 301, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 281, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(470, 390, 121, 23))
        self.pushButton.setObjectName("pushButton")

        # #Кнопка обновить
        self.pushButton_1 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_1.setGeometry(QtCore.QRect(350, 110, 150, 23))
        self.pushButton_1.setObjectName("pushButton1")

        #Двойной клик
        # self.tableWidget.cellDoubleClicked.connect(lambda: self.get_content(self.tableWidget))

        self.tableWidget_8.cellDoubleClicked.connect(lambda: self.get_content(self.tableWidget_8))

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)
        self.pushButton.clicked.connect(lambda: Dialog1.close())


    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Список заказов:"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Номер заказа"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Стоимость заказа"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Дата заказа"))

        self.groupBox_2.setTitle(_translate("Dialog", "Данные пользователя:"))
        self.pushButton.setText(_translate("Dialog", "Выход"))
        self.pushButton_1.setText(_translate("Dialog", "Обновить"))


        # получение данных пользователя
        user = workBD.get_user_cart(self.user_id)
        id_, name, lastname, surname, full_name, birthday, address, email = user

        # формирование и вставка текста
        text = "<b>Фамилия</b>: {}<br>" \
               "<b>Имя</b>: {}<br>" \
               "<b>Отчество</b>: {}<br>" \
               "<b>Возраст</b>: {} лет<br>" \
               "<b>Адрес</b>: {}<br>" \
               "<b>Email</b>: {}". \
            format(lastname, name, surname, birthday, address, email)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(text)

        # получение информации о заказах пользователя
        orders = workBD.get_user_orders(self.user_id)

        # заполнение таблицы
        self.tableWidget_8.setRowCount(len(orders))
        for row, order in enumerate(orders):
            for i in range(len(order)):
                item = QtWidgets.QTableWidgetItem(str(order[i]))
                self.tableWidget_8.setItem(row, i, item)
        # установка запрета на редактирование на изменение таблицы
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def get_content(self, table_widget: PyQt5.QtWidgets.QTableWidget) -> None:
        # получение id из названия вертикального заголовка
        current_row = table_widget.currentRow()
        item = table_widget.item(current_row, 0)
        if item is not None:
            order_number = item.text()

        Dialog2 = QtWidgets.QDialog()
        ui_cart = Ui_Dialog_Content()
        # Передача номера заказа в следующее окно

        ui_cart.setupUi(Dialog2)
        ui_cart.set_order_number(order_number)
        Dialog2.show()
        Dialog2.exec_()

class Ui_Dialog_Content(object):
    order_number = None
    def setupUi(self, Content):
        Content.setObjectName("Dialog")
        Content.resize(530, 492)
        self.groupBox = QtWidgets.QGroupBox(Content)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 421, 371))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 381, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(Content)
        self.pushButton.setGeometry(QtCore.QRect(30, 400, 401, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Content)
        QtCore.QMetaObject.connectSlotsByName(Content)

    def retranslateUi(self, Content):
        _translate = QtCore.QCoreApplication.translate
        Content.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Содержание"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Стоимость"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))

        orders = workBD.get_user_orders(self.order_number)

    def set_order_number(self, order_number):
        self.order_number = order_number
        order_content = workBD.get_orders_content(order_number)
        print(order_content)

        if order_content:
            try:
                self.tableWidget.setRowCount(len(order_content))

                for row, data in enumerate(order_content):
                    item1 = QtWidgets.QTableWidgetItem(str(data[1]))
                    item2 = QtWidgets.QTableWidgetItem(str(data[0]))
                    item3 = QtWidgets.QTableWidgetItem(str(data[2]))

                    self.tableWidget.setItem(row,0,item1)
                    self.tableWidget.setItem(row, 1, item2)
                    self.tableWidget.setItem(row, 2, item3)
            except Exception as e:
                print(e)









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialogg()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())