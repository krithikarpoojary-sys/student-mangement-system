import tkinter as tk
from tkinter import messagebox
import os

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        window.destroy()
        os.system("python main.py")
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )

window = tk.Tk()
window.title("Login")
window.geometry("350x250")
window.configure(bg="#D6EAF8")

tk.Label(
    window,
    text="Login",
    font=("Arial", 18, "bold"),
    bg="#D6EAF8"
).pack(pady=15)
tk.Label(
    window,
    text="Student Management System",
    font=("Arial", 10),
    bg="#D6EAF8",
    fg="gray"
).pack()
tk.Label(window, text="Username", bg="#D6EAF8").pack()
username_entry = tk.Entry(window, width=25)
username_entry.pack(pady=5)

tk.Label(window, text="Password", bg="#D6EAF8").pack()
password_entry = tk.Entry(window, show="*", width=25)
password_entry.pack(pady=5)

tk.Button(
    window,
    text="Login",
    command=login,
    bg="green",
    fg="white",
    width=15
).pack(pady=20)
window.mainloop()
