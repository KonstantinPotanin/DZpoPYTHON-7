import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'На ввод принимаются только цифры! Вы ввели другие символы')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def add_dot(item):
    value = calc.get()
    if value[-1] in '.':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+item)


def make_dgt_btn(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 14), command=lambda: add_digit(digit))


def make_operation_btn(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 14), fg='red',
                     command=lambda: add_operation(operation))


def make_calc_btn(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 14), fg='red',
                     command=calculate)


def make_clear_btn(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 14), fg='red', command=clear)


def make_dot_btn(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 14), fg='red', command=lambda: add_dot(operation))


def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


window = tk.Tk()
window.geometry('325x330')
window.title('Калькулятор')
window.config(bg='orange')
window.bind('<Key>', press_key)

calc = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 17), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=5, stick='we', padx=5)

make_dgt_btn('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_dgt_btn('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_dgt_btn('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_dgt_btn('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_dgt_btn('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_dgt_btn('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_dgt_btn('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_dgt_btn('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_dgt_btn('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_dgt_btn('0').grid(row=4, column=1, stick='wens', padx=5, pady=5)

make_operation_btn('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_btn('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_btn('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_btn('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_btn('=').grid(row=1, column=4, rowspan=4, stick='wens', padx=5, pady=5)

make_clear_btn('C').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_dot_btn('.').grid(row=4, column=2,  stick='wens', padx=5, pady=5)

window.grid_columnconfigure(0, minsize=65)
window.grid_columnconfigure(1, minsize=65)
window.grid_columnconfigure(2, minsize=65)
window.grid_columnconfigure(3, minsize=65)
window.grid_columnconfigure(4, minsize=65)

window.grid_rowconfigure(0, minsize=65)
window.grid_rowconfigure(1, minsize=65)
window.grid_rowconfigure(2, minsize=65)
window.grid_rowconfigure(3, minsize=65)
window.grid_rowconfigure(4, minsize=65)

window.mainloop()
