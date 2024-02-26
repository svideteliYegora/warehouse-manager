import PyQt5
from BD import workBD, con
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sqlite3
from Dialog_2 import Ui_Dialog_Edit


class Ui_Dialog(object):
    lvl = 3

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
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 60, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setText("Редактировать")
        if self.lvl not in (1, 2):
            self.pushButton_9.setVisible(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 50, 471, 281))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        # заполняем таблицу данными о клиентах
        data = workBD.get_all_users()
        self.table_filling(data, self.tableWidget_2)
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
        self.filling_combo_boxes()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.download)
        self.tableWidget.cellDoubleClicked.connect(lambda: self.get_detail(self.tableWidget))
        self.tableWidget_2.cellDoubleClicked.connect(lambda: self.get_detail(self.tableWidget_2, flag=True))
        self.pushButton_4.clicked.connect(self.search_by)
        self.pushButton_3.clicked.connect(lambda: Dialog.close())
        self.pushButton_8.clicked.connect(lambda: Dialog.close())
        self.pushButton_6.clicked.connect(self.add_client)
        self.pushButton_7.clicked.connect(self.del_client)
        self.pushButton_5.clicked.connect(self.search_client)
        self.pushButton_9.clicked.connect(self.edit)


        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Список складов"))

        warehouses = workBD.get_warehouse_name()
        for itm in warehouses:
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
        self.comboBox_2.addItem("", userData="category")
        self.comboBox_2.setItemText(0, _translate("Dialog", "Категория"))
        self.comboBox_2.addItem("", userData="product_name")
        self.comboBox_2.setItemText(1, _translate("Dialog", "Название товара"))
        self.comboBox_2.addItem("", userData="vendor_code")
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

    def edit(self) -> None:
        """
        Метод вызывающий окно для редактирования таблиц: 'Склады', 'Товары', доступен для пользователей 1 и 2 уровня.

        :return: None.
        """
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_Edit()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def download(self) -> None:
        """
        Метод для загрузки продуктов по выбранному складу.

        :return: None
        """
        if self.comboBox.currentData() is not None:
            # получение списка с данными для заполнения таблицы
            data = workBD.get_products_from_warehouse(self.comboBox.currentText())
            # установка количества строк в таблице равное длине полученного списка
            self.tableWidget.setRowCount(len(data))
            # заполнение таблицы
            self.table_filling(data, self.tableWidget)

    def add_client(self) -> None:
        """
        Вызов окна для добавления нового клиента.

        :return: None.
        """
        Dialog = QtWidgets.QDialog()
        ui = Ui_UserCart()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        data = workBD.get_all_users()
        self.table_filling(data, self.tableWidget_2)

    def del_client(self) -> None:
        """
        Удаление выделенной записи из БД и из экземпляра QTableWidget.

        :return: None.
        """

        # проверка на наличие выделенной строки
        row_index = self.tableWidget_2.currentRow()
        if row_index:
            # получение данных из вертикального заголовка выделенной записи
            user_id = self.tableWidget_2.verticalHeaderItem(row_index).text()
            try:
                # удаление записи из бд
                workBD.del_record("users", id=user_id)
                # удаление записи из таблицы QTableWidget
                self.tableWidget_2.removeRow(row_index)
            except Exception as e:
                print(e)

    def search_by(self) -> None:
        """
        Метод реализующий поиск в таблице tableWidget.

        :return: None
        """
        if self.comboBox.currentData():
            # получение данных для формирования запроса на поиск
            warehouse = self.comboBox.currentText()
            param = self.comboBox_2.currentData()
            value = self.lineEdit.text()
            # выполнение запроса
            data = workBD.search_by_param(warehouse, **{param: value})
            # полученный результат используется для заполнения таблицы
            if data:
                self.table_filling(data, self.tableWidget)
            else:
                # удаление содержимого ячеек
                self.tableWidget.clearContents()
                # удаление строки
                while self.tableWidget.rowCount() > 0:
                    self.tableWidget.removeRow(0)

    def search_client(self) -> None:
        """
        Метод для получения выборки записей о клиентах, по заданным в комбо боксах критериях.

        :return: None.
        """
        query = "SELECT id, first_name, last_name, surname, address FROM users"
        params = []
        if any(
                [
                    self.comboBox_3.currentData(),
                    self.comboBox_4.currentData(),
                    self.comboBox_5.currentData(),
                    self.comboBox_6.currentData()
                ]
        ):
            # формирование запроса на основе данных полученных из комбо боксов
            query += " WHERE "
            conditions = []
            for combo_box in (self.comboBox_3, self.comboBox_4, self.comboBox_5, self.comboBox_6):
                if combo_box.currentData():
                    conditions.append(f"{combo_box.currentData()} = ?")
                    params.append(combo_box.currentText())
            query += " AND ".join(conditions)
        # выполнение запроса
        try:
            with con:
                if params:
                    data = con.execute(query, params).fetchall()
                else:
                    data = con.execute(query).fetchall()
        except Exception as e:
            print(e)
        # заполнение таблицы tableWidget_2
        self.table_filling(data, self.tableWidget_2)

    def filling_combo_boxes(self) -> None:
        """
        Метод для заполнения комбо боксов

        :return: None.
        """
        try:
            with con:
                # получение уникальных значений столбцов из БД и заполнение комбо боксов
                query = "SELECT DISTINCT {} FROM users"
                combo_boxes = (self.comboBox_3, self.comboBox_4, self.comboBox_5, self.comboBox_6)
                columns = ("last_name", "first_name", "surname", "address")
                for i in range(len(combo_boxes)):
                    data = con.execute(query.format(columns[i])).fetchall()
                    for itm in data:
                        combo_boxes[i].addItem(itm[0], userData=columns[i])
        except Exception as e:
            print(e)

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
        id_ = int(table_widget.verticalHeaderItem(current_row).text())

        # создание экземпляра диалогового окна и передача полученного id
        Dialog = QtWidgets.QDialog()
        ui_cart = Ui_UserDetail() if flag else Ui_ProductDetail()
        setattr(ui_cart, "user_id", id_) if flag else setattr(ui_cart, "product_id", id_)
        ui_cart.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    @staticmethod
    def table_filling(data: list, table_widget: PyQt5.QtWidgets.QTableWidget) -> None:
        """
        Метод для заполнения таблицы tableWidget.

        :param data: Список кортежей.
        :param table_widget: экземпляр класса QTableWidget.
        :return: None.
        """
        # установка количества строк в таблице равное длине полученного списка
        table_widget.setRowCount(len(data))

        for row, itm in enumerate(data):
            # устанавливаем значение вертикального заголовка как id
            item = QtWidgets.QTableWidgetItem(str(itm[0]))
            table_widget.setVerticalHeaderItem(row, item)

            # заполнение значениями всех столбцов
            for i in range(1, len(itm)):
                item = QtWidgets.QTableWidgetItem(str(itm[i]))
                table_widget.setItem(row, i-1, item)


class Ui_ProductDetail(object):
    product_id = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 433)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 120, 230, 230))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 380, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 250, 250))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(330, 70, 250, 250))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(lambda: Dialog.close())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        # получение информацию о товаре
        product: tuple = workBD.get_product_cart(self.product_id)
        id_, name, category, characteristic, vendor_code, price, img_path = product
        pixmap = QPixmap(img_path)
        self.label_2.setPixmap(pixmap)

        # масштабирование изображения
        self.label_2.setScaledContents(True)

        # формирование и вставка текста
        text = "<b>Название</b>: {}<br><br>" \
               "<b>Категория</b>: {}<br><br>" \
               "<b>Артикул</b>: {}<br><br>" \
               "<b>Стоимость</b>: {}<br><br>" \
               "<b>Характеристика</b>:<br> {}". \
            format(name, category, vendor_code, price, characteristic)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(text)
        self.pushButton.setText(_translate("Dialog", "Выход"))


class Ui_UserCart(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 531)
        self.dialog = Dialog
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 371, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 110, 371, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 180, 371, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 250, 371, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 320, 371, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 390, 371, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 71, 31))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
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
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 430, 401, 20))
        self.label_7.setObjectName("label_7")
        self.label_7.setVisible(False)

        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(lambda: self.dialog.close())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
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
        if self.checker_fields():
            try:
                workBD.add_record(
                    "users",
                    first_name=self.lineEdit.text(),
                    last_name=self.lineEdit_2.text(),
                    surname=self.lineEdit_3.text(),
                    age=self.lineEdit_4.text(),
                    address=self.lineEdit_5.text(),
                    email=self.lineEdit_6.text()
                )
                self.dialog.close()
            except sqlite3.OperationalError as e:
                print(e)
                self.label_7.setVisible(True)
                self.label_7.setText(
                    "<html><head/><body><p><span style=\" font-size:7pt; color:#ff0000;\">Ошибка: Запись не была добавлена. Повторите попытку позже.</span></p></body></html>")
            except Exception as e:
                print(e)
        else:
            self.label_7.setVisible(True)

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

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 433)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 571, 231))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 551, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 301, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 281, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 390, 121, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(lambda: Dialog.close())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Список заказов:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Номер заказа"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Стоимость заказа"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Дата заказа"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Содержимое"))
        self.groupBox_2.setTitle(_translate("Dialog", "Данные пользователя:"))
        self.pushButton.setText(_translate("Dialog", "Выход"))

        # получение данных пользователя
        user = workBD.get_user_cart(self.user_id)
        id_, name, lastname, surname, age, address, email = user

        # формирование и вставка текста
        text = "<b>Фамилия</b>: {}<br>" \
               "<b>Имя</b>: {}<br>" \
               "<b>Отчество</b>: {}<br>" \
               "<b>Возраст</b>: {} лет<br>" \
               "<b>Адрес</b>: {}<br>" \
               "<b>Email</b>: {}".\
            format(lastname, name, surname, age, address, email)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(text)

        # получение информации о заказах пользователя
        orders = workBD.get_user_orders(self.user_id)
        # заполнение таблицы
        self.tableWidget.setRowCount(len(orders))
        for row, order in enumerate(orders):

            for i in range(len(order)):
                item = QtWidgets.QTableWidgetItem(str(order[i]))
                self.tableWidget.setItem(row, i, item)
        # установка запрета на редактирование на изменение таблицы
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
