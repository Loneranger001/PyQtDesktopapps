from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
import sys
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Awesome App')
        # create a VBox layout
        # layout = QVBoxLayout()
        layout = QHBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        # Dummy widget needed to add layout to the main window and allows us to add it as Central Widget
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
