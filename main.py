"""
Alpha 2.2
Calculator by Andrei Yuzvuk
26.12.2021
"""
import tkinter as tk
from tkinter.constants import *
from collections.abc import Callable


class Calculator:
    
    # Инициализация окна
    window = tk.Tk()
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

    def create_btn(self, column: int, row: int, text: str, func: Callable) -> None:
        """Создание кнопок"""
        # При наведении курсора
        def on_enter(e):
            button["background"] = "#4A4A4A"
            button["foreground"] = "white"

        # При убирании курсора
        def on_leave(e):
            button["background"] = "#404040"
            button["foreground"] = "white"

        button = tk.Button(
            text=text,
            width=9,
            height=3,
            activebackground="#606060",
            background="#404040",
            activeforeground="white",
            foreground="white",
            bd=0,
            font=("Arial", 12),
            command=lambda: func(text),
        )

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        button.grid(column=column, row=row)

    def create_label(self) -> None:
        """Создание поля вывода чисел и операций"""
        self.label = tk.Label(
            text="0",
            bg="black",
            fg="white",
            anchor=tk.SE,
            justify=tk.RIGHT,
            height=3,
            font=("Arial", 24),
            bd=0,
        )
        self.label.grid(columnspan=4, row=0, sticky=W + E)

    def clear_all(self, text: str) -> None:
        """Кнопка CE,C очистки всего"""
        self.a = ""  # Первое число
        self.b = ""  # Второе число
        self.sign = ""  # Знак операции
        self.finish = False # Была нажата кнопка = ?
        self.label.config(text="0")
    
    # Оптимизировать!
    def backspace(self, text: str) -> None:
        """Кнопка удаления последней цифры"""
        if self.a == '' and self.sign == '' and self.b == '':
            self.label.config(text='0')
        elif self.a != '' and self.sign == '' and self.b == '':
            self.a = self.a[0:-1]
            self.label.config(text=self.a)
        elif self.a != '' and self.sign != '' and self.b != '':
            self.b = self.b[0:-1]
            self.label.config(text=self.b)

    # Оптимизировать!
    def calculate(self, text: str) -> None:
        """Функция вычислений и логики"""
        # Получаю нажатую кнопку
        key = text
        # Если нажата кнопка 0-9 или .
        if key in self.digit:
            # Если второе число == '' и знак = ''
            if self.b == '' and self.sign == '':
                self.a += key
                print(f'{self.a=}')
                self.label.config(text=self.a)
            # Если первое число != '' и второе число != '' и finish == True
            elif self.a != '' and self.b != '' and self.finish:
                self.b = key
                self.finish = False
                self.label.config(text=self.b)
            else:
                self.b += key
                print(f'{self.b=}')
                self.label.config(text=self.b)
                

        # Если нажата кнопка + - / *
        if key in self.action:
            self.sign = key
            self.label.config(text=self.sign)
        
        # Если нажата +/-
        if key == '+/-':
            if self.a != '' and self.b == '':
                self.a = f"-{self.a}"
                self.label.config(text=self.a)
            elif self.a != '' and self.b != '':
                self.b = f"-{self.b}"
                self.label.config(text=self.b)

        # Нажата =
        if key == '=':
            if self.b == '': self.b = self.a
            # Преобразование во float если возможно
            try:
                self.a = int(self.a)
                self.b = int(self.b)
            except ValueError:
                self.a = float(self.a)
                self.b = float(self.b)
            match self.sign:
                case '+':
                    self.a = self.a + self.b
                case '-':
                    self.a = self.a - self.b
                case '/':
                    try:
                        self.a = self.a / self.b
                    except ZeroDivisionError:
                        self.label.config(text="Ошибка")
                        self.a = ""  # Первое число
                        self.b = ""  # Второе число
                        self.sign = "" # Знак
                        return
                    # Умножить
                case '\u00D7':
                    self.a = self.a * self.b
            self.a = str(self.a)
            self.b = str(self.b)
            self.finish = True
            self.label.config(text=self.a)

    def main(self) -> None:
        # Label
        self.create_label()
        # 1 ряд
        self.create_btn(0, 1, "CE", self.clear_all)
        self.create_btn(1, 1, "C", self.clear_all)
        self.create_btn(2, 1, "<", self.backspace)
        self.create_btn(3, 1, "/", self.calculate)
        # 2 ряд
        self.create_btn(0, 2, "7", self.calculate)
        self.create_btn(1, 2, "8", self.calculate)
        self.create_btn(2, 2, "9", self.calculate)
        self.create_btn(3, 2, "\u00D7", self.calculate) # Умножить
        # 3 ряд
        self.create_btn(0, 3, "4", self.calculate)
        self.create_btn(1, 3, "5", self.calculate)
        self.create_btn(2, 3, "6", self.calculate)
        self.create_btn(3, 3, "-", self.calculate)
        # 4 ряд
        self.create_btn(0, 4, "1", self.calculate)
        self.create_btn(1, 4, "2", self.calculate)
        self.create_btn(2, 4, "3", self.calculate)
        self.create_btn(3, 4, "+", self.calculate)
        # 5 ряд
        self.create_btn(0, 5, "+/-", self.calculate)
        self.create_btn(1, 5, "0", self.calculate)
        self.create_btn(2, 5, ".", self.calculate)
        self.create_btn(3, 5, "=", self.calculate)

    def start(self) -> None:
        self.main()
        Calculator.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.start()
