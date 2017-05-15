import sys
import random
from PyQt4 import QtGui, QtCore
from graph import Grapher

class Widget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.x = [0]
        self.rand_list = []
        self.initUI()

    def initUI(self):

        # Combo Box
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("Reno")
        self.combo.addItem("Tahoe")
        self.combo.addItem("New Reno")
        # line editors
        self.cwnd_box = QtGui.QLineEdit(self)
        self.cwnd_box.resize(10, 10)
        self.ssth_box = QtGui.QLineEdit(self)
        self.ssth_box.resize(10, 10)
        self.l4_box = QtGui.QLineEdit(self)
        self.l4_box.resize(30, 10)
        self.l5_box = QtGui.QLineEdit(self)
        self.l5_box.resize(30, 10)
        self.l6_box = QtGui.QLineEdit(self)
        self.l6_box.resize(30, 10)
        self.l7_box = QtGui.QLineEdit(self)
        self.l7_box.resize(30, 10)
        # Labels
        self.l1 = QtGui.QLabel("TCP", self)
        t_l2 = QtGui.QLabel("CONGESTION", self)
        t_l3 = QtGui.QLabel("CONTROL", self)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        l2 = QtGui.QLabel("Window Sizes", self)
        l2.setAlignment(QtCore.Qt.AlignRight)
        l3 = QtGui.QLabel("TIMERS", self)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l4 = QtGui.QLabel("RTO    :", self)
        l5 = QtGui.QLabel("RTT    :", self)
        l6 = QtGui.QLabel("Max congestion (packets/sec) :", self)
        l7 = QtGui.QLabel("Simulation Time :", self)
        # fonts initialization
        # 1
        title_font = QtGui.QFont("Times")
        title_font.setBold(True)
        title_font.setItalic(True)
        title_font.setPixelSize(20)
        # 2
        bold_font = QtGui.QFont()
        bold_font.setPixelSize(15)
        bold_font.setBold(True)
        bold_font.setUnderline(True)
        # label font setup
        self.l1.setFont(title_font)
        t_l2.setFont(title_font)
        t_l3.setFont(title_font)
        l2.setFont(bold_font)
        l3.setFont(bold_font)
        # Buttons
        sim_btn = QtGui.QPushButton("SIMULATE", self)
        cwnd_btn = QtGui.QPushButton("Enter CWND", self)
        ssthresh_btn = QtGui.QPushButton("Enter ssthresh", self)
        b4 = QtGui.QPushButton("Enter", self)
        b5 = QtGui.QPushButton("Enter", self)
        b6 = QtGui.QPushButton("Enter", self)
        b7 = QtGui.QPushButton("Enter", self)
        # grid layout
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        # grid setup
        grid.addWidget(self.l1, 0, 2)
        grid.addWidget(t_l2, 0, 3)
        grid.addWidget(t_l3, 0, 4)
        grid.addWidget(l2, 1, 0)
        grid.addWidget(self.combo, 2, 0)
        grid.addWidget(self.cwnd_box, 5, 0)
        grid.addWidget(self.ssth_box, 4, 0)
        grid.addWidget(cwnd_btn, 5, 1)
        grid.addWidget(ssthresh_btn, 4, 1)
        grid.addWidget(sim_btn, 8, 1, 1, 3)
        grid.addWidget(l3, 2, 3)
        grid.addWidget(l4, 4, 3)
        grid.addWidget(self.l4_box, 4, 4)
        grid.addWidget(b4, 4, 5)
        grid.addWidget(l5, 5, 3)
        grid.addWidget(self.l5_box, 5, 4)
        grid.addWidget(b5, 5, 5)
        grid.addWidget(l6, 6, 3)
        grid.addWidget(self.l6_box, 6, 4)
        grid.addWidget(b6, 6, 5)
        grid.addWidget(l7, 7, 3)
        grid.addWidget(self.l7_box, 7, 4)
        grid.addWidget(b7, 7, 5)

        self.setLayout(grid)
        self.setWindowTitle('CN Project')
        # timers
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.sim_handler())
        self.timer.start(100)

        # signals and slots
        sim_btn.clicked.connect(self.sim_click)
        cwnd_btn.clicked.connect(self.b1_click)
        ssthresh_btn.clicked.connect(self.b2_click)
        b4.clicked.connect(self.b4_click)
        b5.clicked.connect(self.b5_click)
        b6.clicked.connect(self.b6_click)
        b7.clicked.connect(self.b7_click)

    def b1_click(self):
        self.var_1 = self.cwnd_box.text()
        print(self.var_1)
        try:
            self.var_1 = int(self.var_1)

        except ValueError:
            self.var_1 = 0.01
            self.error_handler_1()

    def error_handler_1(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Enter the numeric values!")
        msg.setWindowTitle("Value Error")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        retval = msg.exec()
        print (retval)

    def b2_click(self):
        self.var_2 = self.ssth_box.text()

        try:
            self.var_2 = int(self.var_2)

        except ValueError:
            self.var_2 = 0.01
            self.error_handler_1()

    def b4_click(self):
        self.var_4 = self.l4_box.text()

        try:
            self.var_1 = int(self.var_4)

        except ValueError:
            self.var_4 = 0.01
            self.error_handler_1()

    def b5_click(self):
        self.var_5 = self.l5_box.text()

        try:
            self.var_5 = int(self.var_5)

        except ValueError:
            self.var_5 = 0.01
            self.error_handler_1()

    def b6_click(self):
        self.var_6 = self.l6_box.text()

        try:
            self.var_6 = int(self.var_6)

        except ValueError:
            self.var_6 = 0.01
            self.error_handler_1()

    def b7_click(self):

        self.var_7 = self.l7_box.text()

        try:
            self.var_7 = int(self.var_7)

        except ValueError:
            self.var_7 = 0.01
            self.error_handler_1()

    def sim_handler(self):

        self.rand_list.append(random.randint(1,7))
        self.x.append(self.x[len(self.x)-1]+1)

    def sim_click(self):
        text = str(self.combo.currentText())
        if text == "Tahoe":
            file = open("output.txt", 'r')
            result = file.read().split('\n')
            x = []
            result1 = []
            count = 0
            result.pop()
            for (i, y) in enumerate(result):
                result1.append(int(y))
                count+=1
                x.append(count)
            result = result1
            print(len(x))
            print(len(result))
        if text == "Reno":
            file = open("output1.txt", 'r')
            result = file.read().split('\n')
            x = []
            result1 = []
            count = 0
            result.pop()
            for (i, y) in enumerate(result):
                result1.append(int(y))
                count+=1
                x.append(count)
            result = result1
            print(len(x))
            print(len(result))
        if text == "New Reno":
            file = open("output2.txt", 'r')
            result = file.read().split('\n')
            x = []
            result1 = []
            count = 0
            result.pop()
            for (i, y) in enumerate(result):
                result1.append(int(y))
                count+=1
                x.append(count)
            result = result1
            print(len(x))
            print(len(result))
        Grapher.gen(self, result, x)

# ---------------------------------------------------------- #