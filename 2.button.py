from qtpy.QtWidgets import QApplication, QPushButton


def say_hello(event):
    print('Hello, world!')


# Initialize application
app = QApplication([])

# Create button widget and connect to 'say_hello'
button = QPushButton('Say hello')
button.clicked.connect(say_hello)
button.show()

# Start 'event loop'
app.exec_()
