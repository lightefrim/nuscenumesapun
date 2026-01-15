from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

from instr import *


class FinalWin(QWidget):
    def __init__(self, age, p1, p2, p3):
        super().__init__()

        # p1, p2, p3 are already 15-second pulse counts
        # Convert to beats per minute by multiplying by 4
        self.p1_bpm = int(p1) * 4 if p1 else 0  # Resting heart rate (15 sec * 4 = BPM)
        self.p2_bpm = int(p2) * 4 if p2 else 0  # Heart rate after exercise (15 sec * 4 = BPM)
        self.p3_bpm = int(p3) * 4 if p3 else 0  # Heart rate 1 min after exercise (15 sec * 4 = BPM)
        self.age = int(age) if age else 0

        self.index = self.calc_ruffier()
        self.result_text = self.interpret_result()

        self.initUI()
        self.set_appear()
        self.show()

    def calc_ruffier(self):
        """
        Calculate Ruffier Index using the standard formula:
        Ruffier Index = (P1 + P2 + P3 - 200) / 10
        where:
        P1 = resting heart rate (BPM)
        P2 = heart rate immediately after exercise (BPM)
        P3 = heart rate 1 minute after exercise (BPM)
        """
        if self.p1_bpm == 0 or self.p2_bpm == 0 or self.p3_bpm == 0:
            return None
        
        ruffier_index = (self.p1_bpm + self.p2_bpm + self.p3_bpm - 200) / 10
        return ruffier_index

    def interpret_result(self):
        if self.index is None:
            return "Please complete all tests to get results"
        
        # Ruffier Index interpretation (standard medical ranges)
        if self.index <= 0:
            return "Excellent cardiac capacity - Your heart is in great shape!"
        elif self.index <= 5:
            return "Good cardiac capacity - Your cardiovascular fitness is above average"
        elif self.index <= 10:
            return "Average cardiac capacity - Your heart fitness is within normal range"
        elif self.index <= 15:
            return "Below average cardiac capacity - Consider regular exercise to improve"
        else:
            return "Poor cardiac capacity - Please consult with a healthcare provider"

    def initUI(self):
        if self.index is not None:
            self.index_label = QLabel(
                f"Ruffier Index: {self.index:.1f}"
            )
            self.details_label = QLabel(
                f"Resting HR: {self.p1_bpm} bpm | After Exercise: {self.p2_bpm} bpm | Recovery: {self.p3_bpm} bpm"
            )
        else:
            self.index_label = QLabel("Ruffier Index: N/A")
            self.details_label = QLabel("")
        
        self.index_label.setAlignment(Qt.AlignCenter)
        self.index_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        self.details_label.setAlignment(Qt.AlignCenter)
        self.details_label.setStyleSheet("font-size: 14px; color: #666;")

        self.result_label = QLabel(self.result_text)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px; padding: 10px;")

        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.addWidget(self.index_label)
        self.layout.addWidget(self.details_label)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
