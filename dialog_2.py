import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QFileDialog, QWidget, QLineEdit
from BD import workBD, con


class Ui_Dialog_Edit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 518)
        self.dialog = Dialog
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 611, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 581, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 201, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 340, 201, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 340, 161, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 460, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 60, 90, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 60, 90, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 30, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(250, 60, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 120, 581, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)

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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)

        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 30, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 390, 101, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 390, 101, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(230, 390, 101, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(370, 390, 101, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(490, 460, 101, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setGeometry(QtCore.QRect(484, 390, 101, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget.addTab(self.tab_2, "")

        self.pushButton_4.clicked.connect(self.dialog.close)
        self.pushButton_12.clicked.connect(self.dialog.close)

        # Склады
        warehouses = workBD.get_warehouses_info()
        self.table_filling(warehouses, self.tableWidget)

        # Товары
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.download()

        # Кнопки обновить и загрузить
        self.pushButton_5.clicked.connect(self.download)
        self.pushButton_6.clicked.connect(self.download)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Список складов"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Адрес"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Локация"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Широта"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Долгота"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.pushButton_2.setText(_translate("Dialog", "Удалить"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_4.setText(_translate("Dialog", "Выход"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Склады"))
        self.label_2.setText(_translate("Dialog", "Список складов"))
        self.comboBox.setItemText(0, _translate("Dialog", "склады"))
        self.pushButton_5.setText(_translate("Dialog", "Загрузить"))
        self.pushButton_6.setText(_translate("Dialog", "Обновить"))
        self.label_3.setText(_translate("Dialog", "Поиск"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Критерии"))
        self.label_4.setText(_translate("Dialog", "Список товаров"))

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название товара"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Артикул"))

        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Количество"))

        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Стоимость"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Дата завоза"))

        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Срок годности"))

        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Характеристика"))

        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Изображение"))


        self.pushButton_7.setText(_translate("Dialog", "Найти"))
        self.pushButton_8.setText(_translate("Dialog", "Добавить"))
        self.pushButton_9.setText(_translate("Dialog", "Удалить"))
        self.pushButton_10.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_11.setText(_translate("Dialog", "Отменить"))
        self.pushButton_12.setText(_translate("Dialog", "Выход"))
        self.pushButton_13.setText(_translate("Dialog", "Изменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Товары"))

        # Кнопки первой таблицы
        self.pushButton_3.clicked.connect(self.save_table)
        self.pushButton.clicked.connect(lambda: self.add(self.tableWidget))
        self.pushButton_2.clicked.connect(self.delete_warehouse)

        # Кнопки второй таблицы
        # self.pushButton_13.clicked.connect(partial(self.table_dialog))
        self.pushButton_13.clicked.connect(self.table_dialog)
        self.pushButton_10.clicked.connect(self.save_table2)
        self.pushButton_8.clicked.connect(self.add_warehosue)
        self.pushButton_9.clicked.connect(lambda: self.delete(self.tableWidget_2))
        self.tableWidget_2.cellClicked.connect(self.click)
        self.pushButton_11.clicked.connect(self.cancel)
        self.pushButton_7.clicked.connect(self.search_by)

        self.comboBox_2.addItems(['Категория', 'Название', 'Артикул'])

        # Комбобоксы
        warehouses = workBD.get_table("warehouse")
        for row in warehouses:
            self.comboBox.addItem(row[1], userData=row[0])

    # Таблица 1

    def save_table(self):
        row_count = self.tableWidget.rowCount()
        column_count = self.tableWidget.columnCount()
        list_params = ['warehouse_name','address','text_location','latitude','longitude']

        for row in range(row_count):
            if self.tableWidget.verticalHeaderItem(row).text() == 'New':
                dict_for_add = {}
                for column in range(column_count):
                    item = self.tableWidget.item(row, column)
                    if item:
                        new_data = item.text()
                    else:
                        new_data = None
                    dict_for_add[list_params[column]] = new_data

                if all(list(dict_for_add.values())):
                    try:
                        workBD.add_record('warehouse',**dict_for_add)
                        warehouses = workBD.get_warehouses_info()
                        self.table_filling(warehouses, self.tableWidget)
                    except Exception as e:
                        print(e)

    def add_warehosue(self):
        if self.comboBox.currentData():
            self.add(self.tableWidget_2)

    def add(self, table_widget: QtWidgets.QTableWidget):
        rowPosition = table_widget.rowCount()
        if rowPosition:
            last_vert_header = table_widget.verticalHeaderItem(rowPosition - 1).text()
            if last_vert_header != "New":
                table_widget.insertRow(rowPosition)
        else:
            table_widget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem('New')
        table_widget.setVerticalHeaderItem(rowPosition, item)

    def delete_warehouse(self):
        current_row = self.tableWidget.currentRow()
        if current_row > -1:
            warehouse_name_item = self.tableWidget.item(current_row, 0)
            if warehouse_name_item is not None:
                id_warehouse = self.tableWidget.verticalHeaderItem(current_row).text()
                try:
                    workBD.del_record('warehouse', id=id_warehouse)
                except Exception as e:
                    print(e)
            self.tableWidget.removeRow(current_row)

    def back_warehouse(self):
        pass

    # Таблица 2
    def save_table2(self):

        row_count = self.tableWidget_2.rowCount()
        column_count = self.tableWidget_2.columnCount()
        hat = ['product_name','category','vendor_code','quantity','price','delivery_date','expiration_date', 'characteristic', 'image_path']
        if self.tableWidget_2.verticalHeaderItem(row_count - 1).text() == "New":
            row_data = {}
            for column in range(column_count):
                item = self.tableWidget_2.item(row_count - 1, column)
                if item is not None and column == 0:
                    row_data[hat[0]] = item.text()
                elif item is not None and column == 1:
                    row_data[hat[1]] = item.text()
                elif item is not None and column == 2:
                    row_data[hat[2]] = item.text()
                elif item is not None and column == 3:
                    row_data[hat[3]] = item.text()
                elif item is not None and column == 4:
                    row_data[hat[4]] = item.text()
                elif item is not None and column == 5:
                    row_data[hat[5]] = item.text()
                elif item is not None and column == 6:
                    row_data[hat[6]] = item.text()
                elif item is not None and column == 7:
                    row_data[hat[7]] = item.text()
                elif item is not None and column == 8:
                    row_data[hat[8]] = item.text()
                if len(row_data) == len(hat):
                    row_data["warehouse_id"] = int(self.comboBox.currentData())
                    workBD.add_warehouse_product(**row_data)
                    self.download()
                if workBD.queries and self.tableWidget_2.verticalHeaderItem(row_count - 1).text() != "New":
                    workBD.execute_queries()
                    self.download()

    def click(self, row, col):
        if self.tableWidget_2.verticalHeaderItem(row).text() == "New":
            if col == 8:
                options = QFileDialog.Options()
                try:
                    file_path, _ = QFileDialog.getOpenFileName(self.dialog, "Выберите изображение", "",
                                                           "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
                except Exception as e:
                    print(e)
                print(file_path)
                item = QtWidgets.QTableWidgetItem(file_path)
                self.tableWidget_2.setItem(row, col, item)

    @staticmethod
    def delete(table_widget: QtWidgets.QTableWidget):
        current_row = table_widget.currentRow()
        if current_row > -1:
            warehouse_product_id = table_widget.verticalHeaderItem(current_row).text()
            workBD.add_del_query("warehouseProduct", id=warehouse_product_id)
            table_widget.removeRow(current_row)

    def cancel(self):
        workBD.queries.clear()
        self.download()


    def search_by(self) -> None:
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
                self.table_filling(data, self.tableWidget_2)
            else:
                # удаляем содержимое ячеек
                self.tableWidget_2.clearContents()
                # удаляем строки
                while self.tableWidget_2.rowCount() > 0:
                    self.tableWidget_2.removeRow(0)

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
                table_widget.setItem(row, i - 1, item)

    def download(self) -> None:
        """
        Метод для загрузки продуктов по выбранному складу.
        :return: None
        """

        if self.comboBox.currentData() is not None:
            # получение списка с данными для заполнения таблицы
            data = workBD.get_products_from_warehouse_2(self.comboBox.currentText())
            # установка количества строк в таблице равное длине полученного списка
            self.tableWidget_2.setRowCount(len(data))

            # заполнение таблицы
            self.table_filling(data, self.tableWidget_2)

    def table_dialog(self):
        warehouse_product_id = self.tableWidget_2.verticalHeaderItem(self.tableWidget_2.currentRow())
        if warehouse_product_id:
            warehouse_product_id = warehouse_product_id.text()
            if warehouse_product_id != "New":
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog1()
                ui.warehouse_product_id = warehouse_product_id
                ui.setupUi(Dialog)
                Dialog.show()
                Dialog.exec_()
                self.download()



class Ui_Dialog1(object):
    warehouse_product_id = None
    warehouse_id = None
    product_id = None
    dialog = None
    queries = {}

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 677)
        self.dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 21))
        self.label.setObjectName("label")
        self.lineEdit = LineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 381, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = LineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 381, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 111, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = LineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 160, 381, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 111, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = LineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 220, 381, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 540, 111, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 570, 381, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 600, 381, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 630, 381, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = LineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 290, 381, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 111, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_7 = LineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 360, 381, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 330, 111, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = LineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 430, 381, 22))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 400, 111, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = LineEdit(Dialog, "lineEdit_9")
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 500, 381, 22))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 470, 111, 21))
        self.label_10.setObjectName("label_10")

        # получение данных о продукте
        try:
            with con:
                product_data = con.execute("SELECT * "
                                           "FROM products JOIN warehouseProduct ON products.id = warehouseProduct.product_id "
                                           "WHERE warehouseProduct.id = ?", (self.warehouse_product_id,)).fetchone()
                self.lineEdit.setText(product_data[1])
                self.lineEdit_2.setText(product_data[3])
                self.lineEdit_3.setText(product_data[4])
                self.lineEdit_4.setText(product_data[5])
                self.lineEdit_5.setText(product_data[-3])
                self.lineEdit_7.setText(product_data[-2])
                self.lineEdit_8.setText(product_data[-1])
                self.lineEdit_9.setText(product_data[6])
                self.comboBox.addItem(product_data[2], userData=product_data[2])

                # получение категорий товаров
                cats = workBD.get_cats()
                if cats:
                    for cat in cats:
                        if cat != product_data[2]:
                            self.comboBox.addItem(cat, userData=cat)

        except Exception as e:
            print(e)

        try:
            with con:
                data = con.execute("SELECT warehouse_id, product_id "
                                   "FROM warehouseProduct "
                                   "WHERE warehouseProduct.id = ?", (self.warehouse_product_id,)).fetchone()
                Ui_Dialog1.warehouse_id = data[0]
                Ui_Dialog1.product_id = data[1]
                Ui_Dialog1.warehouse_product_id = self.warehouse_product_id
        except Exception as e:
            print(e)

        self.comboBox.currentIndexChanged.connect(self.combo_box_change)
        self.pushButton.clicked.connect(self.save)
        self.queries.clear()
        self.pushButton_2.clicked.connect(self.dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название товара:"))
        self.label_2.setText(_translate("Dialog", "Характеристика:"))
        self.label_3.setText(_translate("Dialog", "Артикул:"))
        self.label_4.setText(_translate("Dialog", "Стоимость:"))
        self.label_5.setText(_translate("Dialog", "Категория:"))
        self.pushButton.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_2.setText(_translate("Dialog", "Выход"))
        self.label_6.setText(_translate("Dialog", "Количество:"))
        self.label_8.setText(_translate("Dialog", "Дата завоза:"))
        self.label_9.setText(_translate("Dialog", "Срок годности:"))
        self.label_10.setText(_translate("Dialog", "Изображение:"))

    def combo_box_change(self):
        self.queries["UPDATE products SET category = ? WHERE id = ?"] = (self.comboBox.currentText(), self.product_id)

    def save(self):
        try:
            with con:
                for query, params in self.queries.items():
                    con.execute(query, params)
            self.dialog.close()
        except Exception as e:
            print(e)


class LineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(LineEdit, self).__init__(args[0], **kwargs)
        self.dialog = args[0]
        self.textChanged.connect(self.onTextChanged)
        try:
            self.name = args[1]
        except Exception as e:
            self.name = None

    def mousePressEvent(self, event):
        if self.name == "lineEdit_9":
            options = QFileDialog.Options()
            try:
                file_path, _ = QFileDialog.getOpenFileName(self.dialog, "Выберите изображение", "",
                                                       "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
                self.setText(file_path)
            except Exception as e:
                super().mousePressEvent(event)
                print(e)
        else:
            super().mousePressEvent(event)

    def onTextChanged(self, text):
        update_queries = {
            "lineEdit": ("UPDATE products SET product_name = ? WHERE id = ?", Ui_Dialog1.product_id),
            "lineEdit_2": ("UPDATE products SET characteristic = ? WHERE id = ?", Ui_Dialog1.product_id),
            "lineEdit_3": ("UPDATE products SET vendor_code = ? WHERE id = ?", Ui_Dialog1.product_id),
            "lineEdit_4": ("UPDATE products SET price = ? WHERE id = ?", Ui_Dialog1.product_id),
            "lineEdit_5": ("UPDATE warehouseProduct SET quantity = ? WHERE id = ?", Ui_Dialog1.warehouse_product_id),
            "lineEdit_7": ("UPDATE warehouseProduct SET delivery_date = ? WHERE id = ?", Ui_Dialog1.warehouse_product_id),
            "lineEdit_8": ("UPDATE warehouseProduct SET expiration_date = ? WHERE id = ?", Ui_Dialog1.warehouse_product_id),
            "lineEdit_9": ("UPDATE products SET image_path = ? WHERE id = ?", Ui_Dialog1.product_id),
        }

        pair = update_queries[self.objectName()]
        print(pair)
        print(Ui_Dialog1.warehouse_product_id)
        Ui_Dialog1.queries[pair[0]] = (text, pair[1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_Edit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())