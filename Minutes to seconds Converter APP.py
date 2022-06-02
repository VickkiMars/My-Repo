import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tqdm.notebook import tqdm_notebook



class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        
        layout = QFormLayout()
        
        self.c = QPushButton("Close Converter")
        self.c.clicked.connect(self.close)
        
        
        
        self.l1 = QLabel("Enter the time in Hours:  (_if none please input 0_)  ")
        self.nm = QLineEdit(self)
        self.nm.setText('0')
        layout.addRow(self.l1, self.nm)
        
        self.l2 = QLabel("Enter the time in Minutes:  (_if none please input 0_)  ")
        self.n2 = QLineEdit(self)
        self.n2.setText('0')
        layout.addRow(self.l2, self.n2)
        
        
        self.convert = QPushButton("Convert")
        self.convert.clicked.connect(self.convert_minutes_to_seconds)
        self.answer = QLabel(self)
        layout.addRow(self.convert, self.answer)
        layout.addWidget(self.c)
        
        self.setLayout(layout)
        self.setWindowTitle("Minutes to seconds Converter")
        self.setWindowIcon(QIcon("logoo.png"))
        
    def close(self):
        
    
    def convert_minutes_to_seconds(self):
        
        take_input_hours =   float(self.nm.text())#int(input("(IF THERE ISN'T ANY, ENTER '0') Time in hours >>> "))
        take_input_minutes =  float(self.n2.text()) #int(input('Time in minutes >>> '))
        
        #TIH = int(take_input_hours)
        #TIM = int(take_input_minutes)
        
        TIH = int(take_input_hours)
        TIM = int(take_input_minutes)
        
        tim = str(take_input_minutes)
        tih = str(take_input_hours)
        
        #mts = minutes to seconds
        htm = (TIH*60)
        mts_for_hours = (htm*60)
        mts_for_minutes = (TIM*60)
        
        #a is the result gotten from converting input entered in hours to minutes
        a = htm + TIM
        A = str(a)
        
       
        
        #MTS - total minutes to seconds
        MTS = mts_for_hours + mts_for_minutes
        
        s = str(MTS)
        x = 'There are ' + s + ' seconds in ' + tim + ' minutes' 
        y = 'There are ' + s + ' seconds in ' + tih + ' hour'
        z = 'There are ' + s + ' seconds in ' + tih + ' hours, ' + tim + 'minutes'
        #elif should have been used here but for its complexity
        #this code is written with a novice in mind
        
        if (tih == '1') and (tim == '0'):
            self.answer.setText(y)
        else:
            pass
        
        if (tih > '1') and (tim == '0'):
            self.answer.setText('There are ' + s + ' seconds in ' + tih + ' hours')
        
        if ((tih != '0') and (tim != '0')):
            self.answer.setText(z)
        else:
            pass
        
        if ((tih < '0') and (tim < '0')):
            self.answer.setText('Input Error')
        else:
            pass
        
        if ((tih == '0') and (tim > '1')):
            self.answer.setText(x)
        else:
            pass
            
        if ((tih =='0') and (tim <= '0')):
            self.answer.setText('There are ' + s + ' seconds in ' + tim + ' Minute')
        else:
            pass
    
        if (tih == '0') and (tim == '0'):
            self.answer.setText('Please enter a Number ✌️')
        else:
            pass
        
        if tim == '1':
            self.answer.setText('There are 60 seconds in one minute..... Take Note!!')
        else:
            pass

    
def main(): 
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
