"""
Beta 3.0
Calculator by Andrei Yuzvuk
12.02.2022
Bugs:
    1. 45 + 6 + 6 = 516 - добавить функционал
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
        self.num_first = 0  # Первое число
        self.num_second = 0  # Второе число
        self.sign = ""  # Знак операции
        self.result = 0 # Результат
        self.finish = False # Была нажата кнопка = ?
        self.digit = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
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
        self.num_second = 0  # Второе число
        self.finish = False # Была нажата кнопка = ?
        self.label_text.set("0")

    def clear_all(self, value: str) -> None:
        """Кнопка C очистки всего"""
        self.num_first = 0  # Первое число
        self.num_second = 0  # Второе число
        self.sign = ""  # Знак операции
        self.result = 0 # Результат
        self.finish = False # Была нажата кнопка = ?
        self.label_text.set("0")
    

    def backspace(self, value: str) -> None:
        """Кнопка удаления последней цифры"""
        if len(self.label_text.get()) == 1:
            self.label_text.set("0")
        else:
            self.label_text.set(self.label_text.get()[:-1])
    
    def dot_button_press(self, value):
        """Добавляет в label точку"""
        # Если в строке нету точки, то она добавляется
        if self.label_text.get().count(".") == 0:
            self.label_text.set(self.label_text.get() + ".")

    def number_button_press(self, value: str) -> None:
        """По нажатию на кнопку с цифрой"""
        # Если нажата кнопка 0-9 или .
        if value in self.digit:
            if self.label_text.get() == "0" or self.label_text.get() in self.action:
                self.label_text.set("" + value)
            else:
                self.label_text.set(self.label_text.get() + value)

    def plus_minus_button_press(self, value):
        # Если нажата +/-
        if self.label_text.get().count(".") != 0:
            all_numbers  = float(self.label_text.get())
        else:
            all_numbers  = int(self.label_text.get())
        all_numbers *= -1
        self.label_text.set(all_numbers)

    def math_button_press(self, value: str) -> None:
        """По нажатию на математические знаки"""
        # Если нажата кнопка + - / *
        if value in self.action:
            # Проверка строки на наличие числа float
            if self.label_text.get().count(".") != 0:
                self.num_first  = float(self.label_text.get())
            else:
                self.num_first  = int(self.label_text.get())

            if self.sign == "":
                self.sign = value

            print(f'{self.sign=}')
            self.label_text.set(self.sign)
            
    def equal_button_press(self, value: str) -> None:
        """По нажатию на равно"""
        # Если есть первое число и знак, то прибавляется первое число к первому чилу
        if self.num_second == 0: self.num_second = self.num_first

        if self.label_text.get().count(".") != 0:
            self.num_second  = float(self.label_text.get())
        else:
            self.num_second  = int(self.label_text.get())

        match self.sign:
            case '+':
                self.result = self.num_first + self.num_second
            case '-':
                self.result = self.num_first - self.num_second
            case '/':
                try:
                    self.result = round(self.num_first / self.num_second, 4)
                except ZeroDivisionError:
                    self.label_text.set("0")
                    messagebox.showwarning(message="Ты долбаёб? В школе не учили? На ноль делить нельзя!!!")
                    self.num_first = 0  # Первое число обнулилось
                    self.num_second = 0  # Второе число обнулилось
                    self.sign = "" # Знак обнулился
                    return
            case '\u00D7': # Умножить
                self.result = self.num_first * self.num_second

        self.finish = True
        print(f'{self.result=}')
        self.label_text.set(self.result) 


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
        self.create_btn(5, 0, "+/-", self.plus_minus_button_press)
        self.create_btn(5, 1, "0", self.number_button_press)
        self.create_btn(5, 2, ".", self.dot_button_press)
        self.create_btn(5, 3, "=", self.equal_button_press)

    def start(self) -> None:
        self.main()
        Calculator.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.start()
