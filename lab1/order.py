import sys
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLabel,
                             QSpinBox)


class Order(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle('Order')
        
        self.test_items = [{
            "name": "pizza",
            "price": 199
        }, {
            "name": "bruh",
            "price": 299
        }, {
            "name": "asdasd",
            "price": 1000
        }]
        
        y_offset = 30
        
        self.controls = []
        self.totals = []
        idx = 0
        for i in self.test_items:
            name = QLabel(i["name"], self)
            name.move(30, y_offset)
            price = QLabel(str(i["price"]), self)
            price.move(30, y_offset + 20)
            
            control = QSpinBox(self)
            control.id = idx
            idx += 1
            control.move(150, y_offset)
            control.valueChanged.connect(self.handle_count)
            self.controls.append(control)

            total = QLabel("0.00", self)
            total.move(150, y_offset + 20)
            total.resize(100, 20)
            self.totals.append(total)
            
            y_offset += 60
        
        self.total = QLabel("0.00", self)
        self.total.move(400, 400)
        self.total.resize(100, 20)
        
        self.open_cheque = QPushButton("Чек", self)
        self.open_cheque.move(375, 420)
        self.open_cheque.clicked.connect(self.cheque_window)
        
    def handle_count(self, v):
        i = self.sender().id
        self.totals[i].setText(str(v * self.test_items[i]["price"]) + ".00")
        
        self.total.setText(str(sum(float(c.text()) for c in self.totals)) + "0")
    
    def cheque_window(self):
        positions = []
        pos = 1
        for i in range(len(self.controls)):
            if self.controls[i].value() != 0:
                item = self.test_items[i]
                positions.append(f"#{pos}  {item['name']}    {item['price']} x {self.controls[i].value()}")
                pos += 1
                
        total = (str(sum(float(c.text()) for c in self.totals)) + "0")
        self.cheque_window = Cheque(positions, total)
        self.cheque_window.show()


class Cheque(QWidget):
    def __init__(self, positions, total):
        super().__init__()
        self.initUI(positions, total)
    
    def initUI(self, positions, total):
        self.setGeometry(300, 300, 250, 300)
        self.setWindowTitle('Чек')
        
        self.labels = []
        offset = 10
        for s in positions:
            self.labels.append(QLabel(s, self).move(10, offset))
            offset += 20
        
        self.labels.append(QLabel(total, self).move(180, offset + 50))
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit{font-size: 24pt;}")

    order = Order()
    order.show()

    sys.exit(app.exec())