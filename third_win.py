from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

from instr import *
from second_win import p1, p2, p3


class FinalWin(QWidget):
    def __init__(self, p1, p2, p3):
        super().__init__()

        self.p1 = int(p1) * 4
        self.p2 = int(p2) * 4
        self.p3 = int(p3) * 4

        self.index = self.calc_ruffier()
        self.result_text = self.interpret_result()

        self.initUI()
        self.set_appear()
        self.show()

    def calc_ruffier(self):
        return (self.p1 + self.p2 + self.p3 - 200) / 10

    def interpret_result(self):
        if self.index <= 0:
            return "Excellent cardiac capacity"
        elif self.index <= 5:
            return "Good cardiac capacity"
        elif self.index <= 10:
            return "Average cardiac capacity"
        elif self.index <= 15:
            return "Below average cardiac capacity"
        else:
            return "Poor cardiac capacity"

    def initUI(self):
        self.index_label = QLabel(
            f"Ruffier Index: {self.index:.1f}"
        )
        self.index_label.setAlignment(Qt.AlignCenter)
        self.index_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.result_label = QLabel(self.result_text)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_label)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
