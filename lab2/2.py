import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pprint import pprint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('2.ui', self)
        self.submit.clicked.connect(self.handle)

    def handle(self):
        date = self.calendar.selectedDate().toString('dd.MM.yyyy')
        time = self.time.time().toString('hh:mm')
        # print(self.name.text())
        
        self.list.addItem(f"{self.name.text()} -- {date} {time}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())