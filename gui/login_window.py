

import tkinter as tk
from tkinter import messagebox
from utils.file_handler import FileHandler

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoBot - Logowanie")
        self.root.geometry("300x200")
        self.root.resizable(False, False)


        tk.Label(root, text="Login:").pack(pady=(20, 5))
        self.login_entry = tk.Entry(root)
        self.login_entry.pack()

        tk.Label(root, text="Hasło:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()


        tk.Button(root, text="Zaloguj", command=self.login).pack(pady=(15, 5))
        tk.Button(root, text="Zarejestruj", command=self.register).pack()

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        if FileHandler.validate_user(login, password):
            messagebox.showinfo("Sukces", "Zalogowano pomyślnie!")

            self.root.destroy()
            from gui.dashboard_window import CryptoDashboard
            new_root = tk.Tk()
            app = CryptoDashboard(new_root)
            new_root.mainloop()

        else:
            messagebox.showerror("Błąd", "Niepoprawny login lub hasło.")

    def register(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        if FileHandler.add_user(login, password):
            messagebox.showinfo("Sukces", "Użytkownik zarejestrowany!")
        else:
            messagebox.showerror("Błąd", "Użytkownik już istnieje.")
