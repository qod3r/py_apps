import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pprint import pprint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        colors = ["red", "green", "blue"]
        
        self.buttonGroups = [self.bg1, self.bg2, self.bg3]
        self.labels = [self.label, self.label_2, self.label_3]
        
        for i, bg in enumerate(self.buttonGroups):
            for j, b in enumerate(bg.buttons()):
                b.setText(colors[j])
                b.id = i
            bg.buttonClicked.connect(self.handle)
            
    def handle(self, a):
        self.labels[a.id].setText(a.text())
        self.labels[a.id].setStyleSheet("QLabel {background-color : " + a.text() + "; color: white}");


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())