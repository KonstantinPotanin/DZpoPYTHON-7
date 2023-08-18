# # Задача 34
import tkinter as tk
from tkinter import messagebox


def get_entry():
    value = text_input.get()
    value = value.lower()
    value = value.split()
    vowel_count = list(map(lambda string_line: sum(map(lambda char: char in "аяуюэеыиоё",
                                                       string_line.replace("-", ""))), value))
    if not any(vowel_count):
        messagebox.showinfo('Внимание', 'Нечего проверять')

    elif all(count == vowel_count[0] for count in vowel_count):
        messagebox.showinfo('Внимание', 'Парам пам-пам')

    else:
        messagebox.showinfo('Внимание', 'Пам парам')


def delete_entry():
    text_input.delete(0, tk.END)


window = tk.Tk()
window.geometry('360x110')
window.title('Винни-Пух')

tk.Label(window, text='Введите стихотворение Винни-Пуха:').grid(row=0, column=0, padx=5, pady=20, stick='wens')

text_input = tk.Entry(window)
text_input.grid(row=0, column=1, padx=5, pady=10, stick='wens')

tk.Button(window, text='Проверка', command=get_entry).grid(row=1, column=0, stick='wens')
tk.Button(window, text='Удалить', command=delete_entry).grid(row=1, column=1, stick='wens')


window.mainloop()
