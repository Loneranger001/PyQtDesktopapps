import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore


# my class inherits from QMainWindow class
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.title = 'PyQt Layout Demo'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 400
        self.icon = 'upload.png'
        self.footbal = 'Football'
        self.cricket = 'Cricket'
        self.tennis = 'Tennis'
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # create push button
        self.create_layout()
        # show the window
        self.show()

    def create_button(self):
        # button1 = QPushButton('Football', self)
        # button1.setGeometry(100, 100, 150, 50)
        # button1.setIcon(QtGui.QIcon('football-icon-png.png'))
        #
        # button2 = QPushButton('Cricket', self)
        # button2.setGeometry(100, 100, 150, 50)
        # button2.setIcon(QtGui.QIcon('cricket.png'))
        #
        # button3 = QPushButton('Tennis', self)
        # button3.setGeometry(100, 100, 150, 50)
        # button3.setIcon(QtGui.QIcon('tennis.png'))


        # button1.clicked.connect(self.click_me)
        # button2.clicked.connect(self.click_me)
        # button2.clicked.connect(self.click_me)
        None

    def click_me(self):
        print('Button has been clicked!')

    def closewindow(self):
        print('Window will be closed!!')
        sys.exit()

    def create_layout(self):
        self.groupbox = QGroupBox('What is your favorite sport?')
        hboxlayout = QHBoxLayout()

        button1 = QPushButton('Football', self)
        button1.setGeometry(100, 100, 150, 50)
        button1.setIcon(QtGui.QIcon('football-icon-png.png'))

        button2 = QPushButton('Cricket', self)
        button2.setGeometry(100, 100, 150, 50)
        button2.setIcon(QtGui.QIcon('cricket.png'))

        button3 = QPushButton('Tennis', self)
        button3.setGeometry(100, 100, 150, 50)
        button3.setIcon(QtGui.QIcon('tennis.png'))

        hboxlayout.addWidget(button1)
        hboxlayout.addWidget(button2)
        hboxlayout.addWidget(button3)

        self.groupbox.setLayout(hboxlayout)


#
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
