# -*- encoding:utf-8 -*-
#sortprotection.py
#Gilbert Paquin
#2014/05/13
#
# Sort de protection
from sort import Sort

"""
Class SortProtection
Sort qui augmente la protection d’un belligérant.
— Hérite de : Sort
"""
class SortProtection(Sort):
    """
    Initialise le Sort avec sa classe et sa mana.
    """
    def __init__(self):
        super().__init__(une_classe = 2, une_mana_requise = 8)

    def __str__(self):
        """
        Un retour en string
        """
        return "SortProtection: " + super().__str__()

    def activer(self, cible):
        """
        Active le sort qui agit alors sur sa cible. Il augmente
        la défense du belligérant de 50%.
        — Paramètres :
        (i) cible (Belligérant) : Le belligérant ciblé par le sort.

        Exemple
        >>> from guerrier import Guerrier
        >>> from mage import Mage
        >>> cible = Guerrier("Patrick Lafrance")
        >>> mage = Mage("Émile Brunelle")
        >>> mage.puissance = 3
        >>> sort = SortProtection()
        >>> prev_def = cible.défense
        >>> mage.jeter_sort(sort, cible)
        >>> cible.bounus_défense == prev_def*1.5
        True
        """
        cible.bounus_défense = cible.bonus_défense * 0.5