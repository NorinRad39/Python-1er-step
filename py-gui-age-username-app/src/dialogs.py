import tkinter as tk
from tkinter import messagebox, simpledialog

def ask_age():
    age = simpledialog.askinteger("Âge", "Bienvenue! Entrez votre âge :")
    return age

def ask_username():
    username = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :")
    return username

def show_error_message(message):
    messagebox.showinfo("Erreur", message)

def show_welcome_message(username, age):
    messagebox.showinfo("Bienvenue", f"Bienvenue {username} ! Vous avez {age} ans.")

def show_exit_message():
    messagebox.showinfo("Au revoir", "Au revoir !")