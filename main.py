from _ast import Lambda
import PyQt5.QtWidgets as qtw
class MainWindow(qtw.QWidget): #where the widgets are added
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.tnum = []
        self.fnum = []

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.result_field = qtw.QLineEdit()
        result = qtw.QPushButton('Enter', clicked = self.resultf)
        clear = qtw.QPushButton('AC',clicked = self.clearf)
        b9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))
        b8 = qtw.QPushButton('8',clicked=lambda: self.num_press('8'))
        b7 = qtw.QPushButton('7',clicked=lambda: self.num_press('7'))
        b6 = qtw.QPushButton('6',clicked=lambda: self.num_press('6'))
        b5 = qtw.QPushButton('5',clicked=lambda: self.num_press('5'))
        b4 = qtw.QPushButton('4',clicked=lambda: self.num_press('4'))
        b3 = qtw.QPushButton('3',clicked=lambda: self.num_press('3'))
        b2 = qtw.QPushButton('2',clicked=lambda: self.num_press('2'))
        b1 = qtw.QPushButton('1',clicked=lambda: self.num_press('1'))
        b0 = qtw.QPushButton('0',clicked=lambda: self.num_press('0'))
        plus = qtw.QPushButton('+',clicked=lambda: self.func_press('+'))
        mins = qtw.QPushButton('-',clicked=lambda: self.func_press('-'))
        mult = qtw.QPushButton('*',clicked=lambda: self.func_press('*'))
        div = qtw.QPushButton('/',clicked=lambda: self.func_press('/'))

        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(result, 1, 0, 1, 2)
        container.layout().addWidget(clear, 1, 2, 1, 2)
        container.layout().addWidget(b9, 2, 0)
        container.layout().addWidget(b8, 2, 1)
        container.layout().addWidget(b7, 2, 2)
        container.layout().addWidget(b6, 3, 0)
        container.layout().addWidget(b5, 3, 1)
        container.layout().addWidget(b4, 3, 2)
        container.layout().addWidget(b3, 4, 0)
        container.layout().addWidget(b2, 4, 1)
        container.layout().addWidget(b1, 4, 2)
        container.layout().addWidget(b0,5,0,1,3)
        container.layout().addWidget(plus, 2,3)
        container.layout().addWidget(mins, 3, 3)
        container.layout().addWidget(mult, 4, 3)
        container.layout().addWidget(div, 5, 3)
        self.layout().addWidget(container)

    def num_press(self,key):
        self.tnum.append(key)
        tstring = ''.join(self.tnum)
        if self.fnum:
            self.result_field.setText(''.join(self.fnum)+tstring)
        else:
            self.result_field.setText(tstring)

    def func_press(self,operator):
        tstring = ''.join(self.tnum)
        self.fnum.append(tstring)
        self.fnum.append(operator)
        self.tnum = []
        self.result_field.setText(''.join(self.fnum))
    def resultf(self):
        fstring = ''.join(self.fnum)+''.join(self.tnum)
        rstring = eval(fstring)
        fstring += '='
        fstring += str(rstring)
        self.result_field.setText(fstring)
    def clearf(self):
        self.result_field.clear()
        self.tnum = []
        self.fnum = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
