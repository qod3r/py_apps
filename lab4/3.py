import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QVBoxLayout
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('3.ui', self)
        self.btn.clicked.connect(self.handle)
    
    def create_flags(self, count):
        colors = ["black", "green", "red", "yellow", "blue", "purple"]
        for i in range(count):
            label = QLabel(self)
            # label.resize(100, 50)
            # label.move(100, 50 + 50*i)
            label.setStyleSheet("QLabel {background-color : " + f"{random.choice(colors)}" + ";}")
            self.flag.addWidget(label)
    
    def handle(self):
        colors, ok_pressed = QInputDialog.getInt(
            self, "Выбор цветов", "Выберите количество цветов",
            3, 1, 10, 1)
        if ok_pressed:
            self.create_flags(colors)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())