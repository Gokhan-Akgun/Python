import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1080, 640)
        self.setWindowTitle("Pyqt5 App")

        self.button()
        self.label()
        self.entry()
        self.messageBox()
        self.font()
        self.show()


    def button(self):
        button = QPushButton("Hello World", self)
        button.setToolTip("Whis is a hello world button")
        button.resize(100, 50)
        button.move(50, 50)
        button.clicked.connect(self.buttonFunction)

    def buttonFunction(self):
        print("Hello world")

    def label(self):
        text1 = QLabel("Hello", self)
        self.text2 = QLabel("Word", self)

        # geometry manager
        text1.move(170, 50)
        self.text2.move(170, 70)

        button1 = QPushButton("Change", self)
        button1.move(170, 100)
        button1.clicked.connect(self.button1Function)

    def button1Function(self):
        self.text2.setText("Hello World")
        self.text2.resize(200, 25)
        self.text2.setFont(QFont("Arial", 25, QFont.Bold))

    def entry(self):
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Place holder")
        self.textbox.move(300, 50)

        button2 = QPushButton("Save", self)
        button2.move(300, 75)
        button2.clicked.connect(self.saveFunction)

    def saveFunction(self):
        txt = self.textbox.text()
        if txt != "":
            print(txt)
        else:
            print("Empty !!")

    def messageBox(self):
        button3 = QPushButton("message", self)
        button3.move(500, 50)
        button3.clicked.connect(self.messageFunction)

        button4 = QPushButton("message2", self)
        button4.move(500, 75)
        button4.clicked.connect(self.messageFunction2)

        button5 = QPushButton("message3", self)
        button5.move(500, 100)
        button5.clicked.connect(self.messageFunction3)

    def messageFunction(self):
        m_box = QMessageBox.question(self, "Question", "Did you enjoy the course ?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if m_box == QMessageBox.Yes:
            print("yes")
        elif m_box == QMessageBox.No:
            print("No")
        else:
            print("cancel")

    def messageFunction2(self):
        m_box = QMessageBox.information(self, "Information", "Enjoy your course")

    def messageFunction3(self):
        m_box2 = QMessageBox.warning(self, "Warning", "Enjoy the course !!")

    def font(self):
        self.label = QLabel("Font Like This", self)
        self.label.move(700, 100)

        button6 = QPushButton("Font", self)
        button6.move(700, 50)
        button6.clicked.connect(self.setFont)

    def setFont(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.label.setFont(font)
            self.label.resize(500,200)








app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())