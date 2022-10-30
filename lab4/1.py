import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PIL import Image
import numpy as np


def single_channel(fname, channel):
    a = []
    if channel == "r":
        a = [1, 2]
    if channel == "g":
        a = [0, 2]
    if channel == "b":
        a = [0, 1]
    
    img = Image.open(fname)
    img = np.array(img)
    img[:, :, a] *= 0
    img = Image.fromarray(img)
    return pil2pixmap(img)

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif  im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        self.loadImage_btn.clicked.connect(self.load_image)
        self.channel_btn.clicked.connect(self.change_channel)
        self.rotate_btn.clicked.connect(self.rotate)
    
    def rotate(self):
        self.pixmap = self.pixmap.transformed(QTransform().rotate(90))
        self.image.setPixmap(self.pixmap)
    
    def change_channel(self):
        channel, ok_pressed = QInputDialog.getItem(
            self, "Выбор канала", "канал",
            ("r", "g", "b"), 0, False)
        if ok_pressed:
            self.pixmap = single_channel(self.curr_fname[0], channel)
            self.image.setPixmap(self.pixmap)

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