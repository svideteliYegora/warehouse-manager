from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView, QMessageBox

from datetime import datetime, timezone

import sqlite3 as sl
from BD import workBD

con = sl.connect('warehouseDB.db', check_same_thread=False)
class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(742, 498)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 721, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.comboBox.setObjectName("comboBox")
        warehouse_names = workBD.get_warehouse_name()

        for i in warehouse_names:
            self.comboBox.addItem(i, i)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(10, 130, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 410, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 460, 721, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        products_name=workBD.get_product_names()
        self.cmb=QtWidgets.QComboBox()
        for i in products_name:
            self.cmb.addItem(i, i)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 0,self.cmb )
        time_wig = QtWidgets.QDateEdit()
        time_wig.setDate(datetime.now())
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 2, time_wig)
        item = QtWidgets.QTableWidgetItem()
        item.setData(Qt.EditRole, 1)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(item))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.dateEdit.setDate(datetime.now())
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Дата пригодности"))
        self.label_2.setText(_translate("Dialog", "Поставщик:"))
        self.label_3.setText(_translate("Dialog", "Дата поставки"))
        self.label_5.setText(_translate("Dialog", "Склад:"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.pushButton_2.setText(_translate("Dialog", "Удалить"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))

        self.pushButton.clicked.connect(self.add_product)
        self.pushButton_2.clicked.connect(self.del_product)
        self.pushButton_3.clicked.connect(self.save_delivery)

    def add_product(self):
        products_name=workBD.get_product_names()

        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        cmb_itm=QtWidgets.QComboBox()
        for i in products_name:
            cmb_itm.addItem(i, i)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,0,cmb_itm)
        time_wig=QtWidgets.QDateEdit()
        time_wig.setDate(datetime.now())
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 2, time_wig)
        item = QtWidgets.QTableWidgetItem()
        item.setData(Qt.EditRole, 1)
        self.tableWidget.setItem(self.tableWidget.rowCount()-1,1,QtWidgets.QTableWidgetItem(item))


    def del_product(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def save_delivery(self):
        s = f"""
                INSERT INTO deliveries (warehouse_id,delivery_date, provider)
                SELECT (SELECT id FROM warehouse WHERE warehouse_name='{self.comboBox.currentText()}'),{int(datetime.strptime(self.dateEdit.text(), "%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())},'{self.lineEdit.text()}'
            """
        s1="SELECT MAX(id) FROM deliveries"
        with con:
            con.execute(s)
            data=con.execute(s1).fetchall()[0][0]


        for i in range(self.tableWidget.rowCount()):
            s = f"""
                    INSERT INTO delivery_contents (deliveries_id,products_id, quantity, expiration_date)
                    SELECT {data},(SELECT id FROM products WHERE product_name='{self.tableWidget.cellWidget(i,0).currentText()}'),'{self.tableWidget.item(i,1).text()}',{int(datetime.strptime(self.tableWidget.cellWidget(i,2).text(), "%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())};
                """

            s1=f"""
                    INSERT INTO warehouseProduct (warehouse_id,products_id, quantity, delivery_date, expiration_date)
                    SELECT (SELECT id FROM warehouse WHERE warehouse_name='{self.comboBox.currentText()}'),(SELECT id FROM products WHERE product_name='{self.tableWidget.cellWidget(i,0).currentText()}'),'{self.tableWidget.item(i,1).text()}', {int(datetime.strptime(self.tableWidget.cellWidget(i,2).text(), "%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())} ,{int(datetime.strptime(self.tableWidget.cellWidget(i,2).text(), "%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())};
                """
            with con:
                con.execute(s)
                con.execute(s1)

        self.tableWidget.setRowCount(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
