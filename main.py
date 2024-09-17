import tkinter as tk

from app.utils.database import User, Database
from app.GUI.main_window import login_window


database = Database()

database.drop()
admin = User(username='admin', password='')
database.add_user(admin)

if __name__ == '__main__':
    login_window('mainloop')