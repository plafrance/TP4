# -*- coding: utf-8 -*-
# =========================================================== #
#                    Classe SortRésurrection                  #
#                                                             #
# Jean-Philippe Mongeau                                       #
# SortRésurrection.py                                         #
# Version 1.3                                                 #
# Dernière modification: 13 mai 2014                          #
#                   Par: Jean-Philippe Mongeau                #
#                                                             #
# =========================================================== #

from sort import Sort
from guerrier import Guerrier
from mage import Mage
from belligérant import Belligérant
from dé import Dé

class SortRésurrection(Sort):
    """
    Classe permettant l'utilisation du sort de résurrection

    Méthodes:
        __init__()
        activer(cible)
    """
    
    # --------------------------- #
    #         __init__()          #
    # --------------------------- #
    def __init__(self):
        """
        Instancie le sort de résurrection

        Exemple:
            >>> sort = SortRésurrection()
            >>> print(sort)
            Résurrection : classe 4 ; mana requise : 15
            
        """
        super().__init__(une_classe = 4, une_mana_requise = 15)        

    # --------------------------- #
    #          __str__()          #
    # --------------------------- #
    def __str__(self):
        """
        Retourne une représentation de la classe sous forme de chaîne de caractère.
        
        Retour:
            Une représentation du Sort sous la forme «Résurrection : classe classe ; mana requise : mana_requise».

        Exemple:
            >>> sort = SortRésurrection()
            >>> print(sort.__str__())
            "Résurrection : classe 4 ; mana requise : 15"
            
        """
        return str("Résurrection : classe 4 ; mana requise : 15")
        
    # --------------------------- #
    #       activer(cible)        #
    # --------------------------- #
    def activer(self, cible):
        """
        Active le sort de résurrection sur une cible.

        Paramètres:
            cible: Une cible de type Belligérent qui doit être réssuscitée

        Retour:
            Aucun

        Exemple:
            >>> cible = Guerrier("Patrick Lafrance")
            >>> résurrecteur = Mage("Émile Brunelle")
            >>> cible.pts_vie(0)
            >>> sort = SortRésurrection()
            >>> résurrecteur.jeter_sort(sort, cible)
            >>> return True if résurrecteur.mana < 15
            >>> return True if cible.pts_vie > 0 else return False
            True
            
        """
        if cible.pts_vie == 0:
            cible.pts_vie(2*Dé(20))
        else:
            return "\n\nLa cible n'est pas morte, vous ne pouvez pas la faire revivre!\n\n"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
