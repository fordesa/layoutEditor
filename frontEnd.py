from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keycap Creator")
        outer = QHBoxLayout()
        
        # Raw Data Input
        rawBox = QGroupBox("Raw Keyboard Data")
        rawLayout = QVBoxLayout()
        rawBox.setLayout(rawLayout)
        rawData = QTextEdit()
        rawLayout.addWidget(rawData)
        io = QVBoxLayout()
        output = QPushButton("Generate File")
        output.clicked.connect(self.parser())
        io.addWidget(raw)
        io.addWidget(output)
        outer.addLayout(io)

        self.setLayout(outer)
        raw = self.rawInput()
        basic = self.basicSettings()
        key = self.keySettings()
        stem = self.stemSettings()
        shape = self.shapeSettings()
        misc = self.miscSettings()
        feat = self.features()
        
        settings = QTabWidget()
        settings.addTab(basic, "Basic Settings")
        settings.addTab(key, "Key Settings")
        settings.addTab(stem, "Stem Settings")
        settings.addTab(shape, "Shape Settings")
        settings.addTab(misc, "Misc Settings")
        settings.addTab(feat, "Features")
        

        outer.addWidget(settings)
    def basicSettings(self):
        # Basic Settings
        basicBox = QGroupBox("Basic Settings")
        basicLayout = QFormLayout()
        basicBox.setLayout(basicLayout)
        
        # Basic Settings ComboBoxes
        profiles = ["dcs", "oem", "dsa", "sa", "g20", "disabled"]
        stemTypes = ["cherry", "alps", "rounded_cherry", "box_cherry", "filled", "disabled"]
        supportTypes = ["flared", "bars", "flat", "disabled"]
        stemSupportTypes = ["tines", "brim", "disabled"]
        
        profileBox = QComboBox()
        stemBox = QComboBox()
        supportBox = QComboBox()
        stemSupportBox = QComboBox()
        
        profileBox.addItems(profiles)
        stemBox.addItems(stemTypes)
        supportBox.addItems(supportTypes)
        stemSupportBox.addItems(stemSupportTypes)
        
        # Basic Settings Spinners and Text Edits
        legend = QLineEdit("")
        stemSlope = QDoubleSpinBox()
        stemInnerSlope = QDoubleSpinBox()
        fontSize = QSpinBox()
        doubleSculptRadius = QSpinBox()
        
        stemSlope.setSingleStep(0.01)
        stemInnerSlope.setSingleStep(.1)
        doubleSculptRadius.setRange(-1000, 1000) # arbitrary value
        stemSlope.setValue(0.35)
        stemInnerSlope.setValue(0.2)
        fontSize.setValue(6)
        doubleSculptRadius.setValue(200)
        
        # Basic Settings CheckBoxes
        invertedDish = QCheckBox("")
        outsetLegend = QCheckBox("")
        
        # Add Basic Settings in Order
        basicLayout.addRow(QLabel("Keycap Profile"), profileBox)
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
        
        return basicBox
    def keySettings(self):
        # Key Settings
        keyBox = QGroupBox("Key Settings")
        keyLayout = QFormLayout()
        keyBox.setLayout(keyLayout)
        
        keyHeight = QSpinBox()
        keyHeight.setValue(1)
        
        keytopThickness = QSpinBox()
        keytopThickness.setValue(1)
        
        wallThickness = QSpinBox()
        wallThickness.setValue(3)
        
        cornerRadius = QSpinBox()
        cornerRadius.setValue(1)
        
        bottomWidth = QDoubleSpinBox()
        bottomWidth.setValue(18.16)
        
        bottomHeight = QDoubleSpinBox()
        bottomHeight.setValue(18.16)
        
        widthDiff = QSpinBox()
        widthDiff.setValue(6)
        
        heightDiff = QSpinBox()
        heightDiff.setValue(4)
        
        totalDepth = QDoubleSpinBox()
        totalDepth.setValue(11.5)
        
        topTilt = QSpinBox()
        topTilt.setValue(-6)
        
        topTiltY = QSpinBox()
        topTiltY.setValue(0)
        topTiltY.setRange(-1000, 1000)
        
        topSkew = QDoubleSpinBox()
        topSkew.setValue(1.7)
        
        topSkewX = QSpinBox()
        topSkewX.setValue(0)
        topSkewX.setRange(-1000, 1000)
        
        keyLayout.addRow(QLabel("Key Height"), keyHeight)
        keyLayout.addRow(QLabel("Keytop Thickness"), keytopThickness)
        keyLayout.addRow(QLabel("Wall Thickness"), wallThickness)
        keyLayout.addRow(QLabel("Corner Radius"), cornerRadius)
        keyLayout.addRow(QLabel("Bottom Key Width"), bottomWidth)
        keyLayout.addRow(QLabel("Bottom Key Height"), bottomHeight)
        keyLayout.addRow(QLabel("Width Difference"), widthDiff)
        keyLayout.addRow(QLabel("Height Difference"), heightDiff)
        keyLayout.addRow(QLabel("Total Depth"), totalDepth)
        keyLayout.addRow(QLabel("Top Tilt"), topTilt)
        keyLayout.addRow(QLabel("Top Tilt Y"), topTiltY)
        keyLayout.addRow(QLabel("Top Skew"), topSkew)
        keyLayout.addRow(QLabel("Top Skew X"), topSkewX)
        
        return keyBox
    def stemSettings(self):
        # Stem Settings
        stemBox = QGroupBox("Stem Settings")
        stemLayout = QFormLayout()
        stemBox.setLayout(stemLayout)
        
        stemThrow = QSpinBox()
        stemThrow.setValue(4)
        roundedCherryStem = QDoubleSpinBox()
        roundedCherryStem.setValue(5.5)
        stemInset = QSpinBox()
        stemInset.setValue(0)
        stemInset.setRange(-999, 999)
        stemRotation = QSpinBox()
        stemRotation.setValue(0)
        stemRotation.setRange(-360, 360)
        extraLongStem = QCheckBox()
        
        stemLayout.addRow(QLabel("Stem Throw"), stemThrow)
        stemLayout.addRow(QLabel("Rounded Cherry Stem"), roundedCherryStem)
        stemLayout.addRow(QLabel("Stem Inset"), stemInset)
        stemLayout.addRow(QLabel("Stem Rotation"), stemRotation)
        stemLayout.addRow(QLabel("Extra Long Stem Support"), extraLongStem)
        
        return stemBox
    def shapeSettings(self):
        # Shape Settings
        shapeBox = QGroupBox("Shape Settings")
        shapeLayout = QFormLayout()
        shapeBox.setLayout(shapeLayout)
        
        keyShapeType = QLineEdit("rounded_square")
        linearExtrude = QSpinBox()
        linearExtrude.setRange(-999, 999)
        linearExtrude.setValue(0)
        heightSlices = QSpinBox()
        heightSlices.setValue(1)
        
        shapeLayout.addRow(QLabel("Key Shape Type"), keyShapeType)
        shapeLayout.addRow(QLabel("Linear Extrude Height Adjustment"), linearExtrude)
        shapeLayout.addRow(QLabel("Height Slices"), heightSlices)
        
        return shapeBox
    def dishSettings(self):
        # Dish Settings
        dishBox = QGroupBox("Dish Settings")
        dishLayout = QFormLayout()
        dishBox.setLayout(dishLayout)
        types = ["cylindrical", "spherical", "sideways cylindrical", 
                 "old spherical", "disabled"]
        
        dishTypes = QComboBox()
        dishTypes.addItems(types)
        
        depth = QSpinBox()
        depth.setValue(1)
        
        skewX = QSpinBox()
        skewX.setValue(0)
        skewX.setRange(-999, 999)
        
        skewY = QSpinBox()
        skewY.setValue(0)
        skewY.setRange(-999, 999)
        
        overdrawnWidth = QSpinBox()
        overdrawnWidth.setValue(0)
        overdrawnWidth.setRange(-999, 999)
        
        overdrawnHeight = QSpinBox()
        overdrawnHeight.setValue(0)
        overdrawnHeight.setRange(-999, 999)
        
        dishLayout.addRow(QLabel("Dish Type"), dishTypes)
        dishLayout.addRow(QLabel("Dish Depth"),depth )
        dishLayout.addRow(QLabel("Dish Skew X"), skewX)
        dishLayout.addRow(QLabel("Dish Skew Y"), skewY)
        dishLayout.addRow(QLabel("Dish Overdraw Width"), overdrawnWidth)
        dishLayout.addRow(QLabel("Dish Overdraw Deight"), overdrawnHeight)
        
        return dishBox
    def miscSettings(self):
        # Misc Settings
        dishBox = QGroupBox("Dish Settings")
        dishLayout = QFormLayout()
        dishBox.setLayout(dishLayout)
        
        cherryBevel = QCheckBox()
        cherryBevel.setCheckState(Qt.Checked)

        stemSupportHeight = QDoubleSpinBox()
        stemSupportHeight.setValue(0.8)
        
        font = QLineEdit("DejaVu Sans Mono:style=Book")
        
        clearanceCheck = QCheckBox()
        linearExtrude = QCheckBox()
        skinExtrude = QCheckBox()
        roundedKey = QCheckBox()
        
        minkowskiRadius = QDoubleSpinBox()
        minkowskiRadius.setValue(0.33)
        minkowskiRadius.setSingleStep(0.01)
        
        dishLayout.addRow(QLabel("Cherry Bevel"), cherryBevel)
        dishLayout.addRow(QLabel("Stem Support Height"), stemSupportHeight)
        dishLayout.addRow(QLabel("Font"), font)
        dishLayout.addRow(QLabel("Clearance Check"), clearanceCheck)
        dishLayout.addRow(QLabel("Linear Extrude Shape"), linearExtrude)
        dishLayout.addRow(QLabel("Skin Extrude Shape"), skinExtrude)
        dishLayout.addRow(QLabel("Rounded Key"), roundedKey)
        dishLayout.addRow(QLabel("Minkowski Radius"), minkowskiRadius)
    def features(self):
        # Features
        featuresBox = QGroupBox("Features")
        featuresLayout = QFormLayout()
        featuresBox.setLayout(featuresLayout)
        
        keyBump = QCheckBox()
        keyBumpDepth = QDoubleSpinBox()
        keyBumpDepth.setValue(0.5)
        keyBumpEdge = QDoubleSpinBox()
        keyBumpEdge.setValue(0.4)
        
        featuresLayout.addRow(QLabel("Key Bump"), keyBump)
        featuresLayout.addRow(QLabel("Key Bump Depth"), keyBumpDepth)
        featuresLayout.addRow(QLabel("Key Bump Edge"), keyBumpEdge)
        
        return featuresBox
    def parser(self, data):
        vars = {}
app = QApplication([])
window = Window()
window.show()
app.exec()
