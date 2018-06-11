from qtpy.QtWidgets import QApplication, QPushButton

# Initialize application
app = QApplication([])

# Define a function to connect to the button
def say_hello(event):
    print('Hello, world!')

# Create button widget and connect to 'say_hello'
button = QPushButton('Say hello')
button.clicked.connect(say_hello)
button.show()

# Start 'event loop'
app.exec_()
