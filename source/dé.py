#=========================
# Nom du fichier: dé.py
# Auteur: Alexandre S.
# Date: 2014-05-13
# Encodage: Unicode(UTF-8)
#=========================

# --- Importe module ---
from random import randint

# --- Classe Dé ---
class  Dé:
    # --- Fonction lancer le dé
    def lancer(faces = 6):
        """
        Simule un lancer de dé
        
        Paramètre:
            faces: int, le nombre de faces du dé à lancer
            
        retour: le nombre aléatoir du dé
        
        Exemple:
        >>> Dé.lancer(-7)
        Traceback (most recent call last):

		AssertionError: Le nombre de faces doit être > 1
		"""
        assert faces > 1, "Le nombre de faces doit être > 1"
        return randint(1, faces)

# --- Test ---
if __name__ == "__main__":
    import doctest
    doctest.testmod()
