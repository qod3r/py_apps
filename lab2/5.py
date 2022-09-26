import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from pprint import pprint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('5.ui', self)
        self.label = QLabel("", self)
        self.statusbar.addWidget(self.label)
        self.submit.clicked.connect(self.handle)
    
    def handle(self):
        ts = self.source_text.toPlainText()
        tt = self.target_text.toPlainText()
        pct = self.match_pct.value()
        counter = 0
        for line in ts.split("\n"):
            if line in tt:
                counter += 1
                print("matched:")
                print(line, counter)
        res = counter/len(tt.split("\n")) * 100
        self.label.setText(f"{res:.2f}%")
        if res < pct:
            self.label.setStyleSheet("QLabel {background-color : green; color: white}");
        else:
            self.label.setStyleSheet("QLabel {background-color : red; color: white}");


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())