import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableView
import csv
import pandas as pd
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        try:   
            loadUi('UIPro.ui',self)
            print("UI loaded successfully")
        # Command to remove the default Windows Frame Design.
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            # Command to make the backgroud of Window transparent.
            #These 2 lines are used to put funnctions on close and minimize buttons.
            self.minimizeButton.clicked.connect(lambda: self.showMinimized())
            self.CrossButton.clicked.connect(lambda: self.close())
            # Function to load the previous data of student at the start of program.
            self.load_table()
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        except Exception as ex:
            print(f'error loading it {str(ex)}')
    def load_table(self):
            try:
                self.df = pd.read_csv('Github.csv')
                  
                if not self.df.empty:
                    model = QtGui.QStandardItemModel()
                    model.setHorizontalHeaderLabels(self.df.columns.tolist())

                    for row in self.df.values.tolist():
                        items = [QtGui.QStandardItem(str(field)) for field in row]
                        model.appendRow(items)

                    self.Data_Grid.setModel(model)
                else:
                    QMessageBox.warning(self,'warning','CSV File is empty')
            except Exception as ex:
                    QMessageBox.warning(self,'error',f'{str(ex)}')            
    # def load_table(self):
    #     with open('student.csv', "r",encoding="utf-8") as fileInput:
    #         roww = 0
    #         data = list(csv.reader(fileInput))
            
    #         self.StuInfoTable.setRowCount(len(data))
    #         for row in data:
    #             self.StuInfoTable.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
    #             self.StuInfoTable.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
    #             self.StuInfoTable.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
    #             self.StuInfoTable.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
    #             self.StuInfoTable.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
    #             roww =+ 1        
    # def on_sort_finished(self, sorted_df):
    #         self.df = sorted_df
    #         self.load_data()
    #         self.ui.progressBar.setValue(100)

try:
        app = QApplication(sys.argv)
        window = Mainwindow()
        window.show()
        sys.exit(app.exec_())
except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")