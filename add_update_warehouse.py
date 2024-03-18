from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sl
from BD import workBD

con = sl.connect('warehouseDB.db', check_same_thread=False)
class Ui_Dialog5(object):
    this_add=False
    number=0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(271, 319)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 251, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 130, 251, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(10, 180, 251, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(10, 230, 251, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Назание склада:"))
        self.label_2.setText(_translate("Dialog", "Адрес:"))
        self.label_3.setText(_translate("Dialog", "Локация:"))
        self.label_4.setText(_translate("Dialog", "Долгота:"))
        self.label_5.setText(_translate("Dialog", "Широта:"))
        self.doubleSpinBox.setMinimum(-180.0)
        self.doubleSpinBox.setMaximum(180.0)
        self.doubleSpinBox_2.setMinimum(-90.0)
        self.doubleSpinBox_2.setMaximum(90.0)
        self.pushButton.setText(_translate("Dialog", "Сохранить"))

        self.pushButton.clicked.connect(self.save)

    def save(self):
        if self.this_add==True:

            s = f"""
                    INSERT INTO warehouse (warehouse_name,address, text_location, latitude, longitude)
                    SELECT '{self.lineEdit.text()}','{self.lineEdit_2.text()}','{self.lineEdit_3.text()}','{str(self.doubleSpinBox_2.text()).replace(",",".")}','{str(self.doubleSpinBox.text()).replace(",",".")}';
                """
        elif self.this_add==False:
            s = f"""
                    UPDATE warehouse
                    SET warehouse_name ='{self.lineEdit.text()}' ,address='{self.lineEdit_2.text()}',text_location='{self.lineEdit_3.text()}', latitude='{str(self.doubleSpinBox_2.text()).replace(",",".")}',longitude='{str(self.doubleSpinBox.text()).replace(",",".")}'
                    WHERE id='{self.number}'
                """
        with con:
            con.execute(s)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.doubleSpinBox.setValue(0)
        self.doubleSpinBox_2.setValue(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
