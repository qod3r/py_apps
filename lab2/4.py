import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pprint import pprint
from numpy import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('4_start.ui', self)
        self.start_btn.clicked.connect(self.start)

    def start(self):
        amount = self.rock_count.value()
        if amount > 0:
            uic.loadUi('4_game.ui', self)
            self.restart.setVisible(False)
            self.restart.clicked.connect(self.handle_restart)
            self.rocks.setText(str(amount))
            self.take.clicked.connect(self.handle_take)
    
    def handle_restart(self):
        uic.loadUi('4_start.ui', self)
        self.start_btn.clicked.connect(self.start)
    
    def get_rock_count(self):
        return int(self.rocks.text())
    
    def handle_take(self):
        if self.get_rock_count() - self.spinBox.value() <= 0:
            self.rocks.setText("Вы выиграли!")
            self.take.setEnabled(False)
            self.restart.setVisible(True)
        else:
            self.rocks.setText(str(self.get_rock_count() - self.spinBox.value()))
            self.last_action.setText(f"Вы взяли {self.spinBox.value()}.\n{self.last_action.text()}\n")
            self.ai_move()
    
    def ai_move(self):
        if self.get_rock_count() < 4:
            self.rocks.setText("Вы проиграли!")
            self.take.setEnabled(False)
            self.restart.setVisible(True)
            return
        
        if self.get_rock_count() % 4 == 0:
            value = random.randint(1, 4)
        else:
            value = self.get_rock_count() % 4
        
        self.rocks.setText(str(self.get_rock_count() - value))
        self.last_action.setText(f"\nВаш противник взял {value}.\n{self.last_action.text()}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())