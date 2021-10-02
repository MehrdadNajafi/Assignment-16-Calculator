import math

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

def int_or_float(num):
    a = float(num)
    b = int(num)
    if a != b:
        return a
    else:
        return b

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()
        
        self.ui.btn_1.clicked.connect(self.btn_1)
        self.ui.btn_2.clicked.connect(self.btn_2)
        self.ui.btn_3.clicked.connect(self.btn_3)
        self.ui.btn_4.clicked.connect(self.btn_4)
        self.ui.btn_5.clicked.connect(self.btn_5)
        self.ui.btn_6.clicked.connect(self.btn_6)
        self.ui.btn_7.clicked.connect(self.btn_7)
        self.ui.btn_8.clicked.connect(self.btn_8)
        self.ui.btn_9.clicked.connect(self.btn_9)
        self.ui.btn_0.clicked.connect(self.btn_0)

        self.ui.btn_clear.clicked.connect(self.btn_clear)
        self.ui.btn_equal.clicked.connect(self.btn_equal)
        self.ui.btn_point.clicked.connect(self.btn_point)

        self.ui.btn_sum.clicked.connect(self.btn_sum)
        self.ui.btn_minus.clicked.connect(self.btn_minus)
        self.ui.btn_multi.clicked.connect(self.btn_multi)
        self.ui.btn_div.clicked.connect(self.btn_div)
        self.ui.btn_symmetry.clicked.connect(self.btn_symmetry)
        self.ui.btn_percent.clicked.connect(self.percent)
        self.ui.btn_sin.clicked.connect(self.btn_sin)
        self.ui.btn_cos.clicked.connect(self.btn_cos)
        self.ui.btn_tan.clicked.connect(self.btn_tan)
        self.ui.btn_cot.clicked.connect(self.btn_cot)
        self.ui.btn_sqrt.clicked.connect(self.btn_sqrt)
        self.ui.btn_log.clicked.connect(self.btn_log)


        self.num_list = []

        self.flag_for_sum = False
        self.flag_for_minus = False
        self.flag_for_multi = False
        self.flag_for_div = False

    def btn_sum(self):
        num = float(self.ui.textbox.text())
        self.num_list.append(num)
        self.ui.textbox.setText('')
        self.flag_for_sum = True

    def btn_minus(self):
        num = float(self.ui.textbox.text())
        self.num_list.append(num)
        self.ui.textbox.setText('')
        self.flag_for_minus = True

    def btn_multi(self):
        num = float(self.ui.textbox.text())
        self.num_list.append(num)
        self.ui.textbox.setText('')
        self.flag_for_multi = True

    def btn_div(self):
        num = float(self.ui.textbox.text())
        self.num_list.append(num)
        self.ui.textbox.setText('')
        self.flag_for_div = True

    def btn_symmetry(self):
        num = -float(self.ui.textbox.text())
        num = int_or_float(num)
        self.ui.textbox.setText(str(num))

    def percent(self):
        num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(int_or_float(num / 100)))

    def btn_sin(self):
        num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(int_or_float(math.sin(math.radians(num)))))

    def btn_cos(self):
        num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(int_or_float(math.cos(math.radians(num)))))

    def btn_tan(self):
        num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(int_or_float(math.tan(math.radians(num)))))

    def btn_cot(self):
        num = float(self.ui.textbox.text())
        sin = math.sin(math.radians(num))
        cos = math.cos(math.radians(num))
        try:
            cot = cos / sin
        except:
            cot = 'Cannot divide by zero'
        self.ui.textbox.setText(str(int_or_float(cot)))

    def btn_sqrt(self):
        num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(int_or_float(math.sqrt(num))))

    def btn_log(self):
        num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(int_or_float(math.log(num))))

    def btn_point(self):
        num = self.ui.textbox.text()
        for word in num:
            if word == '.':
                break
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '.')

    def btn_equal(self):
        if self.flag_for_minus:
            num = -float(self.ui.textbox.text())
            self.num_list.append(num)
            result = sum(self.num_list)
            self.flag_for_minus = False

        elif self.flag_for_sum:
            num = float(self.ui.textbox.text())
            self.num_list.append(num)
            result = sum(self.num_list)
            self.flag_for_sum = False

        elif self.flag_for_multi:
            num = float(self.ui.textbox.text())
            self.num_list.append(num)
            result = self.num_list[0] * self.num_list[1]
            self.flag_for_multi = False

        elif self.flag_for_div:
            try:
                num = float(self.ui.textbox.text())
                self.num_list.append(num)
                result = self.num_list[0] / self.num_list[1]
            except:
                result = 'Cannot divide by zero'
            self.flag_for_div = False

        try:
            result = int_or_float(result)
            self.ui.textbox.setText(str(result))
            print(self.num_list)
            self.num_list.clear()
            print(self.num_list)
        
        except:
            pass

    
    def btn_clear(self):
        self.num_list.clear()
        self.ui.textbox.setText('0')
    
    
    def btn_1(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('1')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '1')

    def btn_2(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('2')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '2')

    def btn_3(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('3')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '3')

    def btn_4(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('4')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '4')

    def btn_5(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('5')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '5')

    def btn_6(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('6')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '6')

    def btn_7(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('7')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '7')

    def btn_8(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('8')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '8')

    def btn_9(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('9')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '9')

    def btn_0(self):
        if self.ui.textbox.text() == '0':
            self.ui.textbox.setText('0')
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + '0')


app = QApplication([])
window = Calculator()
app.exec()