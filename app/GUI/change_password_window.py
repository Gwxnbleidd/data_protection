import tkinter as tk
from tkinter import ttk
import re

from app.utils.database import Database

def check_restrictions(pwd):
  lowercase = r"[a-z]"
  uppercase = r"[A-Z]"
  numbers = r"[0-9]"
  arithmetic_operators = r"[+\-*/]"

  return bool(re.search(lowercase, pwd) and re.search(uppercase, pwd) and 
              re.search(numbers, pwd) and re.search(arithmetic_operators, pwd))

# --- Основное окно ---
def open_window():
    global window
    global old_pwd_entry
    global new_pwd_entry
    global result_label

    window = tk.Tk()
    window.title("Главное окно")
    window.geometry("300x270+800+300")

    
    old_pwd_label = ttk.Label(window, text='Старый пароль')
    new_pwd_label = ttk.Label(window, text='Новый пароль')
    result_label = ttk.Label(window, text='')

    old_pwd_entry = ttk.Entry(window, show='*')
    new_pwd_entry = ttk.Entry(window, show='*')

    change_password_button = ttk.Button(window, text="Сменить пароль", command=change_password)
    exit_button = ttk.Button(window, text="Отмена", command=lambda: window.destroy())

    old_pwd_label.place(x=15, y=10, width=120)
    new_pwd_label.place(x=15, y=60, width=120)

    old_pwd_entry.place(x=150, y=10, width=135)
    new_pwd_entry.place(x=150, y=60, width=135)

    change_password_button.place(x=15, y=110, width=150)
    exit_button.place(x=185, y=110, width=100)

    result_label.place(x=25, y=160, width=270)

def change_password():
    db = Database()
    
    from app.GUI.main_window import current_user

    current_user = db.find_user(current_user)

    old_pwd = old_pwd_entry.get()
    if old_pwd != current_user.password:
        result_label['text'] = 'Старый пароль неверен!'
        return
    
    new_pwd = new_pwd_entry.get()
    if current_user.restrictions:
        if not check_restrictions(new_pwd):
            result_label['text'] = 'Пароль должен содержать\nцифру, знак арифметической, \nоперации заглавную \nи строчную буквы!'
            return
        
    db.change_password(username=current_user.username, new_password=new_pwd)
    window.destroy()

