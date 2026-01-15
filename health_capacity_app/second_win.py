from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)

from instr import *
from third_win import FinalWin


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
        self.current_test = None  # Track which test is running

    def start_timer(self):
        """Start timer for first test (15 seconds)"""
        self.current_test = 1
        self.time_left = QTime(0, 0, 15)
        self.text_timer.setText(self.time_left.toString('hh:mm:ss'))
        self.timer.start(1000)

    def start_squats_timer(self):
        """Start timer for squats test (45 seconds)"""
        self.current_test = 2
        self.time_left = QTime(0, 0, 45)
        self.text_timer.setText(self.time_left.toString('hh:mm:ss'))
        self.timer.start(1000)

    def start_final_timer(self):
        """Start timer for final test (60 seconds)"""
        self.current_test = 3
        self.time_left = QTime(0, 1, 0)
        self.text_timer.setText(self.time_left.toString('hh:mm:ss'))
        self.timer.start(1000)

    def update_timer(self):
        self.time_left = self.time_left.addSecs(-1)
        self.text_timer.setText(self.time_left.toString('hh:mm:ss'))

        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
            self.current_test = None

    def set_appearance(self):
        self.setWindowTitle("Cardiac capacity program")
        self.resize(300, win_height)
        self.move(300, 50)
        self.setLayout(self.main_layout)

    def next_click(self):
        try:
            p1 = int(self.le3.text()) if self.le3.text() else 0
            p2 = int(self.le4.text()) if self.le4.text() else 0
            p3 = int(self.le5.text()) if self.le5.text() else 0
            age = int(self.le2.text()) if self.le2.text() else 0

            self.final = FinalWin(age, p1, p2, p3)
            self.final.show()
            self.hide()
        except ValueError:
            # Handle invalid input
            pass


    def connects(self):
        self.btn1.clicked.connect(self.start_timer)
        self.btn2.clicked.connect(self.start_squats_timer)
        self.btn3.clicked.connect(self.start_final_timer)
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
        left_layout.setSpacing(15)  # Add spacing between widgets

        left_layout.addWidget(self.label1)
        left_layout.addWidget(self.le1)
        left_layout.addSpacing(10)  # Extra spacing after name input
        left_layout.addWidget(self.label2)
        left_layout.addWidget(self.le2)
        left_layout.addSpacing(10)  # Extra spacing after age input
        left_layout.addWidget(self.label3)
        left_layout.addWidget(self.btn1)
        left_layout.addWidget(self.le3)
        left_layout.addSpacing(10)  # Extra spacing after test 1
        left_layout.addWidget(self.label4)
        left_layout.addWidget(self.btn2)
        left_layout.addSpacing(10)  # Extra spacing after squats
        left_layout.addWidget(self.label5)
        left_layout.addWidget(self.btn3)
        left_layout.addWidget(self.le4)
        left_layout.addWidget(self.le5)
        left_layout.addSpacing(10)  # Extra spacing before submit
        left_layout.addWidget(self.btn4)

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(left_layout)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.text_timer, alignment=Qt.AlignTop | Qt.AlignRight)







