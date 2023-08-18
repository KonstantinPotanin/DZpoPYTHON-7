#  Задача 36
import tkinter as tk


def multiplication_operation(row, col):
    return row * col


def print_operation_table():
    num_rows = int(entry_rows.get())
    num_columns = int(entry_columns.get())

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            result = multiplication_operation(row, col)
            output_text.insert(tk.END, f'{result:4} ')
        output_text.insert(tk.END, '\n')


def clear_table():
    output_text.delete("1.0", tk.END)


window = tk.Tk()
window.title("Таблица умножения")

label_rows = tk.Label(window, text="Количество строк:")
label_rows.grid(row=0, column=0)

entry_rows = tk.Entry(window)
entry_rows.grid(row=0, column=1)

label_columns = tk.Label(window, text="Количество столбцов:")
label_columns.grid(row=1, column=0)

entry_columns = tk.Entry(window)
entry_columns.grid(row=1, column=1)

button_generate = tk.Button(window, text="Создать таблицу", command=print_operation_table)
button_generate.grid(row=2, column=0, columnspan=2, stick='we')

button_clear = tk.Button(window, text="Удалить таблицу", command=clear_table)
button_clear.grid(row=3, column=0, columnspan=2, stick='we')

output_text = tk.Text(window, height=10, width=40)
output_text.grid(row=4, column=0, columnspan=2)

window.mainloop()

# Не графическое решение
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for row in range(1, num_rows + 1):
#         for col in range(1, num_columns + 1):
#             result = operation(row, col)
#             print(f'{result:3}', end=' ')
#         print()
#
#
# print_operation_table(lambda row, col: row * col)

