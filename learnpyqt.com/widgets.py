from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Awesome App')
        # widget = QLabel('Hello')
        # # get the current font
        # font = widget.font()
        # # update the font
        # font.setPointSize(30)
        # # reapply
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter|Qt.AlignCenter)
        # self.setCentralWidget(widget)
        # # check box
        # cb_brand = QCheckBox()
        # cb_brand.setCheckState(Qt.Checked)
        # cb_brand.stateChanged.connect(self.show_state)
        # self.setCentralWidget(cb_brand)

        # combo box

        # cb_brands = QComboBox()
        # cb_brands.addItems(['One', 'Two', 'Three'])
        # # this signal sends the current index
        # cb_brands.currentIndexChanged.connect(self.index_changed)
        # # this index sends the currently selected string, this is often more useful
        # cb_brands.currentIndexChanged[str].connect(self.text_changed)
        #
        # self.setCentralWidget(cb_brands)

        # # List boxes
        #
        # cb_brands = QListWidget()
        # cb_brands.addItems(['One', 'Two', 'Three'])
        # cb_brands.currentTextChanged.connect(self.text_changed)
        # cb_brands.currentItemChanged.connect(self.item_changed)
        #
        # self.setCentralWidget(cb_brands)

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter your text here ...')
        widget.setText('File Name will go Here')
        # Making the Text Read only
        # widget.setReadOnly(True)
        # When Enter is pressed.
        widget.returnPressed.connect(self.return_pressed)
        # this will be fired for text selection changed.
        widget.selectionChanged.connect(self.selection_changed)
        # this will be fired for each character deleted or changed.
        widget.textChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def return_pressed(self):
        # This is fired when Enter is pressed
        print('Return Pressed!')


    def selection_changed(self):
        print('selection changed!')

    def text_changed(self):
        print('text changed!')






    # def show_state(self, s):
    #     print(s == Qt.Checked)
    #     print(s)
    #
    # def index_changed(self, i):
    #     print(i)
    #
    # def text_changed(self, s):
    #     print(s == 'One')
    # def item_changed(self, i): # not an index, i is an QListItem
    #     print(i.text())


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()