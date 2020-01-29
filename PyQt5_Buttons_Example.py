from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        # Layout for the window
        layout = QHBoxLayout()

        self.go_button = QPushButton("Go")
        # Example without passing data
        #self.go_button.clicked.connect(self.click_my_button)
        # Example using lambda to pass the string "go" to the function
        self.go_button.clicked.connect(lambda: self.click_my_button("go"))
        layout.addWidget(self.go_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(lambda: self.click_my_button("stop"))
        layout.addWidget(self.stop_button)

        # QWidget is the top-level widget that all the other widgets sit in
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def click_my_button(self, x):
        print(x + " button clicked")

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # Windows are hidden by default.

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.

