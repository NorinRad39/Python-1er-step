class Joueur:
    def __init__(self, nom_choisi):
        # C'est le constructeur (le public Joueur() en C#)
        self.nom = nom_choisi
        self.xp = 0

    def gagner_xp(self, quantite): 
        self.xp += quantite
        
        

    def afficher_statut(self):
        # Et ici aussi
        pass
