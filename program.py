import sys
import resourse.resource

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


class Window2(QMainWindow):
    def __init__(self, parent=None, word=False, exel=False, power=False):
        super(Window2, self).__init__(parent)
        self.word = word
        uic.loadUi("Windows.ui", self)
        # self.get_tipeFile()
        if self.word is True:
            self.setWindowTitle("Word")
        if power is True:
            self.setWindowTitle("Power Point")
        if exel is True:
            self.setWindowTitle("Exel")
        self.show()

    def get_tipeFile(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Global()
    ex.show()
    sys.exit(app.exec_())