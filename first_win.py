from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()

    def initUI(self):
        self.next_button = QPushButton(btn_text_start, self)

        self.welcome_label1 = QLabel(welcome_text1, self)
        self.welcome_label1.setMaximumWidth(700)

        self.welcome_label2 = QLabel(welcome_text2, self)
        self.welcome_label2.setMaximumWidth(700)

        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.welcome_label1)
        self.layoutV.addWidget(self.welcome_label2)
        self.layoutV.addWidget(self.next_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layoutV)

    def connects(self):
        self.next_button.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
        

    def set_appear(self):
        self.setWindowTitle("Health Status Detection Program")
        self.resize(900, win_height)
        self.move(500, 10)
        self.show()

app = QApplication([])
window = MainWindow()
app.exec()

