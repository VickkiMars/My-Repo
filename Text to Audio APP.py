import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import speech_recognition as sr
import pyttsx3

class Window(QWidget):
    def __init__(self, parent= None):
        super(Window, self).__init__(parent)
        
        layout = QFormLayout()
        
        self.s = QPushButton("Speak Text")
        self.s.clicked.connect(self.SpeakText)
        
        self.entertext = QLabel("Enter text:  ")
        self.TXT = QLineEdit(self)
        
        layout.addRow(self.entertext, self.TXT)
        layout.addWidget(self.s)
        
        self.setLayout(layout)
        self.setWindowTitle("Speech to Text App")
        self.setFixedSize(400, 100)
        self.setWindowIcon(QIcon("download.png"))
        
        
        r = sr.Recognizer()
    
    def SpeakText(self):
        engine = pyttsx3.init()
        engine. setProperty("rate", 178)
        engine.say(self.TXT.text())
        engine.runAndWait()
        #x = SpeakText(self.TXT.text())
    
def main(): 
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()