from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QGridLayout


def input_check(new_entry, existing_entry):
    symbol2 = ["*", "/"]
    symbol1 = ["+", "-"]
    point = "."
    if not existing_entry:
        print(existing_entry, bool(not existing_entry))
        if new_entry in symbol2 or new_entry in point:
            return False
        if new_entry is point:
            return False
        if new_entry in symbol1:
            return True
    else:
        try:
            last_entry = existing_entry[-1]
        except IndexError as error:
            print(error)
        else:
            if new_entry in symbol2:
                if last_entry in symbol1:
                    return 0
                elif last_entry in symbol2:
                    return 0
                elif last_entry == point:
                    return 0
            elif new_entry in symbol1:
                if last_entry in symbol2:
                    return True
                elif last_entry in symbol1 and new_entry != last_entry:
                    return 0
                elif last_entry == point:
                    return 0
            if new_entry == point:
                if last_entry == point:
                    return False
                if last_entry in symbol1 or last_entry in symbol2:
                    return False
    return True


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CALCULATOR")
        self.entry = ""
        self.entry_label = QLabel("Question")
        self.answer_label = QLabel("Answer")
        layout = QGridLayout()
        button1 = QPushButton("1")
        button1.clicked.connect(lambda: self.button_clicked(1))
        button2 = QPushButton("2")
        button2.clicked.connect(lambda: self.button_clicked(2))
        button3 = QPushButton("3")
        button3.clicked.connect(lambda: self.button_clicked(3))
        button4 = QPushButton("4")
        button4.clicked.connect(lambda: self.button_clicked(4))
        button5 = QPushButton("5")
        button5.clicked.connect(lambda: self.button_clicked(5))
        button6 = QPushButton("6")
        button6.clicked.connect(lambda: self.button_clicked(6))
        button7 = QPushButton("7")
        button7.clicked.connect(lambda: self.button_clicked(7))
        button8 = QPushButton("8")
        button8.clicked.connect(lambda: self.button_clicked(8))
        button9 = QPushButton("9")
        button9.clicked.connect(lambda: self.button_clicked(9))
        button0 = QPushButton("0")
        button0.clicked.connect(lambda: self.button_clicked(0))
        button_add = QPushButton("+")
        button_add.clicked.connect(lambda: self.button_clicked("+"))
        button_sub = QPushButton("-")
        button_sub.clicked.connect(lambda: self.button_clicked("-"))
        button_mul = QPushButton("*")
        button_mul.clicked.connect(lambda: self.button_clicked("*"))
        button_div = QPushButton("/")
        button_div.clicked.connect(lambda: self.button_clicked("/"))
        button_del = QPushButton("del")
        button_del.clicked.connect(lambda: self.button_clicked(90))
        button_point = QPushButton(".")
        button_point.clicked.connect(lambda: self.button_clicked("."))
        button_enter = QPushButton("=")
        button_enter.clicked.connect(lambda: self.button_clicked(20))
        buttons = [
            button1, button2, button3, button4, button5, button6, button7, button8, button9, button_point, button0,
            button_enter
        ]
        button_2 = [button_del, button_add, button_sub, button_mul, button_div, ]
        layout.addWidget(self.entry_label, 0, 0)
        layout.addWidget(self.answer_label, 1, 0)
        row = 2
        column = 0
        for index, widget in enumerate(buttons):
            layout.addWidget(widget, row, column)
            index += 1
            column += 1
            if index % 3 == 0:
                row += 1
                column = 0
        row2 = 2
        column2 = 3
        for index, widget in enumerate(button_2):
            layout.addWidget(widget, row2, column2)
            row2 += 1

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(250, 350))

    def button_clicked(self, entry):

        if entry == 20:
            try:
                answer = eval(self.entry)
            except SyntaxError as error:
                print(error)
            else:
                self.set_answer(str(answer))
            finally:
                self.entry = ""
                self.set_question()

        elif entry == 90:
            try:
                self.entry = self.entry[:-1]
            except IndexError as error:
                print(error)
                self.entry = ""

            finally:
                self.set_question()
        else:
            entry = str(entry)
            result = input_check(entry, self.entry)
            print(result)
            if result:
                print("i got here first")
                self.entry += entry
                self.set_question()

            elif result == 0:
                self.entry = self.entry[:-1] + entry
                self.set_question()

            elif not result:
                print("i got here")
                pass


    def set_question(self):
        self.entry_label.setText(self.entry)

    def set_answer(self, answer):
        self.answer_label.setText(answer)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
