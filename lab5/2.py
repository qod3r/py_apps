import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('2_ex.ui', self)
        self.connection = sqlite3.connect("films_db.sqlite")
        self.pushButton.clicked.connect(self.select_data)
        self.textEdit.setPlainText("SELECT * FROM films")
        self.select_data()

    def select_data(self):
        query = self.textEdit.toPlainText()
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())