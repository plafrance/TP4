# -*- coding: utf-8 -*-
# =========================================================== #
#                    Classe SortRésurrection                  #
#                                                             #
# Jean-Philippe Mongeau                                       #
# SortRésurrection.py                                         #
# Dernière modification: 13 mai 2014                          #
#                   Par: Jean-Philippe Mongeau                #
#                                                             #
# =========================================================== #

from Sort import Sort

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
            Résurrection C=4 M=15
            
        """
        super().__init__(une_classe = 4, une_mana_requise = 15)        

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
            >>> résurecteur = Mage("Émile Brunelle")
            >>> cible.pts_vie(0)
            >>> sort = SortRésurrection()
            >>> résurecteur.jeter_sort(sort, cible)
            >>> return True if cible.pts_vie > 0 else return False
            True
            
        """
        if cible.pts_vie == 0:
            cible.pts_vie(2*Dé(20))
        else:
            return "\n\nLa cible n'est pas morte, vous ne pouvez pas la faire revivre!\n\n"
