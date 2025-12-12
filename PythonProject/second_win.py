from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import *
from instr import *
from third_win import *

class MainWindow(self):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appearance()
        self.show()
    def initUi(self):
        self.label1 = QLabel(label1, self)
        self.label2 = QLabel(label2, self)
        self.label3 = QLabel(lable3, self)
        self.label4 = QLabel(label4, self)
        self.label5 = QLabel(label5, self)
        self.btn1 = QPushButton(btn1, self)
        self.btn2 = QPushButton(btn2, self)
        self.btn3 = QPushButton(btn3, self)
        self.btn4 = QPushButton(btn4, self)
        self.timer = QLabel()
        self.le1 = QLineEdit(le1, self)
        self.le2 = QLineEdit(le2, self)
        self.le3 = QLineEdit(le3, self)
        self.le4 = QLineEdit(le4, self)

