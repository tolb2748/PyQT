'''
Created on Dec 8, 2018

@author: Brandon
'''
from PyQt5.Qt import QMainWindow, QPushButton

from OpeningOtherWindows.SecondWindow import Second


class First(QMainWindow):
    '''Main Window'''
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton("click me")

        self.setCentralWidget(self.pushButton)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)


    def on_pushButton_clicked(self):
        ''' Opens the second window'''
        self.dialog = Second();
        self.dialog.show()