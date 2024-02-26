import sqlite3
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from BD import workBD
from dialog_3 import Ui_Dialog


class Ui_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(313, 249)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 130, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 202, 291, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 171, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setVisible(False)
        self.pushButton.clicked.connect(partial(self.login, Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Автоиризация"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_3.setText(_translate("Dialog", "Пароль"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:7pt; color:#ff0000;\">Неверный логин или пароль!</span></p></body></html>"))

    def login(self, Dialog) -> None:
        log = self.lineEdit.text()
        pas = self.lineEdit_2.text()
        try:
            lvl = workBD.get_access_level(log, pas)
            if lvl:
                dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.lvl = lvl
                ui.setupUi(dialog)
                Dialog.close()
                dialog.show()
            else:
                self.label_4.setVisible(True)

        except sqlite3.OperationalError as e:
            self.label_4.setVisible(True)
            self.label_4.setText("<html><head/><body><p><span style=\" font-size:7pt; color:#ff0000;\">Ошибка выполнения операции.</span></p></body></html>")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
