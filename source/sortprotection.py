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
        """
        Initialisation de la classe
        """
        super().__init__(une_classe = 2, une_mana_requise = 8)

    def __str__(self):
        """
        Le retour lors de l'appel de la classe en str()

        Retour: Guérison c=...
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
        >>> mage.classe = 3
        >>> sort = SortProtection()
        >>> prev_def = cible.défense
        >>> mage.jeter_sort(sort, cible)
        >>> cible.défense == prev_def*1.5
        True
        """
        cible.bounus_défense = cible.défense * 0.5


if __name__ == "__main__":
    import doctest
    doctest.testmod()