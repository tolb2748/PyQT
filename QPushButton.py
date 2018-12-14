'''
Created on Dec 13, 2018

@author: Brandon
'''
import sys

from PyQt5.Qt import  QWidget, QApplication, QPushButton


class PrettyWidget(QWidget):
    
    def __init__(self):
        super().__init__();
        self.initUi();      ##Function
        
    def initUi(self):
        self.setGeometry(600,300,400,200)
        self.setWindowTitle('Absolute Positioning')
        
        #QPushButton
        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(150,100)
        
       
        
def main():
    app = QApplication(sys.argv)
    window = PrettyWidget()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main();
    