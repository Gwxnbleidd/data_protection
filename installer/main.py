import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

import os
import shutil

EXE_FILE='main.py'
SRC_FILE = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/' + EXE_FILE

class InstallerApp:
    def __init__(self, root):
        self.path = ''
        self.root = root
        self.root.title("Установщик")
        self.root.geometry("300x205+600+300")

        # Надписи
        self.label = ttk.Label(root, text="Укажите путь для установки программы")
        self.path_entry = ttk.Entry(root, state='readonly', width=30)

        # Кнопки
        self.path_button = ttk.Button(root, text="Выбрать путь", command=self.handler_click_to_path_button)
        self.confirm_button = ttk.Button(root, text="Установить", command=self.handler_click_to_confirm_button, state=tk.DISABLED)

        # Размещение элементов
        self.label.pack(pady=5)
        self.path_entry.pack(pady=10)
        self.path_button.pack(pady=20)
        self.confirm_button.pack(pady=5)

    def handler_click_to_path_button(self):
        self.path = filedialog.askdirectory()
        if self.path:
            self.path_entry.configure(state='normal')
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, self.path)
            self.path_entry.configure(state='readonly')
            self.confirm_button.configure(state=tk.NORMAL)


    def handler_click_to_confirm_button(self):
        try:
            shutil.copy(SRC_FILE, self.path)
            messagebox.showinfo("Success", f"Installation successful! File copied to {EXE_FILE}")
        except Exception as e:
            messagebox.showerror("Error", f"Installation failed: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
