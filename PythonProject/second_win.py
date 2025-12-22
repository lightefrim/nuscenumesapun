from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *
from third_win import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appearance()

    def set_appearance(self):
        self.setWindowTitle("Cardiac capacity program")
        self.resize(win_width, win_height)
        self.move(300, 50)
        self.setLayout(self.layoutv)
        self.show()

    def next_click(self):
        self.hide()

    def connects(self):
        self.btn4.clicked.connect(self.next_click)

    def initUI(self):
        self.label1 = QLabel(label1, self)
        self.label2 = QLabel(label2, self)
        self.label3 = QLabel(label3, self)
        self.label3.setWordWrap(True)
        self.label3.setMaximumWidth(800)
        self.label4 = QLabel(label4, self)
        self.label4.setWordWrap(True)
        self.label4.setMaximumWidth(800)
        self.label5 = QLabel(label5, self)
        self.label5.setWordWrap(True)
        self.label5.setMaximumWidth(800)

        self.btn1 = QPushButton(btn1, self)
        self.btn1.setFixedWidth(150)
        self.btn2 = QPushButton(btn2, self)
        self.btn2.setFixedWidth(150)
        self.btn3 = QPushButton(btn3, self)
        self.btn3.setFixedWidth(150)
        self.btn4 = QPushButton(btn4, self)
        self.btn4.setFixedWidth(150)

        self.le1 = QLineEdit(self)
        self.le1.setFixedWidth(200)
        self.le1.setText(le1)
        self.le2 = QLineEdit(self)
        self.le2.setFixedWidth(200)
        self.le2.setText(le2)
        self.le3 = QLineEdit(self)
        self.le3.setFixedWidth(200)
        self.le3.setText(le3)
        self.le4 = QLineEdit(self)
        self.le4.setFixedWidth(200)
        self.le4.setText(le4)
        self.le5 = QLineEdit(self)
        self.le5.setFixedWidth(200)
        self.le5.setText(le5)

        self.layoutv = QVBoxLayout()
        self.layouth1 = QHBoxLayout()
        self.layouth2 = QHBoxLayout()
        self.layouth3 = QHBoxLayout()
        self.layouth4 = QHBoxLayout()
        self.layouth5 = QHBoxLayout()
        self.layouth6 = QHBoxLayout()
        self.layouth7 = QHBoxLayout()
        self.layouth8 = QHBoxLayout()
        self.layouth9 = QHBoxLayout()
        self.layouth10 = QHBoxLayout()
        self.layouth11 = QHBoxLayout()
        self.layouth12 = QHBoxLayout()
        self.layouth13 = QHBoxLayout()
        self.layouth14 = QHBoxLayout()

        self.layouth1.addWidget(self.label1, Qt.AlignLeft)
        self.layouth2.addWidget(self.le1, Qt.AlignLeft)
        self.layouth3.addWidget(self.label2, Qt.AlignLeft)
        self.layouth4.addWidget(self.le2, Qt.AlignLeft)
        self.layouth5.addWidget(self.label3, Qt.AlignLeft)
        self.layouth6.addWidget(self.btn1, Qt.AlignLeft)
        self.layouth7.addWidget(self.le3, Qt.AlignLeft)
        self.layouth8.addWidget(self.label4, Qt.AlignLeft)
        self.layouth9.addWidget(self.btn2, Qt.AlignLeft)
        self.layouth10.addWidget(self.label5, Qt.AlignLeft)
        self.layouth11.addWidget(self.btn3, Qt.AlignLeft)
        self.layouth12.addWidget(self.le4, Qt.AlignLeft)
        self.layouth13.addWidget(self.le5, Qt.AlignLeft)
        self.layouth14.addWidget(self.btn4, Qt.AlignLeft)

        self.layoutv.addLayout(self.layouth1)
        self.layoutv.addLayout(self.layouth2)
        self.layoutv.addLayout(self.layouth3)
        self.layoutv.addLayout(self.layouth4)
        self.layoutv.addLayout(self.layouth5)
        self.layoutv.addLayout(self.layouth6)
        self.layoutv.addLayout(self.layouth7)
        self.layoutv.addLayout(self.layouth8)
        self.layoutv.addLayout(self.layouth9)
        self.layoutv.addLayout(self.layouth10)
        self.layoutv.addLayout(self.layouth11)
        self.layoutv.addLayout(self.layouth12)
        self.layoutv.addLayout(self.layouth13)
        self.layoutv.addLayout(self.layouth14)

app = QApplication([])
window = MainWindow()
app.exec()





