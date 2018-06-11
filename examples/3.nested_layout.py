from qtpy.QtWidgets import (QApplication, QLabel, QWidget,
                            QHBoxLayout, QVBoxLayout, QPushButton)

# Initialize application
app = QApplication([])

# Set up individual widgets
label1 = QLabel('My wonderful application')
label2 = QLabel('The button:')
button = QPushButton('Press me!')

# Combine label2 and button into a single widget
bottom_widget = QWidget()
bottom_layout = QHBoxLayout()
bottom_layout.addWidget(label2)
bottom_layout.addWidget(button)
bottom_widget.setLayout(bottom_layout)

# Combine this widget with label1 to form the main window
widget = QWidget()
layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(bottom_widget)
widget.setLayout(layout)

# Show main widget
widget.show()

# Start event loop
app.exec_()
