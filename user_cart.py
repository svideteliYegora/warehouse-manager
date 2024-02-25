from PyQt5 import QtCore, QtGui, QtWidgets
from BD import workBD
import sqlite3


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_UserCart()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
