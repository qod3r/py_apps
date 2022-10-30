import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('4.ui', self)
        self.color = "green"
        self.scale = 1
        self.btn.clicked.connect(self.handle_btn)
        self.slider.valueChanged.connect(self.handle_slider)
        self.label.setPixmap(QPixmap(self.label.size()))
        # self.setCentralWidget(self.label)
    
    def draw_smile(self):
        new_pix = QPixmap(self.label.size())
        new_pix.fill(QColor("black"))
        self.label.setPixmap(new_pix)
        
        p = QPainter(self.label.pixmap())
        
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(self.color))
        p.setPen(pen)
        
        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize((self.scale + 1) * 15)
        p.setFont(font)
        
        p.drawText(0, 0, 730, 360, Qt.AlignHCenter | Qt.AlignVCenter, ':)')
        p.end()
        
    
    def handle_slider(self, v):
        self.scale = v
        self.draw_smile()
        self.update()
    
    def handle_btn(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color
            self.draw_smile()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())