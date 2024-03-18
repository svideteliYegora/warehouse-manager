import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QHeaderView, QMessageBox

from update_delivery import Ui_Dialog7

from BD import workBD

class Ui_Dialog6(object):
    number=0
    characteristics=[]
    def setupUi(self, Dialog):
        print(self.characteristics)
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 501)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 621, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 201, 64))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        data = workBD.get_delivery_contents(self.number)
        print(self.number)
        print(data)
        self.table_filling(data,self.tableWidget,[1],[2])



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Редактировать"))
        self.label.setText(_translate("Dialog", "Содержимое поставки:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Дата пригодности"))
        self.plainTextEdit.setPlainText(_translate("Dialog", f"Поставка: {self.characteristics[0]}\n"
                                                                                f"Склад: {self.characteristics[1]}\n"
                                                                                f"Поставщик: {self.characteristics[2]}\n"
                                                                                f"Дата поставки: {self.characteristics[3]}"))


        self.pushButton.clicked.connect(self.open_update_delivery)


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
        table_widget.setRowCount(len(data))

        for i in range(len(data)):
            for j in range(table_widget.columnCount()):
                if data[i] in didgit_list:
                        item = QtWidgets.QTableWidgetItem()
                        item.setData(Qt.EditRole, data[i][j])
                        table_widget.setItem(i ,j,item)
                elif data[i] in date_list:
                        data[i][j] = data[i][j].split(".")
                        data[i][j] = QDate(int(data[i][j][2]), int(data[i][j][0]), int(data[i][j][1]))

                        item = QtWidgets.QTableWidgetItem()
                        item.setData(Qt.DisplayRole, data[i][j])
                        table_widget.setItem(i , j, item)
                else:
                        item = QtWidgets.QTableWidgetItem()
                        item.setData(Qt.EditRole, str(data[i][j]))
                        table_widget.setItem(i , j, item)

    def open_update_delivery(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog7()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
