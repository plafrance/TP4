# -*- encoding:utf-8 -*-
#SortProtection.py
#Gilbert Paquin
#2014/05/13
#
# Sort de protection
import sort
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
        return "SortProtection: c=%i,c=%i" % (super().classe, super().mana_requise)

    """
    Active le sort qui agit alors sur sa cible. Il augmente
    la défense du belligérant de 50%.
    — Paramètres :
    (i) cible (Belligérant) : Le belligérant ciblé par le sort.

    Exemple
    >>> cible = Guerrier("Patrick Lafrance")
    >>> mage = Mage("Émile Brunelle")
    >>> sort = SortProtection()
    >>> prev_def = cible.défense
    >>> mage.jeter_sort(sort, cible)
    >>> cible.défense == prev_def*1.5
    """
    def activer(self, cible = Billigérant):
        cible.défense += cible.défense * 1.5