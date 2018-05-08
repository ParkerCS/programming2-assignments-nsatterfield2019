#  Make a desktop calculator app with pyqt  (40pts)
#  Calculator will have the following functions and buttons. 
#     Answer label where your equation and answer will appear.  It will be nicely formatted and update properly with every button push. (10pts)
#     Clear button to zero your answer Label.  (2pts)
#     buttons 0 through 9.   (5pts)
#     *, /, -, and + buttons (5pts)
#     = button to evaluate the current answer label. (5pts)
#     Decimal button to add float capability (2pts)
#     All buttons, columns, and rows will be of same relative size. (3pts)
#     Use a stylesheet to change the color, font and size to approximately match the built in OS calulator app. (5pts)
#     Add one or more additional functional button to your calculator (square, sqrt, pi, memory, trig, or whatever you choose) (3pts)

#  Model your calculator after the built in calc on your operating system.  (minus the +/- and % buttons)


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.equation = ""

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10,10,300,200)


        # Widgets
        self.display = QLabel("0")
        self.grid.addWidget(self.display, 1, 1, 1, 3)

        self.button0 = QPushButton("0")
        self.grid.addWidget(self.button0, 6, 1, 1, 2)

        self.buttondec = QPushButton(".")
        self.grid.addWidget(self.buttondec, 6, 3, 1, 1)

        self.button1 = QPushButton("1")
        self.grid.addWidget(self.button1, 5, 1, 1, 1)

        self.button2 = QPushButton("2")
        self.grid.addWidget(self.button2, 5, 2, 1, 1)

        self.button3 = QPushButton("3")
        self.grid.addWidget(self.button3, 5, 3, 1, 1)

        self.button4 = QPushButton("4")
        self.grid.addWidget(self.button4, 4, 1, 1, 1)

        self.button5 = QPushButton("5")
        self.grid.addWidget(self.button5, 4, 2, 1, 1)

        self.button6 = QPushButton("6")
        self.grid.addWidget(self.button6, 4, 3, 1, 1)

        self.button7 = QPushButton("7")
        self.grid.addWidget(self.button7, 3, 1, 1, 1)

        self.button8 = QPushButton("8")
        self.grid.addWidget(self.button8, 3, 2, 1, 1)

        self.button9 = QPushButton("9")
        self.grid.addWidget(self.button9, 3, 3, 1, 1)

        self.button_mult = QPushButton("x")
        self.grid.addWidget(self.button_mult, 3, 4, 1, 1)

        self.buttonc = QPushButton("C")
        self.grid.addWidget(self.buttonc, 2, 1, 1, 1)

        self.buttonsqr = QPushButton("x^2")
        self.grid.addWidget(self.buttonsqr, 2, 2, 1, 1)

        self.buttonsqroot = QPushButton("x^(1/2)")
        self.grid.addWidget(self.buttonsqroot, 2, 3, 1, 1)

        self.button_div = QPushButton("/")
        self.grid.addWidget(self.button_div, 2, 4, 1, 1)

        self.button_sub = QPushButton("-")
        self.grid.addWidget(self.button_sub, 4, 4, 1, 1)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 5, 4, 1, 1)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 6, 4, 1, 1)




        # Signals and Slots
        self.button1.clicked.connect(lambda: self.concat("1"))
        self.button2.clicked.connect(lambda: self.concat("2"))
        self.button3.clicked.connect(lambda: self.concat("3"))
        self.button4.clicked.connect(lambda: self.concat("4"))
        self.button5.clicked.connect(lambda: self.concat("5"))
        self.button6.clicked.connect(lambda: self.concat("6"))
        self.button7.clicked.connect(lambda: self.concat("7"))
        self.button8.clicked.connect(lambda: self.concat("8"))
        self.button9.clicked.connect(lambda: self.concat("9"))
        self.button0.clicked.connect(lambda: self.concat("0"))
        self.buttondec.clicked.connect(lambda: self.concat("."))
        self.button_div.clicked.connect(lambda: self.concat("/"))
        self.button_sub.clicked.connect(lambda: self.concat("-"))
        self.button_mult.clicked.connect(lambda: self.concat("*"))
        self.button_add.clicked.connect(lambda: self.concat("+"))
        self.buttonsqr.clicked.connect(lambda: self.concat("** 2"))
        self.buttonsqroot.clicked.connect(lambda: self.concat("** (1/2)"))
        self.button_equal.clicked.connect(self.equal)

        # Style

        # Draw

        self.show()
    def concat(self, val):
        self.equation += val
        self.display.setText(self.equation)

    def equal(self):
        try:
            self.equation = str(eval(self.equation))
            self.display.setText(self.equation)

        except:
            self.display.setText("error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())