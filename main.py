import tkinter as tk

from app.utils.database import User, Database
from app.GUI.secret_phrase import open_window as secret_phrase_window


database = Database()

admin = User(username='admin', password='')
try:
    database.add_user(admin)
except Exception as e:
    pass

if __name__ == '__main__':
    secret_phrase_window()