import random

class Jeu:
    def __init__(self, limite, essais_max):
        self.limite = limite
        self.essais_max = essais_max
        self.essais = 0
        self.secret = random.randint(1, limite)
        self.terminé = False

    def verifier(self, tentative):
        if self.terminé:
            return "Le jeu est terminé."

        self.essais += 1
        if tentative == self.secret:
            self.terminé = True
            return "gagné"
        elif self.essais >= self.essais_max:
            self.terminé = True
            return "perdu"
        elif tentative < self.secret:
            return "petit"
        else:
            return "grand"
