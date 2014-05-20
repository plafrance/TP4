# -*- coding: utf-8 -*-
# =========================================================== #
#                    Classe SortRésurrection                  #
#                                                             #
# Jean-Philippe Mongeau                                       #
# SortRésurrection.py                                         #
# Version 1.3.2                                               #
# Dernière modification: 15 mai 2014                          #
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
        __str__()
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
            Résurrection : c=4;m=15
            
        """
        super().__init__(4, 15)        

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
            Résurrection : c=4;m=15
            
        """
        return "Résurrection : " + super().__str__()
        
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
            >>> from guerrier import Guerrier
            >>> from mage import Mage
            >>> cible = Guerrier("Patrick Lafrance")
            >>> résurrecteur = Mage("Émile Brunelle")
            >>> cible.pts_vie = 0
            >>> résurrecteur.mana = 69
            >>> résurrecteur.classe = 5
            >>> sort = SortRésurrection()
            >>> résurrecteur.jeter_sort(sort, cible)
            >>> print(True if cible.pts_vie > 0 else False)
            True
                
        """
        if cible.pts_vie == 0:
            cible.pts_vie = Dé.lancer(20)+Dé.lancer(20)
        else:
            return "\n\nLa cible n'est pas morte, vous ne pouvez pas la faire revivre!\n\n"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
