from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from BD import workBD
from PyQt5.QtCore import Qt


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ProductDetail()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
