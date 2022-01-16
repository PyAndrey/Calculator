"""
Beta 1.1
Calculator by Andrei Yuzvuk
16.01.2022
Bugs:
    1. Может быть две точки в числе
    2. 45 + 6 + 6 = 516 при двух плюсах добавляется ко 2 числу
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import *
from collections.abc import Callable


class Calculator:
    
    # Инициализация окна
    window = Tk()
    # Изменение заголовка окна
    window.title("Калькулятор")
    # Окно не изменяется по размеру
    window.resizable(False, False)

    def __init__(self) -> None:
        self.a = ""  # Первое число
        self.b = ""  # Второе число
        self.sign = ""  # Знак операции
        self.finish = False # Была нажата кнопка = ?
        self.digit = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")
        self.action = ("/", "\u00D7", "-", "+")
        self.label_text = StringVar(self.window, "0")

    def create_btn(self, row: int, column: int, text: str, func: Callable) -> None:
        """Создание кнопок"""
        # При наведении курсора
        def on_enter(e):
            button["background"] = "#4A4A4A"
            button["foreground"] = "white"

        # При убирании курсора
        def on_leave(e):
            button["background"] = "#404040"
            button["foreground"] = "white"

        button = Button(
            text=text,
            width=9,
            height=3,
            activebackground="#606060",
            background="#404040",
            activeforeground="white",
            foreground="white",
            bd=0,
            font=("Arial", 12, "bold"),
            command=lambda: func(text),
        )

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        button.grid(row=row, column=column)

    def create_label(self) -> None:
        """Создание поля вывода чисел и операций"""
        self.label = Label(
            textvariable=self.label_text,
            background="black",
            foreground="white",
            anchor=SE,
            justify=RIGHT,
            height=3,
            font=("Arial", 24, "bold"),
            bd=0,
        )
        self.label.grid(row=0, columnspan=4, sticky=W + E)

    def clear_last(self, value: str) -> None:
        """Кнопка CE очистки последнего"""
        self.b = ""  # Второе число
        self.finish = False # Была нажата кнопка = ?
        self.label_text.set("0")

    def clear_all(self, value: str) -> None:
        """Кнопка C очистки всего"""
        self.a = ""  # Первое число
        self.b = ""  # Второе число
        self.sign = ""  # Знак операции
        self.finish = False # Была нажата кнопка = ?
        self.label_text.set("0")
    

    def backspace(self, value: str) -> None:
        """Кнопка удаления последней цифры"""
        if self.a != '' and self.sign == '' and self.b == '':
            self.a = self.a[0:-1]
            self.label_text.set(self.a)
            if not self.a:
                self.label_text.set("0")
        elif self.a != '' and self.sign != '' and self.b != '':
            self.b = self.b[0:-1]
            self.label_text.set(self.b)
            if not self.b:
                self.label_text.set("0")

    def isfloat(self, value: str) -> bool:
        """Проверяет строку на число float"""
        try:
            if '.' in value:
                float(value)
                return True
        except ValueError:
            return False

    def number_button_press(self, value: str) -> None:
        """По нажатию на кнопку с цифрой"""
        # Если нажата кнопка 0-9 или .
        if value in self.digit:
            # Если второе число пустое и знак пустой
            if self.b == '' and self.sign == '':
                self.a += value
                print(f'{self.a=}')
                self.label_text.set(self.a)
            # Пофиксить баг
            elif self.a != '' and self.b != '' and self.sign != '':
                self.b = value
                self.finish = False
                self.label_text.set(self.b)
            # Если первое число не пустое и второе число не пустое и нажата равно
            elif self.a != '' and self.b != '' and self.finish:
                self.b = value
                self.finish = False
                self.label_text.set(self.b)
            else:
                self.b += value
                print(f'{self.b=}')
                self.label_text.set(self.b)

    def math_button_press(self, value: str) -> None:
        """По нажатию на математические знаки"""
        # Если нажата кнопка + - / *
        if value in self.action:
            self.sign = value
            print(f'{self.sign=}')
            self.label_text.set(self.sign)
        
        # Если нажата +/-
        if value == '+/-':
            print(f'{value=}')
            # Если первое число не пустое и второе пустое
            if self.a != '' and self.b == '':
                # Первое число становится отрицательным
                self.a = f"-{self.a}"
                self.label_text.set(self.a)
            # Если первое число не пустое и второе не пустое
            elif self.a != '' and self.b != '':
                #  Второе число становится отрицательным
                self.b = f"-{self.b}"
                self.label_text.set(self.b)

    def equal_button_press(self, value: str) -> None:
        """По нажатию на равно"""
        # Нажата =
        if value == '=':
            # Если есть первое число и знак, то прибавляется первое число к первому чилу
            if self.b == '': self.b = self.a

            # Преобразование во float если возможно
            if self.isfloat(self.a) or self.isfloat(self.b):
                self.a = float(self.a)
                self.b = float(self.b)
            else:
                self.a = int(self.a)
                self.b = int(self.b)

            match self.sign:
                case '+':
                    self.a = self.a + self.b
                case '-':
                    self.a = self.a - self.b
                case '/':
                    try:
                        self.a = round(self.a / self.b, 4)
                    except ZeroDivisionError:
                        self.label_text.set("Ошибка")
                        messagebox.showwarning(message="Ты долбаёб? В школе не учили? На ноль делить нельзя!!!")
                        self.a = ""  # Первое число обнулилось
                        self.b = ""  # Второе число обнулилось
                        self.sign = "" # Знак обнулился
                        return
                case '\u00D7': # Умножить
                    self.a = self.a * self.b
            self.a = str(self.a)
            self.b = str(self.b)
            self.finish = True
            print(f'{self.a=}')
            self.label_text.set(self.a)    

    def main(self) -> None:
        """Тело приложения"""
        # Label
        self.create_label()
        # 1 ряд
        self.create_btn(1, 0, "CE", self.clear_last)
        self.create_btn(1, 1, "C", self.clear_all)
        self.create_btn(1, 2, "<", self.backspace)
        self.create_btn(1, 3, "/", self.math_button_press)
        # 2 ряд
        self.create_btn(2, 0, "7", self.number_button_press)
        self.create_btn(2, 1, "8", self.number_button_press)
        self.create_btn(2, 2, "9", self.number_button_press)
        self.create_btn(2, 3, "\u00D7", self.math_button_press) # Умножить
        # 3 ряд
        self.create_btn(3, 0, "4", self.number_button_press)
        self.create_btn(3, 1, "5", self.number_button_press)
        self.create_btn(3, 2, "6", self.number_button_press)
        self.create_btn(3, 3, "-", self.math_button_press)
        # 4 ряд
        self.create_btn(4, 0, "1", self.number_button_press)
        self.create_btn(4, 1, "2", self.number_button_press)
        self.create_btn(4, 2, "3", self.number_button_press)
        self.create_btn(4, 3, "+", self.math_button_press)
        # 5 ряд
        self.create_btn(5, 0, "+/-", self.math_button_press)
        self.create_btn(5, 1, "0", self.number_button_press)
        self.create_btn(5, 2, ".", self.number_button_press)
        self.create_btn(5, 3, "=", self.equal_button_press)

    def start(self) -> None:
        self.main()
        Calculator.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.start()
