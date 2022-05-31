# importing libraries
from lib2to3.pgen2.literals import evalString
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math

  
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("   Calculator")
  
        # setting geometry
        #self.setGeometry(100, 100, 360, 350)

        self.setFixedSize(400, 630)

        # setting window icon
        self.setWindowIcon(QIcon("logo.png"))

  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
        # method for widgets
    def UiComponents(self):
  
        # creating a label
        self.label = QLabel(self)
        # setting geometry to the label

        self.label.setGeometry(2, 175, 350, 100)

        

        # creating label multi line
        self.label.setWordWrap(False)

       
    

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 2px grey;"
                                 "background-color: rgb(240, 240, 240);"
                                 "}"
                                )

  
        # setting alignment to the label
        self.label.setAlignment(Qt.AlignRight)

        #self.label.adjustSize()    

        # setting font
        self.label.setFont(QFont('serif', 27))


        push_clear = QPushButton(" C ", self)
        push_clear.setGeometry(7, 240, 90, 60)
        push_clear.setFont(QFont('Calibri', 16))
        push_clear.setStyleSheet("background-color : rgb(64, 64, 64); border-radius : 10; color: white;")

        
        push_open = QPushButton("(", self)
        push_open.setGeometry(104, 240, 90, 60)
        push_open.setFont(QFont('Calibri', 15))

        push_close = QPushButton(")", self)
        push_close.setGeometry(201, 240, 90, 60)
        push_close.setFont(QFont('Calibri', 15))

         # del one character button
        push_del = QPushButton(" ⊗ ", self)
        push_del.setGeometry(298, 240, 90, 60)
        push_del.setFont(QFont('Calibri', 30))
        push_del.setStyleSheet("background-color : rgb(64, 64, 64); border-radius : 10; color: white;")

  
        push_negate = QPushButton("±", self)
        push_negate.setGeometry(7, 305, 90, 60)
        push_negate.setFont(QFont('Italic', 15))

        push_sqr = QPushButton("x²", self)
        push_sqr.setGeometry(104, 305, 90, 60)
        push_sqr.setFont(QFont('Book Antiqua', 15))

        # creating push button
        push_div = QPushButton("÷", self)
        # setting geometry
        push_div.setGeometry(298, 305, 90, 60)
        push_div.setFont(QFont('Georgia', 17))

         # creating a push button
        push_root = QPushButton("√", self)
        push_root.setGeometry(201, 305, 90, 60)
        push_root.setFont(QFont('Georgia', 15))

         # adding number button to the screen
        # creating a push button
        push7 = QPushButton("7", self)
        # setting geometry
        push7.setGeometry(7, 370, 90, 60)
        push7.setFont(QFont('Calibri', 15))


        # creating a push button
        push8 = QPushButton("8", self)
        # setting geometry
        push8.setGeometry(104, 370, 90, 60)
        push8.setFont(QFont('Calibri', 15))


        # creating a push button
        push9 = QPushButton("9", self)
        # setting geometry
        push9.setGeometry(201, 370, 90, 60)
        push9.setFont(QFont('Calibri', 15))


        # creating push button
        push_mul = QPushButton("×", self)
        # setting geometry
        push_mul.setGeometry(298, 370, 90, 60)
        push_mul.setFont(QFont('Calibri', 15))


        # creating a push button
        push4 = QPushButton("4", self)
        # setting geometry
        push4.setGeometry(7, 435, 90, 60)
        push4.setFont(QFont('Calibri', 15))

  
        # creating a push button
        push5 = QPushButton("5", self)
        # setting geometry
        push5.setGeometry(104, 435, 90, 60)
        push5.setFont(QFont('Calibri', 15))


        # creating a push button
        push6 = QPushButton("6", self)
        # setting geometry
        push6.setGeometry(201, 435, 90, 60)
        push6.setFont(QFont('Calibri', 15))


        # creating push button
        push_minus = QPushButton("–", self)
        # setting geometry
        push_minus.setGeometry(298, 435, 90, 60)
        push_minus.setFont(QFont('Calibri', 15))

        # creating a push button
        push1 = QPushButton("1", self)
        # setting geometry
        push1.setGeometry(7, 500, 90, 60)
        push1.setFont(QFont('Calibri', 15))
  
        # creating a push button
        push2 = QPushButton("2", self)
        # setting geometry
        push2.setGeometry(104, 500, 90, 60)
        push2.setFont(QFont('Calibri', 15))
  
        # creating a push button
        push3 = QPushButton("3", self)
        push3.setGeometry(201, 500, 90, 60)
        push3.setFont(QFont('Calibri', 15))

        # creating push button
        push_plus = QPushButton("+", self)
        # setting geometry
        push_plus.setGeometry(298, 500, 90, 60)
        push_plus.setFont(QFont('Calibri', 15))

        # creating a push button
        push0 = QPushButton("0", self)
        push0.setGeometry(7, 565, 90, 60)
        push0.setFont(QFont('Calibri', 15))

        # creating push button
        push_00 = QPushButton("00", self)
        push_00.setGeometry(104, 565, 90, 60)
        push_00.setFont(QFont('Calibri', 15))

        # creating push button
        push_point = QPushButton(".", self)
        push_point.setGeometry(201, 565, 90, 60)
        push_point.setFont(QFont('Calibri', 15))
    

        # creating push button
        push_equal = QPushButton("=", self)
        push_equal.setStyleSheet("background-color : rgb(64, 64, 64); border-radius : 12; color: white;")
        # setting geometry
        push_equal.setGeometry(298, 565, 90, 60)
        push_equal.setFont(QFont('Helvetica', 25))

  
        # adding action to each of the button
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)
        push_00.clicked.connect(self.action_00)
        push_root.clicked.connect(self.action_root)
        push_negate.clicked.connect(self.action_negate)
        push_sqr.clicked.connect(self.action_sqr)
        push_close.clicked.connect(self.action_close)
        push_open.clicked.connect(self.action_open)



    def action_equal(self):
        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            ans = eval(equation)
            anss = str(ans)

            # setting text to the label
            tn = (len(anss))
            a = int(tn) - 13
            x = anss[:-a]
            X = str(x)

            if a <= 0:
                self.label.setText(anss)
            else:
                self.label.setText(X)
            

        except:
            self.label.setText("Inp")

            
            
    def action_open(self):
        text = self.label.text()
        self.label.setText(text + "(")

    def action_negate(self):
        text = self.label.text()
        self.label.setText("-" + text)

    def action_close(self):
        text = self.label.text()
        self.label.setText(text + ")")

    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "+")
  
    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "-")

    def action_sqr(self):
        text = self.label.text()
        text1 = str(int((float(text)*float(text))))
        self.label.setText(text1)
  
    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "/")

  
    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "*")
  
    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")
  
    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")
  
    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")
  
    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")
  
    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")
  
    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")
  
    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")
  
    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")
  
    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")
  
    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")
  
    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")
  
    def action_clear(self):
        # clearing the label text
        self.label.setText("")
  
    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])

    def action_00(self):
        text = self.label.text()
        self.label.setText(text + "00")

    def action_root(self):
        text = self.label.text()
        self.label.setText("math.sqrt(" + text +")")

        
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
