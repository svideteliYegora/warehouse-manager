import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QHeaderView, QMessageBox, QVBoxLayout

from BD import workBD
class Ui_Dialog(object):
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
    @staticmethod
    def table_filling(data: list, table_widget: PyQt5.QtWidgets.QTableWidget,didgit_list:list,date_list:list) -> None:
        """
        Метод для заполнения таблицы

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
                    table_widget.setItem(row + 1, i-1 , item)
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
