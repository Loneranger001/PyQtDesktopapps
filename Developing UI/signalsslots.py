import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore


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
        # create push button
        self.pushButtons()
        # show the window
        self.show()

    def pushButtons(self):
        button = QPushButton('Upload', self)
        button1 = QPushButton('Close Application',self)
        button1.setGeometry(400,80,200,30)
        button.setGeometry(400, 40, 200, 30)
        # button1.move(500, 80)
        button1.setIcon(QtGui.QIcon('close.png'))
        # move the button to position
        # button.move(500, 50)
        button.setIcon(QtGui.QIcon(self.icon))
        # button.setToolTip('This is for UDA upload')
        # connect the slot/function with clicking of the button
        button.clicked.connect(self.ClickMe)
        button1.clicked.connect(self.closewindow)

    def ClickMe(self):
        print('Button has been clicked!')

    def closewindow(self):
        print('Window will be closed!!')
        sys.exit()
#
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
