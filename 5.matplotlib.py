from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

# Initialize application
app = QApplication([])

# Create Matplotlib figure and canvas
fig = Figure()
ax = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasQTAgg(fig)


def plot_points(event):
    x = np.random.random(1000)
    y = np.random.random(1000)
    ax.cla()
    ax.plot(x, y, '.')
    fig.canvas.draw()


# Create button
button = QPushButton('test')
button.clicked.connect(plot_points)

# Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(canvas)
layout.addWidget(button)

# Apply layout to widget
widget = QWidget()
widget.setLayout(layout)

widget.show()

# Start 'event loop'
app.exec_()
