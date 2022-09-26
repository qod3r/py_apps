import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pprint import pprint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('3.ui', self)
        self.submit.clicked.connect(self.handle)
        
    def handle(self):
        self.book.addItem(f"{self.name.text()} - {self.phone.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())