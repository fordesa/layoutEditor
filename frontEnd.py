from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KeebCap Creator")
        outer = QHBoxLayout()
        self.setLayout(outer)
        right = QVBoxLayout()
        left = QVBoxLayout()
        outer.addLayout(right)
        outer.addLayout(left)
        rawBox = QGroupBox("Raw Keyboard Data")
        rawLayout = QVBoxLayout()
        rawBox.setLayout(rawLayout)
        rawData = QTextEdit()
        rawLayout.addWidget(rawData)
        left.addWidget(rawBox)
app = QApplication([])
window = Window()
window.show()
app.exec()
