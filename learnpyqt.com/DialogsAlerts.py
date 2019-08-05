from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QVBoxLayout
import sys

# create custom dialog box


class CustomDialog(QDialog):
    def __init__(self):
        super(CustomDialog, self).__init__()
        self.setWindowTitle('Are you sure?')
        # buttons that will be available.
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        # create an instance of the button box to hold the buttons
        self.buttonbox = QDialogButtonBox(buttons)
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonbox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Dialogs & Alerts!')
        self.width = 1024
        self.height = 768
        self.setGeometry(50,50,self.width,self.height)
        self.create_buttons()
        # self.onMyToolBarButtonClick('Done')

    def create_buttons(self):
        # self is passed otherwise how it wil know where to place it
        button = QPushButton('OK', self)
        button.setGeometry(50,50,100,30)
        # button1 = QPushButton('cancel', self)
        button.show()
        # button1.show()
        button.clicked.connect(self.onMyToolBarButtonClick)

    def onMyToolBarButtonClick(self, s):
        print('click', s)
        dlg = CustomDialog()
        if dlg.exec_():
            print('Success')
        else:
            print('Cancel!')

    def print_ok(self):
        print('Clicked ok')


def main():
    # Initialize app
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




