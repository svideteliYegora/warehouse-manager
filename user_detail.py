from PyQt5 import QtCore, QtGui, QtWidgets
from BD import workBD


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
    ui = Ui_UserDetail()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
