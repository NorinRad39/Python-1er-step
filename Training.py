import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()

age  = simpledialog.askinteger("Âge", f"Bienvenue! Entrez votre âge :") 

if age is not None and age < 18:
    messagebox.showinfo("Accés refusé", "Désolé, c'est interdit aux mineurs.")
    
if age is None :
    messagebox.showinfo("Au revoir", "Au revoir !")
    root.destroy()
    
nom_utilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :") 

while nom_utilisateur.isdigit() or nom_utilisateur == "":
    
    if nom_utilisateur is not None and nom_utilisateur.isdigit():
            messagebox.showinfo("Erreur", "Le nom d'utilisateur ne doit pas être un nombre. Veuillez réessayer.")
            nom_utilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :")
            

    if nom_utilisateur == "":
            messagebox.showinfo("Erreur", "Le nom d'utilisateur ne doit pas être vide. Veuillez réessayer.")
            nom_utilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :")
        
if nom_utilisateur is None:
    messagebox.showinfo("Au revoir", "Au revoir !")           
    root.destroy()
    

    
messagebox.showinfo("Bienvenue", f"Bienvenue {nom_utilisateur} ! Vous avez {age} ans.")
   

root.destroy()