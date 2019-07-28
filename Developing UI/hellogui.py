import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui


# my class inherits from QMainWindow class
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.title = 'UDA Upload tool'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 400
        self.icon = 'upload.png'
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.pushButtons()
        self.show()

    def pushButtons(self):
        button = QPushButton('Upload', self)
        # move the button to position
        button.move(500, 50)
        button.setIcon(QtGui.QIcon(self.icon))
        button.setToolTip('This is for UDA upload')

#
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
