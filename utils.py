# Ajoute des outils comme lecture de sons, conversions, etc.
from playsound import playsound

def jouer_son(victoire: bool):
    chemin = "assets/win_sound.mp3" if victoire else "assets/lose_sound.mp3"
    playsound(chemin)
