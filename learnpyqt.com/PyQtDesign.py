import sys
from PyQt5.QtWidgets import QApplication, QFileDialog,QWidget
from PyQt5 import uic

def main():
    app = QApplication([])
    window = uic.loadUi('MainWindow.ui')
    window.pb_browse.clicked.connect(getfile)

    window.show()
    app.exec()

def getfile():
    file = QFileDialog.getOpenFileName('Single File', 'C:\'', "Excel(*.xlsx *.xls)")


if __name__ == '__main__':
    main()
