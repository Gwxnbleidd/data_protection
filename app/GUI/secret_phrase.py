import time
import tkinter as tk
from tkinter import ttk
import os

from app.GUI.main_window import login_window
from app.utils.encryption import generate_key_using_phrase, form_decrypt_file, encrypt_file
from app.utils.database import User, Database
from app.utils.exit_program import close_program

def open_error_window():
    global error_window
    error_window = tk.Tk()
    error_window.title("Ошибка!")
    error_window.geometry("225x50+800+300")

    # Надписи
    phrase_label = ttk.Label(error_window, text="Неверная парольная фраза!")
    # Кнопки
    confirm_button = ttk.Button(error_window, text="ОК", command=exit)

    phrase_label.grid(row=0,column=0)
    confirm_button.grid(row=1,column=0)
    return
    

def open_window():

    # Создание окна
    global window
    window = tk.Tk()
    window.title("Ввод парольной фразы")
    window.geometry("300x200+800+300")
    window.protocol("WM_DELETE_WINDOW", lambda: close_program(window))

    # Надписи
    phrase_label = ttk.Label(window, text="Введите парольную фразу:")

    # Поля ввода
    global result_label
    global phrase_entry
    phrase_entry = ttk.Entry(window)

    # Кнопки
    confirm_button = ttk.Button(window, text="ОК", command=click_processing)
    exit_button = ttk.Button(window, text="Отмена", command=exit)

    # Текст результата
    result_label = ttk.Label(window, text="")

    # Размещение элементов
    phrase_label.place(x=20, y=20, width=250)
    phrase_entry.place(x=20, y=70, width=250)

    confirm_button.place(x=50, y=120, width=80)
    exit_button.place(x=170, y=120, width=80)

    result_label.place(x=60, y=160, width=250)

    window.mainloop()

def click_processing():
    # если файл не зашифрован - добавить пользователя и зашифровать
    # если зашифрован - расшифровать
    result_label['text'] = ''

    global key
    phrase = phrase_entry.get()
    key = generate_key_using_phrase(phrase)
    
    if not os.path.exists('database.txt'):
        admin = User(username='admin', password='')
        database = Database('database.txt')
        database.add_user(admin)   
        encrypt_file(key, 'database.txt', 'database.txt')
    
    try:
        form_decrypt_file(key)
    except ValueError:
        window.destroy()
        open_error_window()
        return
    
    db = Database()
    database = db.read()

    if database.get('admin'):
        window.destroy()
        login_window()
    else:
        result_label['text'] = 'Неверная парольная фраза'
        exit()

