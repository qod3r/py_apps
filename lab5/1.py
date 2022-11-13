import sys
import pandas as pd
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        self.btn.clicked.connect(self.handle)
        
        self.basedf = pd.read_csv('rez.csv')
        self.basedf['school'] = self.basedf['login'].apply(lambda x: x.split('-')[2])
        self.basedf['class'] = self.basedf['login'].apply(lambda x: x.split('-')[3])
        self.basedf['participant_no'] = self.basedf['login'].apply(lambda x: x.split('-')[4])
        self.df = self.basedf.copy()
        self.loadTable()
        print(self.df.head())
        
        schools = sorted(self.basedf['school'].unique().tolist())
        schools.insert(0, 'None')
        self.school_box.addItems(schools)
        
        classes = sorted(self.basedf['class'].unique().tolist())
        classes.insert(0, 'None')
        self.class_box.addItems(classes)
    
    def loadTable(self):
        df = self.df.reset_index(drop=True)[['login', 'user_name', 'Score']]
        while self.table.rowCount() > 0:
            self.table.removeRow(0)
        
        headers = df.columns.values.tolist()
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        
        for i, row in df.iterrows():
            self.table.setRowCount(self.table.rowCount() + 1)
            
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(str(row[j])))
        self.table.resizeColumnsToContents()
    
    def handle(self):
        sel_sch = self.school_box.currentText()
        sel_cl = self.class_box.currentText()
        self.df = self.basedf.copy()
        if sel_sch != 'None' and sel_cl != 'None':
            self.df = self.basedf[(self.basedf['school'] == sel_sch) & (self.basedf['class'] == sel_cl)]
        elif sel_sch != 'None':
            self.df = self.basedf[self.basedf['school'] == sel_sch]
        elif sel_cl != 'None':
            self.df = self.basedf[self.basedf['class'] == sel_cl]
        print(self.df.head())
        self.loadTable()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())