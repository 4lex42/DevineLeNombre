import tkinter as tk
from tkinter import messagebox
from game import Jeu
from player import Joueur
from score_manager import GestionScores

class JeuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Devine le nombre")
        self.root.geometry("400x400")

        self.scores = GestionScores()
        self.joueur = None
        self.jeu = None

        self.difficultes = {
            "Facile": (50, 10),
            "Moyen": (100, 7),
            "Difficile": (200, 5)
        }

        self.afficher_ecran_demarrage()

    def afficher_ecran_demarrage(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=40)

        tk.Label(self.frame, text="Entrez votre nom :").pack()
        self.entry_nom = tk.Entry(self.frame)
        self.entry_nom.pack()

        tk.Label(self.frame, text="Choisissez une difficulté :").pack()
        self.diff_var = tk.StringVar(value="Facile")
        tk.OptionMenu(self.frame, self.diff_var, *self.difficultes.keys()).pack()

        tk.Button(self.frame, text="Commencer", command=self.commencer_jeu).pack(pady=10)

    def commencer_jeu(self):
        nom = self.entry_nom.get().strip()
        if not nom:
            messagebox.showerror("Erreur", "Nom requis.")
            return

        self.joueur = Joueur(nom)
        limite, essais = self.difficultes[self.diff_var.get()]
        self.jeu = Jeu(limite, essais)

        self.frame.destroy()
        self.afficher_zone_jeu()

    def afficher_zone_jeu(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label_info = tk.Label(self.frame, text=f"Devine entre 1 et {self.jeu.limite}")
        self.label_info.pack()

        self.entry = tk.Entry(self.frame)
        self.entry.pack()

        self.label_feedback = tk.Label(self.frame, text="")
        self.label_feedback.pack(pady=5)

        tk.Button(self.frame, text="Valider", command=self.valider_essai).pack(pady=10)

    def valider_essai(self):
        val = self.entry.get()
        if not val.isdigit():
            self.label_feedback.config(text="Nombre invalide.", fg="orange")
            return

        resultat = self.jeu.verifier(int(val))

        couleurs = {
            "petit": "blue",
            "grand": "purple",
            "gagné": "green",
            "perdu": "red",
            "Le jeu est terminé.": "gray"
        }

        messages = {
            "petit": "Trop petit !",
            "grand": "Trop grand !",
            "gagné": "🎉 Gagné !",
            "perdu": f"😞 Perdu ! C'était {self.jeu.secret}",
            "Le jeu est terminé.": "Le jeu est déjà terminé."
        }

        if resultat in messages:
            self.label_feedback.config(text=messages[resultat], fg=couleurs[resultat])

            if resultat == "gagné":
                self.joueur.enregistrer_resultat(True, self.jeu.essais)
                self.fin_jeu()
            elif resultat == "perdu":
                self.joueur.enregistrer_resultat(False, self.jeu.essais)
                self.fin_jeu()
        else:
            self.label_feedback.config(text="Erreur inconnue", fg="black")

    def fin_jeu(self):
        self.scores.enregistrer(self.joueur)
        tk.Button(self.frame, text="Rejouer", command=self.rejouer).pack(pady=10)
        tk.Button(self.frame, text="Quitter", command=self.root.quit).pack()

    def rejouer(self):
        self.frame.destroy()
        self.afficher_ecran_demarrage()
