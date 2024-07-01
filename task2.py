import tkinter as tk

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""


window = tk.Tk()
window.title("Simple Calculator")


input_text = tk.StringVar()


input_entry = tk.Entry(window, textvariable=input_text, font=('arial', 18, 'bold'), bd=20, insertwidth=4, bg='powder blue', justify='right')
input_entry.grid(columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(window, text=text, padx=10, pady=10, font=('arial', 18, 'bold'), bd=8, bg='powder blue',
                       command=lambda item=text: button_click(item))
    button.grid(row=row, column=column)


clear_button = tk.Button(window, text='C', padx=10, pady=10, font=('arial', 18, 'bold'), bd=8, bg='powder blue',
                         command=button_clear)
clear_button.grid(row=4, column=1)


equal_button = tk.Button(window, text='=', padx=10, pady=10, font=('arial', 18, 'bold'), bd=8, bg='powder blue',
                         command=button_equal)
equal_button.grid(row=4, column=2)


window.mainloop()