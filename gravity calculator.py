# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a pyqt5 app with the following attributes:
# - use an App/Window class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function or custom method
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 2 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10,10,300,300)

        # Widget
        self.title = QLabel("Universal Gravity Calculator:")
        self.grid.addWidget(self.title, 1, 1, 2, 1)
        self.title.setObjectName("title")

        self.label_radius = QLabel("Center to center distance between objects:")
        self.grid.addWidget(self.label_radius, 2, 1, 1, 1)

        self.label_mass1 = QLabel("Mass of first object:")
        self.grid.addWidget(self.label_mass1, 3, 1, 1, 1)

        self.label_mass2 = QLabel("Mass of second object:")
        self.grid.addWidget(self.label_mass2, 4, 1, 1, 1)

        self.radius = QLineEdit()
        self.grid.addWidget(self.radius, 2, 2, 1, 1)

        self.mass1 = QLineEdit()
        self.grid.addWidget(self.mass1, 3, 2, 1, 1)

        self.mass2 = QLineEdit()
        self.grid.addWidget(self.mass2, 4, 2, 1, 1)

        self.calc = QPushButton("Calculate")
        self.grid.addWidget(self.calc, 5, 1, 1, 1)

        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 5, 2, 1, 1)



        # Singals/Slots
        self.calc.clicked.connect(self.find_gravity)

        # Set Style
        self.set_style()

        # Draw
        self.show()

    def set_style(self):
        style_sheet = "gcalc style.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())



    def find_gravity(self):
        try:
            r = float(self.radius.text())
            m1 = float(self.mass1.text())
            m2 = float(self.mass2.text())

            c = (6.67e-11 * (m1 * m2)) / r ** 2

            self.answer.setText(str(c))
        except:
            self.answer.setText("error")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())

