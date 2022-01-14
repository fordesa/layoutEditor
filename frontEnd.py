from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KeebCap Creator")
        
        # Overall layout
        outer = QHBoxLayout()
        self.setLayout(outer)
        
        # Raw Data Input
        rawBox = QGroupBox("Raw Keyboard Data")
        rawLayout = QVBoxLayout()
        rawBox.setLayout(rawLayout)
        rawData = QTextEdit()
        rawLayout.addWidget(rawData)
        outer.addWidget(rawBox)
        
        # Basic Settings
        basicBox = QGroupBox("Basic Settings")
        basicLayout = QFormLayout()
        basicBox.setLayout(basicLayout)
        
        # Basic Settings ComboBoxes
        profiles = ["dcs", "oem", "dsa", "sa", "g20", "disabled"]
        rows = ["0", "1", "2", "3", "4", "5"]
        stemTypes = ["cherry", "alps", "rounded_cherry", "box_cherry", "filled", "disabled"]
        supportTypes = ["flared", "bars", "flat", "disabled"]
        stemSupportTypes = ["tines", "brim", "disabled"]
        
        profileBox = QComboBox()
        rowBox = QComboBox()
        stemBox = QComboBox()
        supportBox = QComboBox()
        stemSupportBox = QComboBox()
        fontBox = QComboBox() # TODO add font types
        
        profileBox.addItems(profiles)
        rowBox.addItems(rows)
        stemBox.addItems(stemTypes)
        supportBox.addItems(supportTypes)
        stemSupportBox.addItems(stemSupportTypes)
        
        # Basic Settings LineEdit
        legend = QLineEdit("")
        stemSlope = QLineEdit("0.35")
        stemInnerSlope = QLineEdit("0.2")
        fontSize = QLineEdit("6")
        doubleSculptRadius = QLineEdit("200")
        
        stemSlope.setValidator(QDoubleValidator())
        stemInnerSlope.setValidator(QDoubleValidator())
        fontSize.setValidator(QIntValidator())
        doubleSculptRadius.setValidator(QDoubleValidator())
        
        # Basic Settings CheckBoxes
        invertedDish = QCheckBox("")
        outsetLegend = QCheckBox("")
        
        # Add Basic Settings in Order
        basicLayout.addRow(QLabel("Keycap Profile"), profileBox)
        basicLayout.addRow(QLabel("Row"), rowBox)
        basicLayout.addRow(QLabel("Legend"), legend)
        basicLayout.addRow(QLabel("Stem Type"), stemBox)
        basicLayout.addRow(QLabel("Stem Slope"), stemSlope)
        basicLayout.addRow(QLabel("Stem Inner Slope"), stemInnerSlope)
        basicLayout.addRow(QLabel("Font Size"), fontSize)
        basicLayout.addRow(QLabel("Inverted Dish"), invertedDish)
        basicLayout.addRow(QLabel("Double Sculpt Radius"), doubleSculptRadius)
        basicLayout.addRow(QLabel("Support Type"), supportBox)
        basicLayout.addRow(QLabel("Stem Support Type"), stemSupportBox)
        basicLayout.addRow(QLabel("Outset Legend"), outsetLegend)
                
        # Overall Settings
        settings = QTabWidget()
        settings.addTab(basicBox, "Basic Settings")
        outer.addWidget(settings)
        
app = QApplication([])
window = Window()
window.show()
app.exec()
