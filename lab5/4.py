import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('4.ui', self)
        
        self.coords = (0, 0)
        
        self.setMouseTracking(True)
        
    def inside_btn(self):
        x = self.coords[0]
        y = self.coords[1]
        x1 = self.btn.pos().x()
        y1 = self.btn.pos().y()
        x2 = x1 + self.btn.size().width()
        y2 = y1 + self.btn.size().height()
        
        if (x1 - 5 <= x <= x2 + 5) and (y1 - 5 <= y <= y2 + 5):
            return True
        return False
    
    def move_btn(self):
        newx = random.randint(0, self.size().width() - self.btn.size().width())
        newy = random.randint(0, self.size().height() - self.btn.size().height())
        self.btn.move(newx, newy)
    
    def mouseMoveEvent(self, e):
        self.coords = (e.x(), e.y())
        if self.inside_btn():
            self.move_btn()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())