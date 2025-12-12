from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import *
from instr import *
from second_win import TestWIn

class MainWindow(self):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.next_button = QPushButton(btn_txt_start, self)
        self.welcome_label1 = QLabel(welcome_text1,self)
        self.welcome_label2 =  QLabel(welcome_tex2, self)
        self_layoutV = QVBoxLayout()
        self_layoutV.addWidget(self.welcome_label1, alignment=Qt.AlignLeft)
        self_layoutV.addWidget(self.welcome_label2 ,alignement=Qt.AlignLeft)
        self.layoutV.addWidget(self.next_button,alignment=Qt.AlignCenter)
        self.setLayout(self_layoutV)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.next_button.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle("Cardiac capacity prorgram")
        self.resize(win_width, win_height)
        self.move(500, 10)
        self.show()

app = QApplication([])
app.exec_()