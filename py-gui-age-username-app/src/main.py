import tkinter as tk
from tkinter import messagebox
from gui import create_gui
from dialogs import ask_age, ask_username

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    age = ask_age()
    if age is None:
        messagebox.showinfo("Au revoir", "Au revoir !")
        root.destroy()
        return

    if age < 18:
        messagebox.showinfo("Accès refusé", "Désolé, c'est interdit aux mineurs.")
        root.destroy()
        return

    username = ask_username()
    if username is None:
        messagebox.showinfo("Au revoir", "Au revoir !")
        root.destroy()
        return

    messagebox.showinfo("Bienvenue", f"Bienvenue {username} ! Vous avez {age} ans.")
    root.destroy()

if __name__ == "__main__":
    main()