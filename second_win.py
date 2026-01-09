from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)

from instr import *


class FinalWin(QWidget):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.setWindowTitle("Results")

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Test 1: {p1}"))
        layout.addWidget(QLabel(f"Test 2: {p2}"))
        layout.addWidget(QLabel(f"Test 3: {p3}"))

        self.setLayout(layout)

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()
        self.connects()
        self.set_appearance()
        self.show()

    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_left = QTime(0, 0, 15)

    def start_timer(self):
        self.time_left = QTime(0, 0, 15)
        self.text_timer.setText(self.time_left.toString('hh:mm:ss'))
        self.timer.start(1000)

    def update_timer(self):
        self.time_left = self.time_left.addSecs(-1)
        self.text_timer.setText(self.time_left.toString('hh:mm:ss'))

        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()

    def set_appearance(self):
        self.setWindowTitle("Cardiac capacity program")
        self.resize(300, win_height)
        self.move(300, 50)
        self.setLayout(self.main_layout)

    def next_click(self):
        p1 = self.le3.text()
        p2 = self.le4.text()
        p3 = self.le5.text()

        self.final = FinalWin(p1, p2, p3)
        self.final.show()
        self.hide()


    def connects(self):
        self.btn1.clicked.connect(self.start_timer)
        self.btn4.clicked.connect(self.next_click)

    def initUI(self):
        self.label1 = QLabel(label1)
        self.label2 = QLabel(label2)
        self.label3 = QLabel(label3)
        self.label3.setWordWrap(True)

        self.label4 = QLabel(label4)
        self.label4.setWordWrap(True)

        self.label5 = QLabel(label5)
        self.label5.setWordWrap(True)

        self.text_timer = QLabel("00:00:15")
        self.text_timer.setFont(QFont("Times", 28, QFont.Bold))
        self.text_timer.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.btn1 = QPushButton(btn1)
        self.btn2 = QPushButton(btn2)
        self.btn3 = QPushButton(btn3)
        self.btn4 = QPushButton(btn4)

        self.le1 = QLineEdit(le1)
        self.le2 = QLineEdit(le2)
        self.le3 = QLineEdit(le3)
        self.le4 = QLineEdit(le4)
        self.le5 = QLineEdit(le5)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        left_layout.addWidget(self.label1)
        left_layout.addWidget(self.le1)
        left_layout.addWidget(self.label2)
        left_layout.addWidget(self.le2)
        left_layout.addWidget(self.label3)
        left_layout.addWidget(self.btn1)
        left_layout.addWidget(self.le3)
        left_layout.addWidget(self.label4)
        left_layout.addWidget(self.btn2)
        left_layout.addWidget(self.label5)
        left_layout.addWidget(self.btn3)
        left_layout.addWidget(self.le4)
        left_layout.addWidget(self.le5)
        left_layout.addWidget(self.btn4)

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(left_layout)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.text_timer, alignment=Qt.AlignTop | Qt.AlignRight)


app = QApplication([])
window = MainWindow()
app.exec()







