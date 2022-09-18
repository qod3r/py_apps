import sys
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton,
                             QLabel, 
                             QLineEdit,
                             QCheckBox)


class Boxes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Checkboxes')

        self.btn = QPushButton("text", self)
        self.btn.move(10, 20)
        
        self.label = QLabel("text", self)
        self.label.move(10, 50)
        
        self.inp = QLineEdit(self)
        self.inp.move(10, 75)
        self.inp.resize(100, 30)
        
        self.checkboxes = []
        self.checkstates = []
        self.things = [self.btn, self.label, self.inp]
        
        for i in range(1, 4):
            c = QCheckBox(str(i), self)
            c.move(250, i*20)
            c.clicked.connect(self.handle)
            self.checkboxes.append(c)
            self.checkstates.append(False)

    def handle(self):
        idx = int(self.sender().text()) - 1
        
        if not self.checkstates[idx]:
            self.things[idx].hide()
        else:
            self.things[idx].show()
            
        self.checkstates[idx] = not self.checkstates[idx]
            
        print(f"{self.sender().text()} {self.checkstates[idx]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit{font-size: 24pt;}")

    boxes = Boxes()
    boxes.show()

    sys.exit(app.exec())