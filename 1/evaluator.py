import sys
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLineEdit)


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 500, 50)
        self.setWindowTitle('Eval')
        
        self.btn = QPushButton('-->', self)
        self.btn.resize(60, 50)
        self.btn.move(280, 0)
        self.btn.clicked.connect(self.evaluate)
        
        self.input = QLineEdit(self)
        self.input.resize(280, 50)
        
        self.output = QLineEdit(self)
        self.output.resize(160, 50)
        self.output.move(340, 0)
    
    def evaluate(self):
        expr = self.input.text()
        res = eval(expr)
        self.output.setText(str(res))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit{font-size: 24pt;}")

    evaluator = Evaluator()
    evaluator.show()

    sys.exit(app.exec())