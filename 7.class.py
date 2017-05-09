from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MyMatplotlibWidget(QWidget):

    def __init__(self, parent=None):

        super(MyMatplotlibWidget, self).__init__(parent=parent)

        # Create Matplotlib figure and canvas
        self.fig = Figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasQTAgg(self.fig)

        # Create button
        self.button = QPushButton('test')
        self.button.clicked.connect(self.plot_points)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def plot_points(self, event):
        x = np.random.random(1000)
        y = np.random.random(1000)
        self.ax.cla()
        self.ax.plot(x, y, '.')
        self.fig.canvas.draw()


app = QApplication([])

widget = MyMatplotlibWidget()
widget.show()

app.exec_()
