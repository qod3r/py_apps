import sys
import string
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLineEdit)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle('Calculator')
        
        self.just_clicked = False
        
        self.input = QLineEdit("0", self)
        self.input.move(150, 30)
        self.input.returnPressed.connect(self.calc)
        self.input.selectionChanged.connect(self.reset)
        self.input.textEdited.connect(self.reset)

    def calc(self):
        self.input.setText(f"{self.input.text()} = {str(eval(self.input.text()))}")
        self.just_clicked = True
    
    def reset(self):
        if self.just_clicked:
            self.input.setText("")
            self.just_clicked = False
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit{font-size: 24pt;}")

    calc = Calculator()
    calc.show()

    sys.exit(app.exec())
