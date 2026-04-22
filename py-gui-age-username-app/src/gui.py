import tkinter as tk
from tkinter import messagebox, simpledialog

class AgeUsernameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion d'âge et de nom d'utilisateur")
        self.age = None
        self.username = None
        self.create_widgets()

    def create_widgets(self):
        self.ask_age()

    def ask_age(self):
        self.age = simpledialog.askinteger("Âge", "Bienvenue! Entrez votre âge :")
        if self.age is None:
            self.exit_app("Au revoir !")
        elif self.age < 18:
            messagebox.showinfo("Accès refusé", "Désolé, c'est interdit aux mineurs.")
            self.exit_app()
        else:
            self.ask_username()

    def ask_username(self):
        self.username = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :")
        while self.username is None or self.username.strip() == "" or self.username.isdigit():
            if self.username is None:
                self.exit_app("Au revoir !")
            elif self.username.isdigit():
                messagebox.showinfo("Erreur", "Le nom d'utilisateur ne doit pas être un nombre. Veuillez réessayer.")
            else:
                messagebox.showinfo("Erreur", "Le nom d'utilisateur ne doit pas être vide. Veuillez réessayer.")
            self.username = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :")
        
        self.welcome_user()

    def welcome_user(self):
        messagebox.showinfo("Bienvenue", f"Bienvenue {self.username} ! Vous avez {self.age} ans.")
        self.exit_app()

    def exit_app(self, message=None):
        if message:
            messagebox.showinfo("Au revoir", message)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeUsernameApp(root)
    root.mainloop()