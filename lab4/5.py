import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('5.ui', self)
        self.btn.clicked.connect(self.handle)
        
    def handle(self):
        formula = self.formula.text()
        r = self.range.text()
        
        r = eval(r)
        rstart, rstop, count = -10, 10, 21
        if isinstance(r, int):
            rstop = r
        elif isinstance(r, tuple):
            rstart = r[0]
            rstop = r[1]
            if len(r) == 3:
                count = r[2]
            print(f"start: {rstart}, stop: {rstop}, count: {count}")
            
        self.graphicsView.clear()
        self.graphicsView.plot(np.linspace(rstart, rstop, count), [eval(formula) for x in np.linspace(rstart, rstop, count)])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())