import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt


class Window1(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 800, 150)
        self.setWindowTitle("Pyqt5 App_1")
        self.radioButton()
        self.comboBox()
        self.checkBox()
        self.progresBar()
        self.show()

    def radioButton(self):
        self.method1 = QRadioButton("method1", self)
        self.method2 = QRadioButton("method2", self)
        self.method3 = QRadioButton("method3", self)

        self.method1.move(50, 40)
        self.method2.move(50, 60)
        self.method3.move(50, 80)

        self.method1.setChecked(True)

        button = QPushButton("Radio Button", self)
        button.move(50,100)
        button.clicked.connect(self.window_page)

    def window_page(self):
        if self.method1.isChecked():
            print("method 1")

        elif self.method2.isChecked():
            pass

        elif self.method3.isChecked():
            print("method 3")

        else:
            print("Empty")

    def comboBox(self):
        self.combo = QComboBox(self)
        self.combo.move(150,40)
        self.combo.addItem("one")
        self.combo.addItem("two")
        self.combo.addItem("three")

        button = QPushButton("Combo Button", self)
        button.move(150, 80)
        button.clicked.connect(self.comboFunction)

    def comboFunction(self):
        print(self.combo.currentText())

    def checkBox(self):
        self.save = QCheckBox("save", self)
        self.save.move(250,40)

        button = QPushButton("Save", self)
        button.move(250, 60)
        button.clicked.connect(self.saveall)

    def saveall(self):
        if self.save.isChecked():
            print("save !!!")
        else:
            print("not save")

    def progresBar(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(400,20,200,25)
        self.pbar.setValue(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(500)

    def handleTimer(self):
        value = self.pbar.value()
        step = 1
        if value < 100:
            value = value + step
            self.pbar.setValue(value)
        elif value == 100:
            self.pbar.setValue(0)
        else:
            self.timer.stop()




app = QApplication(sys.argv)
window1 = Window1()
sys.exit(app.exec_())