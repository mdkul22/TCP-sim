import sys
from PyQt4 import QtGui, QtCore
from cw import Widget

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        #
        self.timer_list = [0, 0, 0, 0]
        cwnd = 0

        # adding action to file menu
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        resetAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Reset', self)
        resetAction.setShortcut('Ctrl+R')
        resetAction.setStatusTip('Reset Test')
        resetAction.triggered.connect(self.reset_test)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(resetAction)

        self.widget1 = Widget()
        self.setCentralWidget(self.widget1)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("TCP mini-simulator 1.0")
        self.show()

    def reset_test(self):
        print("hello")

def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
