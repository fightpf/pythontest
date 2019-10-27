import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.button=QtWidgets.QPushButton(self)
        self.button.setText("hello")

app=None
window=None

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())