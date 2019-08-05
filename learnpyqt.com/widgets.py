from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Awesome App')
        widget = QLabel('Hello')
        # get the current font
        font = widget.font()
        # update the font
        font.setPointSize(30)
        # reapply
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter|Qt.AlignCenter)
        # self.setCentralWidget(widget)
        cb_brand = QCheckBox()
        cb_brand.setCheckState(Qt.Checked)
        cb_brand.stateChanged.connect(self.show_state)
        self.setCentralWidget(cb_brand)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)



app = QApplication([])
window = MainWindow()
window.show()
app.exec_()