# -*- coding: utf-8 -*-
# =========================================================== #
#                    Classe SortRésurrection                  #
#                                                             #
# Jean-Philippe Mongeau                                       #
# sortrésurrection.py                                         #
# Dernière modification: 13 mai 2014                          #
#                   Par: Jean-Philippe Mongeau                #
#                                                             #
# =========================================================== #

from sort import Sort
from dé import Dé

class SortRésurrection(Sort):
    """
    Classe permettant l'utilisation du sort de résurrection

    Méthodes:
        __init__()
        activer(cible)
    """
    
    # ---------------------------
    #         __init__()
    # ---------------------------
    def __init__(self):
        """
        Instancie le sort de résurrection

        Exemple:
            >>> sort = SortRésurrection()
            >>> print(sort)
            Résurrection: c=4;m=15
            
        """
        super().__init__(une_classe = 4, une_mana_requise = 15)

    def __str__(self):
        """
        Un retour en string
        """
        return "Résurrection: " + super().__str__()


    # ---------------------------
    #       activer(cible)
    # ---------------------------
    def activer(self, cible):
        """
        Active le sort de résurrection sur une cible.

        Paramètres:
            cible: Une cible de type Belligérent qui doit être réssuscitée

        Retour:
            Aucun

        Exemple:
            >>> from guerrier import Guerrier
            >>> from mage import Mage
            >>> cible = Guerrier("Patrick Lafrance")
            >>> résurecteur = Mage("Émile Brunelle")
            >>> résurecteur.puissance = 5
            >>> cible.pts_vie = 0
            >>> sort = SortRésurrection()
            >>> résurecteur.jeter_sort(sort, cible)
            >>> print(True if cible.pts_vie > 0 else False)
            True
            
        """
        if cible.pts_vie == 0:
            dé1 = Dé.lancer(20)
            dé2 = Dé.lancer(20)
            cible.pts_vie = dé1+dé2
        else:
            return "\n\nLa cible n'est pas morte, vous ne pouvez pas la faire revivre!\n\n"
