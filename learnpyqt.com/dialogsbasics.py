from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        button = QPushButton('OK', self)
        button.clicked.connect(self.onMyButtonClick)

    def onMyButtonClick(self, s):
        print('click', s)
        dlg = QDialog()
        dlg.setWindowTitle('Hello')
        dlg.exec_()


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()