import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtcreator_file = 'tax_calc.ui'  # UI file name

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # super(MyWindow, self).__init__()
        # super().setWindowTitle('Sales Tax Calcuc')
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # signal and slot attached
        self.pb_calc_tax.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        # print('Clicked')
        price = float(self.LI_price_box.text())
        tax = float(self.sb_tax_rate.value())
        total_price = price + ((tax/100)*price)
        total_price_string = "The total price with tax is : {:.2f}".format(total_price)
        self.result_text.setText(total_price_string)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()