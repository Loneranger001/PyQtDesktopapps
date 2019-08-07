from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
import os
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
        self.createbuttons()

    # SLOT: This accepts a string and prints it
    def onwindowTitlechnage(self, s):
        print(s)

    # intercept an event, function name should be same event name
    def contextMenuEvent(self, event):
        print("Context menu event!")
        # In case you still want to call parent event handler
        super(MainWindow, self).contextMenuEvent(event)


    def createbuttons(self):
        pb_browse = QPushButton('Browse', self)
        pb_browse.clicked.connect(self.getFile)


    def getFile(self):
        # path = os.path.join()
        file = QFileDialog.getOpenFileName(self, 'Single File', 'C:\'', "Excel(*.xlsx *.xls)")
        # this returns a tuple with full path
        # print(file)
        # Extracting the file name only
        file_name = os.path.basename(file[0])
        full_path = os.path.dirname(file[0])
        print('File:' + file_name)
        print('full_path:' + full_path)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# main section

if __name__ == '__main__':
    main()


