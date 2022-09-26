import sys
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLineEdit)


class Mover(QWidget):
    btn_states = ["-->", "<--"]
    btn_curr_state = 0
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 500, 50)
        self.setWindowTitle('Word mover')
        
        self.btn = QPushButton('-->', self)
        self.btn.resize(60, 50)
        self.btn.move(220, 0)
        self.btn.clicked.connect(self.move)
        
        self.left = QLineEdit(self)
        self.left.resize(220, 60)

        self.right = QLineEdit(self)
        self.right.resize(220, 60)
        self.right.move(280, 0)
        self.right.setReadOnly(True)
        
    def move(self):
        if self.btn_curr_state:
            self.left.setText(self.right.text())
            self.right.setText("")
            self.left.setReadOnly(False)
            self.right.setReadOnly(True)
        else:
            self.right.setText(self.left.text())
            self.left.setText("")
            self.right.setReadOnly(False)
            self.left.setReadOnly(True)
        
        self.btn.setText(self.btn_states[not self.btn_curr_state])
        self.btn_curr_state = not self.btn_curr_state
        
        pprint(vars(self))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit{font-size: 30pt;}")

    mover = Mover()
    mover.show()

    sys.exit(app.exec())