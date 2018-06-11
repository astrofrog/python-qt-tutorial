from qtpy.uic import loadUi
from qtpy.QtWidgets import QApplication, QLabel

# Initialize application
app = QApplication([])

# Load file made using Qt Designer
widget = loadUi('mywidget.ui')


def add_star(event):
    widget.list.addItem('A star')


def add_planet(event):
    widget.list.addItem('A planet')


def add_galaxy(event):
    if widget.option.isChecked():
        widget.list.addItem('A BIG galaxy')
    else:
        widget.list.addItem('A galaxy')


# Connect events to buttons
widget.add_star.clicked.connect(add_star)
widget.add_planet.clicked.connect(add_planet)
widget.add_galaxy.clicked.connect(add_galaxy)

widget.show()

# Start 'event loop'
app.exec_()
