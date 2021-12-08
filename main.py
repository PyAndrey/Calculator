import tkinter as tk

window = tk.Tk()


def main():
    greeting = tk.Label(text="0", bg="black", fg="white")
    greeting.grid(column=0, columnspan=4, row=0)

    # 1 ряд
    button = tk.Button(
        text="CE",
        width=25,
        height=10,
        activebackground="#606060",
        background="#404040",
        activeforeground="white",
        foreground="white",
        highlightcolor="yellow",
        bd=0,
    )
    button.grid(column=0, row=1)
    button = tk.Button(
        text="C",
        width=25,
        height=10,
        activebackground="#606060",
        background="#404040",
        activeforeground="white",
        foreground="white",
        border=0,
    )
    button.grid(column=1, row=1)
    button = tk.Button(
        text="<",
        width=25,
        height=10,
        activebackground="#606060",
        background="#404040",
        activeforeground="white",
        foreground="white",
        border=0,
    )
    button.grid(column=2, row=1)
    button = tk.Button(
        text="/",
        width=25,
        height=10,
        activebackground="#606060",
        background="#404040",
        activeforeground="white",
        foreground="white",
        border=0,
    )
    button.grid(column=3, row=1)

    # 2 ряд
    button = tk.Button(
        text="7",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=0, row=2)
    button = tk.Button(
        text="8",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=1, row=2)
    button = tk.Button(
        text="9",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=2, row=2)
    button = tk.Button(
        text="\u00D7",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=3, row=2)

    # 3 ряд
    button = tk.Button(
        text="4",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=0, row=3)
    button = tk.Button(
        text="5",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=1, row=3)
    button = tk.Button(
        text="6",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=2, row=3)
    button = tk.Button(
        text="-",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=3, row=3)

    # 4 ряд
    button = tk.Button(
        text="1",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=0, row=4)
    button = tk.Button(
        text="2",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=1, row=4)
    button = tk.Button(
        text="3",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=2, row=4)
    button = tk.Button(
        text="+",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=3, row=4)

    # 5 ряд
    button = tk.Button(
        text="+/-",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=0, row=5)
    button = tk.Button(
        text="0",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=1, row=5)
    button = tk.Button(
        text=".",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=2, row=5)
    button = tk.Button(
        text="=",
        width=6,
        height=2,
        bg="#404040",
        fg="white",
    )
    button.grid(column=3, row=5)


if __name__ == "__main__":
    main()
    window.mainloop()
