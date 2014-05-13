#=========================
# Nom du fichier: dé.py
# Auteur: Alexandre S.
# Date: 2014-05-13
# Encodage: Unicode(UTF-8)
#=========================

# --- Importe module ---
import random

# --- Classe Dé ---
class  Dé:
    # --- Fonction lancer le dé
    def lancer(faces = 6):
        """
        Simule un lancer de dé
        
        Paramètre:
            faces: int, le nombre de faces du dé à lancer
            
        """
        assert faces > 1, "Le nombre de faces doit être > 1"
        return random.randint(1, faces)
