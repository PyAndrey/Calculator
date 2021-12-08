import tkinter as tk


def create_btn(column, row, text):
    def on_enter(e):
        button["background"] = "#4A4A4A"
        button["foreground"] = "white"

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
        font=("Arial", 12)
    )

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    button.grid(column=column, row=row)


def main():
    greeting = tk.Label(
        text="0", 
        bg="black", 
        fg="white",
        justify=tk.RIGHT,
        width=12,
        font=("Arial", 24),
        bd=0,
        )
    greeting.grid(column=0, columnspan=4, row=0)

    # 1 ряд
    create_btn(0, 1, "CE")
    create_btn(1, 1, "C")
    create_btn(2, 1, "<")
    create_btn(3, 1, "/")
    # 2 ряд
    create_btn(0, 2, "7")
    create_btn(1, 2, "8")
    create_btn(2, 2, "9")
    create_btn(3, 2, "\u00D7")
    # 3 ряд
    create_btn(0, 3, "4")
    create_btn(1, 3, "5")
    create_btn(2, 3, "6")
    create_btn(3, 3, "-")
    # 4 ряд
    create_btn(0, 4, "1")
    create_btn(1, 4, "2")
    create_btn(2, 4, "3")
    create_btn(3, 4, "+")
    # 5 ряд
    create_btn(0, 5, "+/-")
    create_btn(1, 5, "0")
    create_btn(2, 5, ".")
    create_btn(3, 5, "=")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Калькулятор")
    window.resizable(False, False)
    main()
    window.mainloop()
