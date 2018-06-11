from qtpy.QtWidgets import QApplication, QLabel

# Initialize application
app = QApplication([])

# Create label widget
label = QLabel('Hello, world!')
label.show()

# Start 'event loop'
app.exec_()
