from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Calculator')
text = QLabel('Calculator')
my_win.move(500 ,10)
my_win.resize(900, 500)
n1 = randint(1,100)
n2 = randint(1,100)
res = 0

button1 = QPushButton('+')
button2 = QPushButton('-')
button3 = QPushButton('*')
button4 = QPushButton('/')
button5 = QPushButton('=')
button6 = QLabel('')

button7 = QLabel(f'{n1}')
button8 = QLabel(f'{n2}')

lh12 = QHBoxLayout()
lh2 = QHBoxLayout()
lh3 = QHBoxLayout()
lh4 = QHBoxLayout()

lh1 = QVBoxLayout()

lh2.addWidget(button7, alignment=Qt.AlignCenter)
lh2.addWidget(button6, alignment=Qt.AlignCenter)
lh3.addWidget(button1, alignment=Qt.AlignCenter)
lh3.addWidget(button2, alignment=Qt.AlignCenter)
lh3.addWidget(button3, alignment=Qt.AlignCenter)
lh3.addWidget(button4, alignment=Qt.AlignCenter)
lh2.addWidget(button8, alignment=Qt.AlignCenter)
lh12.addWidget(button5, alignment=Qt.AlignCenter)

lh1.addLayout(lh2)
lh1.addLayout(lh12)
lh1.addLayout(lh3)
lh1.addLayout(lh4)

def add(n1,n2):
    res = n1 + n2
    return res
def scadere(n1, n2):
    res = n1 - n2
    return res
def inmultire(n1, n2):
    res = n1 * n2
    return res
def impartire(n1, n2):
    if n2 != 0:
        res = n1 / n2
        return res
    else:
        button8.setText('Invalid number')
def show_result(res):
    button6.setText(res)


my_win.setLayout(lh1)

button1.clicked.connect(add)
button2.clicked.connect(scadere)
button3.clicked.connect(inmultire)
button4.clicked.connect(impartire)
button5.clicked.connect(show_result)

my_win.show()
app.exec_()
