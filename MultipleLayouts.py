'''
Created on Dec 14, 2018

@author: Brandon
'''
import sys

from PyQt5.Qt import QWidget, QPushButton, QVBoxLayout, QApplication,\
    QHBoxLayout


class PrettyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUi()
        
    def initUi(self):
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Combo Box Layout')
        
        button1 = QPushButton('Button1', self)
        button2 = QPushButton('Button2', self)
        
        button3 = QPushButton('Button3', self)
        button4 = QPushButton('Button4', self)
        
        v1 = QVBoxLayout()
        v1.addWidget(button1)
        v1.addWidget(button2)
        
        v2 = QVBoxLayout()
        v2.addWidget(button3)
        v2.addWidget(button4)
        
        
        hbox = QHBoxLayout()
        hbox.addLayout(v1)
        hbox.addLayout(v2)
        
        self.setLayout(hbox)
        
        
def main():
    app = QApplication(sys.argv)
    window = PrettyWidget()
    window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
        