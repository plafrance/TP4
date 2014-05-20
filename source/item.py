# -*- encoding:utf-8 -*-
# Benjamion Bradley roy
# 20 mai 2014
# Module item

class Item:
    """
    Retourne un objet poig(gramme).
    """

    def __init__(self,un_poids):
        """
        Constructeur

        paramètre:
        un_poids: un entier représentant le gramme.
        """

        self._poids = un_poids


    def __str__(self):
        """
        retourne le poig sous format p = un entier

        Exemple:
        >>> démonstration = Item(5)
        >>> print(démonstration)
        P = 5
        """
        

        return "P = " + str(self._poids)
    @property
    def poids(self):
        """
        retourne le poids seul.

        Exemple:
        >>> démonstration = Item(5)
        >>> print(démonstration.poids)
        5
        """
        return self._poids

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
