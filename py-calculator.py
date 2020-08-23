import tkinter as tk


class Calculator:
    def __init__(self):
        pass

    def add(self, list):
        n = 0
        for i in list:
            n += i
        return n

    def multiply(self, list):
        n = 1
        for i in list:
            n *= i
        return n

    def divide(self, list):
        n = list[0]
        for i in list[1::]:
            n /= i
        return n

    def subtract(self, list):
        n = list[0]
        for i in list[1::]:
            n -= i
        return n

    def set_expression(self, num):
        """ Assigns the clicked buttons value to the entry box. """
        sum_entry.insert(tk.END, num)

    def clear_expression(self):
        """ Clears the entry window, equivelant to the C button on calculator. """
        sum_entry.delete(0, tk.END)

    def calc_expression(self):
        """ Calculates the given expression """
        expression = sum_entry.get()
        result = 0

        if "*" in expression:
            nums = [int(i) for i in (expression.split("*"))]
            result = calc.multiply(nums)
        elif "/" in expression:
            nums = [int(i) for i in (expression.split("/"))]
            result = calc.divide(nums)
        elif "+" in expression:
            nums = [int(i) for i in (expression.split("+"))]
            result = calc.add(nums)
        elif "-" in expression:
            nums = [int(i) for i in (expression.split("-"))]
            result = calc.subtract(nums)

        calc.clear_expression()
        calc.set_expression(result)


calc = Calculator()


# Global variables

btn_width = 7
btn_height = 3

# Main window

window = tk.Tk()
window.title("Simple Calculator")
window.columnconfigure([0, 3], weight=1)
window.rowconfigure([0, 5], weight=1)
window.iconbitmap('c:/')

# Result pane

sum_entry = tk.Entry(window)
sum_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=10)


# Define calculator number buttons

btn_1 = tk.Button(
    window,
    text="1",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("1"),
)

btn_2 = tk.Button(
    window,
    text="2",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("2"),
)

btn_3 = tk.Button(
    window,
    text="3",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("3"),
)

btn_4 = tk.Button(
    window,
    text="4",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("4"),
)

btn_5 = tk.Button(
    window,
    text="5",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("5"),
)

btn_6 = tk.Button(
    window,
    text="6",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("6"),
)

btn_7 = tk.Button(
    window,
    text="7",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("7"),
)

btn_8 = tk.Button(
    window,
    text="8",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("8"),
)

btn_9 = tk.Button(
    window,
    text="9",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("9"),
)

btn_0 = tk.Button(
    window,
    text="0",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("0"),
)


# Define alculator operation buttons

btn_add = tk.Button(
    window,
    text="+",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("+"),
)
btn_subtract = tk.Button(
    window,
    text="-",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("-"),
)
btn_multiply = tk.Button(
    window,
    text="*",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("*"),
)
btn_divide = tk.Button(
    window,
    text="/",
    width=btn_width,
    height=btn_height,
    command=lambda: calc.set_expression("/"),
)

# Define calculator generic buttons

btn_clear = tk.Button(window, text="Clear", command=calc.clear_expression)
btn_equal = tk.Button(window, text="=", height=btn_height, command=calc.calc_expression)

# Button layout

btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)

btn_0.grid(row=4, column=0)

btn_add.grid(row=1, column=3)
btn_subtract.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)

btn_clear.grid(row=4, column=1, columnspan=2, sticky="nsew")
btn_equal.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Start event loop

window.mainloop()
