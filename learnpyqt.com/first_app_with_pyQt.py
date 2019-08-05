import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

# app = QApplication([])
# window = QMainWindow()
#
# window.show()  # Important, Windows are hidden by default
#
# # start the event loop
# app.exec_()
# print('Finished!')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Demo Application')
        label = QLabel('<h1>This is a PyQt Window<\h1>')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


app = QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec_())