import sys
from PyQt5 import uic
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPainter, QPixmap, QColor, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget
import random


X, Y = 0, 1


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('3.ui', self)
        
        self.colors = ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#B48EAD", "#4C566A"]
        self.coords = (0, 0)
        pix = QPixmap(self.label.size())
        pix.fill(QColor("white"))
        self.label.setPixmap(pix)
        self.label.setAttribute(Qt.WA_TransparentForMouseEvents)
        
        self.setMouseTracking(True)
    
    def draw_shape(self, shape):
        p = QPainter(self.label.pixmap())
        if shape == "circle":
            print("circle", self.coords)
            pen = QPen()
            pen.setWidth(5)
            color = random.choice(self.colors)
            pen.setColor(QColor(color))
            radius = random.randint(20, 60)
            p.setPen(pen)
            p.setBrush(QColor(color))
            p.drawEllipse(QPoint(self.coords[X], self.coords[Y]), radius, radius)
        elif shape == "square":
            print("square", self.coords)
            pen = QPen()
            pen.setWidth(random.randint(20, 100))
            color = random.choice(self.colors)
            pen.setColor(QColor(color))
            p.setPen(pen)
            p.drawPoint(self.coords[X], self.coords[Y])
        elif shape == "triangle":
            print("triangle")
            pen = QPen()
            pen.setWidth(5)
            color = random.choice(self.colors)
            pen.setColor(QColor(color))
            p.setPen(pen)
            p.setBrush(QColor(color))
            x = self.coords[X]
            y = self.coords[Y]
            size = random.randint(20, 100)
            poly = QPolygon([
                QPoint(x - size//2, y - size//2),
                QPoint(x + size//2 , y - size//2),
                QPoint(x, y + size//2)
            ])
            p.drawPolygon(poly)
            
        p.end()
        self.update()
    
    def mouseMoveEvent(self, event: QMouseEvent):
        self.coords = (event.x(), event.y())

    def mousePressEvent(self, event: QMouseEvent):
        if (event.button() == Qt.LeftButton):
            self.draw_shape("circle")
        elif (event.button() == Qt.RightButton):
            self.draw_shape("square")
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.nativeVirtualKey() == Qt.Key_Space:
            self.draw_shape("triangle")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())