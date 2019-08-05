from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    # Initialize the class
    def __init__(self):
        super(MainWindow, self).__init__()
        self.windowTitleChanged.connect(self.onwindowTitlechnage)
        self.setWindowTitle('Signals and Slots!')
        self.setWindowIcon(QtGui.QIcon('cricket.png'))
        label = QLabel('This is a label')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    # SLOT: This accepts a string and prints it
    def onwindowTitlechnage(self, s):
        print(s)

    # intercept an event, function name should be same event name
    def contextMenuEvent(self, event):
        print("Context menu event!")
        # In case you still want to call parent event handler
        super(MainWindow, self).contextMenuEvent(event)




app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec_())