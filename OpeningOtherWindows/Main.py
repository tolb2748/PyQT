'''
Created on Dec 8, 2018

@author: Brandon
'''
import sys

from PyQt5.Qt import QApplication

from OpeningOtherWindows.MainWindow import First


def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()