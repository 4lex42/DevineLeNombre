class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.victoires = 0
        self.defaites = 0
        self.meilleur_score = None

    def enregistrer_resultat(self, gagné, essais):
        if gagné:
            self.victoires += 1
            if self.meilleur_score is None or essais < self.meilleur_score:
                self.meilleur_score = essais
        else:
            self.defaites += 1

    def ratio(self):
        total = self.victoires + self.defaites
        return round((self.victoires / total) * 100, 2) if total else 0
