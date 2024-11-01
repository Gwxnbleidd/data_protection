import tkinter as tk
from tkinter import ttk

from app.GUI.main_window import login_window

def open_window():

    # Создание окна
    window = tk.Tk()
    window.title("Ввод парольной фразы")
    window.geometry("300x200+800+300")

    # Надписи
    phrase_label = ttk.Label(window, text="Введите парольную фразу:")

    # Поля ввода
    global username_entry
    global result_label
    phrase_entry = ttk.Entry(window)

    # Кнопки
    confirm_button = ttk.Button(window, text="ОК", command=login_window)
    exit_button = ttk.Button(window, text="Отмена", command=window.destroy)

    # Текст результата
    result_label = ttk.Label(window, text="")

    # Размещение элементов
    phrase_label.place(x=20, y=20, width=250)
    phrase_entry.place(x=20, y=70, width=250)

    confirm_button.place(x=50, y=120, width=80)
    exit_button.place(x=170, y=120, width=80)

    result_label.place(x=60, y=160, width=250)

    window.mainloop()