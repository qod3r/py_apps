import sys
import string
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLineEdit)


class Morse(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle('Morse')
        
        with open("morse.txt", "r") as f:
            self.codes = [line.rstrip() for line in f]
        # print(len(self.codes))
        
        self.result = QLineEdit(self)
        self.result.setReadOnly(True)
        self.result.move(125, 50)
        
        self.clear = QPushButton("Clear", self)
        self.clear.move(237, 100)
        self.clear.clicked.connect(self.clear_output)
        
        self.btns = []
        self.chars = string.ascii_uppercase + string.digits
        top_margin = 100
        left_margin = 125
        for i in range(len(self.codes)):
            btn = QPushButton(self.chars[i], self)
            btn.resize(50, 50)
            btn.clicked.connect(self.handle)
            self.btns.append(btn)
            
            if i % 6 == 0:
                top_margin += 50
            btn.move(left_margin + i % 6 * 50, top_margin)

    def handle(self):
        char = str.lower(self.sender().text())
        self.result.setText(self.result.text() + self.codes[self.chars.lower().index(char)])
        
    def clear_output(self):
        self.result.setText("")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit{font-size: 24pt;}")

    morse = Morse()
    morse.show()

    sys.exit(app.exec())