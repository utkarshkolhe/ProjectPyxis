# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

def onsendc1(self):
    self.label3.setText(self.text1.text())
def window():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle('Pyqt')
    win.button1.clicked.connect(win.onsendc1)

    win.show()

if __name__ == "__main__":
    app = QApplication([])
    # ...
    window()
    sys.exit(app.exec_())
