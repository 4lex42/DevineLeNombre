import json
import os

class GestionScores:
    def __init__(self, chemin="data/scores.json"):
        self.chemin = chemin
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        if not os.path.exists(chemin):
            with open(chemin, "w") as f:
                json.dump({}, f)

    def charger(self):
        with open(self.chemin, "r") as f:
            return json.load(f)

    def enregistrer(self, joueur):
        data = self.charger()
        data[joueur.nom] = {
            "victoires": joueur.victoires,
            "defaites": joueur.defaites,
            "meilleur_score": joueur.meilleur_score
        }
        with open(self.chemin, "w") as f:
            json.dump(data, f, indent=2)
