#  """
#  The code burger:

#  1. all imports 
#  2. main app objects and settings
#  3. create all widgets needed in application.
#  4. design your layouts, add widgets to the screen
#  5. set the final layout to the main window
#  6. show and execute the application

#  """
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

mywords=["sdlf", "234", "lksadjf", "lkasjf403"]


application = QApplication([])
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("test application")

# create all objects
title_text = QLabel("random keywords")
txt1 = QLabel("vietnam")
txt2 = QLabel("?")
txt3 = QLabel("goodbye")

btn1 = QPushButton("click me")
btn2 = QPushButton("click me")
btn3 = QPushButton("click me")

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)
row2.addWidget(txt1, alignment=Qt.AlignLeft)
row2.addWidget(txt2, alignment=Qt.AlignCenter)
row2.addWidget(txt3, alignment=Qt.AlignRight)

row3.addWidget(btn1, alignment=Qt.AlignLeft)
row3.addWidget(btn2, alignment=Qt.AlignCenter)
row3.addWidget(btn3, alignment=Qt.AlignRight)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

# creating functions

def random_word1():
    word = random.choice(mywords)
    txt1.setText(word)

def random_word2():
    word = random.choice(mywords)
    txt2.setText(word)
    
def random_word3():
    word = random.choice(mywords)
    txt3.setText(word)


#events

btn1.clicked.connect(random_word1)
btn2.clicked.connect(random_word2)
btn3.clicked.connect(random_word3)

window.setLayout(master_layout)
window.show()
application.exec_()

