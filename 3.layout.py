from qtpy.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton


def say_hello(event):
    print('Hello, world!')


# Initialize application
app = QApplication([])

# Create label
label = QLabel('Hello, world!')

# Create button
button = QPushButton('test')
button.clicked.connect(say_hello)

# Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

# Apply layout to widget
widget = QWidget()
widget.setLayout(layout)

widget.show()

app.exec_()
