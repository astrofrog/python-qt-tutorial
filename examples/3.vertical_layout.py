from qtpy.QtWidgets import (QApplication, QLabel, QWidget,
                            QVBoxLayout, QPushButton)

# Initialize application
app = QApplication([])

# Create label and button
label = QLabel('Hello, world!')
button = QPushButton('test')

# Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

# Apply layout to widget
widget = QWidget()
widget.setLayout(layout)

# Show widget
widget.show()

# Start event loop
app.exec_()
