import sys
from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('2.ui', self)
        self.loadImage_btn.clicked.connect(self.load_image)
        self.transparency_slider.valueChanged.connect(self.update_image)
    
    def update_image(self, pos):
        self.transparency_label.setText(f"{pos}%")
        new_pix = QPixmap(self.pixmap.size())
        new_pix.fill(QColor("transparent"))
        painter = QPainter(new_pix)
        painter.setOpacity(1 - pos * 0.01)
        painter.drawPixmap(QPoint(), self.pixmap)
        painter.end()
        self.image.setPixmap(new_pix)

    def load_image(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Все файлы (*)')
        print(fname)
        self.curr_fname = fname
        self.pixmap = QPixmap(fname[0])
        self.image.setPixmap(self.pixmap)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())