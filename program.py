import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Global(QMainWindow, QWidget):
    def __init__(self):
        super(Global, self).__init__()
        uic.loadUi('project.ui', self)
        self.setWindowTitle("Window1")
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_3.clicked.connect(self.openWindow)

    def openWindow(self):
        if self.sender().text() == "W":
            Window2(parent=self, word=True)
        if self.sender().text() == "PP":
            Window2(parent=self, power=True)
        if self.sender().text() == "Ex":
            Window2(parent=self, exel=True)


class Window2(QMainWindow, QWidget):
    def __init__(self, parent=None, word=False, exel=False, power=False):
        super(Window2, self).__init__(parent)
        self.word = word
        uic.loadUi("Windows.ui", self)
        self.con = sqlite3.connect("table.sqlite")
        if self.word is True:
            self.setWindowTitle("Word")
            self.iscat.clicked.connect(self.update_result)
            print(1.1)
        if power is True:
            self.setWindowTitle("Power Point")
            self.iscat.clicked.connect(self.update_result)
            print(1.2)
        if exel is True:
            self.setWindowTitle("Exel")
            self.iscat.clicked.connect(self.update_result)
            print(1.3)
        self.show()
        print(1)

    def update_result(self):
        print(3)
        cur = self.con.cursor()
        print(2)
        que = "SELECT * FROM table"
        print(2.1)
        result = cur.execute(que).fetchall()
        print(2.2)
        self.tableWidget.setRowCount(len(result))
        print(2.3)
        self.tableWidget.setColumnCount(len(result[0]))
        print(4)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Global()
    ex.show()
    sys.exit(app.exec_())
