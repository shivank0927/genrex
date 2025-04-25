from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from utils import *
from PyQt5.QtGui import QFont
import sys

buttonSymbols = [
    "7", "8", "9", "*",
    "4", "5", "6", "/", 
    "1", "2", "3", "-", 
    "0", ".", "=", "+"
]

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("calculator")
        self.resize(500, 500)

        self.masterLayout = QVBoxLayout()
        self.buttonGridLayout = QGridLayout()


        self.textBox = QLineEdit()
        self.textBox.setPlaceholderText("expression")
        self.textBox.setStyleSheet("font-family: 'Source Code Pro'; font-size: 16px; padding: 10px;")
        self.masterLayout.addWidget(self.textBox) # adding textbox direct - > master

        
        for index, symbol in enumerate(buttonSymbols):
            row = index // 4
            col = index % 4

            button = QPushButton(symbol)

            if symbol == "=":
                button.setStyleSheet(equalsButtonStyle)
            else:
                button.setStyleSheet(buttonStyle)

            button.clicked.connect(self.calculationEvent)
            self.buttonGridLayout.addWidget(button, row, col)

        self.masterLayout.addLayout(self.buttonGridLayout)


        self.endButtonLayout = QHBoxLayout()

        self.clearButton = QPushButton("C") # clear and del btns
        self.clearButton.setStyleSheet(clearButtonStyle)
        self.clearButton.clicked.connect(self.calculationEvent)

        self.deleteButton = QPushButton("<<")
        self.deleteButton.setStyleSheet(deleteButtonStyle)
        self.deleteButton.clicked.connect(self.calculationEvent)

        self.endButtonLayout.addWidget(self.clearButton)
        self.endButtonLayout.addWidget(self.deleteButton)

        self.masterLayout.addLayout(self.endButtonLayout)
        self.masterLayout.setContentsMargins(25, 25, 25, 25)

        self.setLayout(self.masterLayout)

    def calculationEvent(self):
        button = self.sender()
        symbol = button.text()

        if symbol == "=":
            expression = self.textBox.text()
            try:
                result = eval(expression)
                self.textBox.setText(str(result))
            except Exception as e:
                self.textBox.setText(f"error: {e}")

        elif symbol == "C":
            self.textBox.clear()

        elif symbol == "<<":
            current = self.textBox.text()
            self.textBox.setText(current[:-1])

        else:
            current = self.textBox.text()
            self.textBox.setText(current + symbol)

if __name__ == "__main__":

    app = QApplication([])
    calculator = Calculator()
    calculator.setStyleSheet("QWidget { background-color: #adb8ba; }")
    calculator.show()
    app.exec_()
