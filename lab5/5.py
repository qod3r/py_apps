import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('5.ui', self)
        
        self.pixmap = QPixmap(self.label.size())
        self.pixmap.load('alien.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

    def check_bounds(self):
        xa = self.label.pos().x()
        ya = self.label.pos().y()
        xb = self.size().width()
        yb = self.size().height()
        if xa <= 0:
            self.label.move(xb, self.label.pos().y())
        if xa >= xb:
            self.label.move(0, self.label.pos().y())
        if ya <= 0:
            self.label.move(self.label.pos().x(), yb)
        if ya >= yb:
            self.label.move(self.label.pos().x(), 0)
    
    def move_alien(self, dir):
        dirs = {
            "up": (0, -20),
            "down": (0, 20),
            "left": (-20, 0),
            "right": (20, 0)
        }
        x = self.label.pos().x()
        y = self.label.pos().y()
        self.label.move(x + dirs[dir][0], y + dirs[dir][1])
        self.check_bounds()

    def keyPressEvent(self, event: QKeyEvent):
        dir = None
        if event.nativeVirtualKey() == Qt.Key_A:
            dir = "left"
        if event.nativeVirtualKey() == Qt.Key_D:
            dir = "right"
        if event.nativeVirtualKey() == Qt.Key_W:
            dir = "up"
        if event.nativeVirtualKey() == Qt.Key_S:
            dir = "down"
        self.move_alien(dir)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())