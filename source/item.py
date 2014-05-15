# -*- encoding:utf-8 -*-
# Benjamion Bradley roy
#Module item

class Item():#Retourne un entier sous forme de gramme

    def __init__(self,un_poids):
        """
        Constructeur

        paramètre:
        un_poids: un entier représentant le poids.
        """

        self._poids = un_poids


    def __str__(self):
        """
        retourne « self._poids » en objet str.

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
        return str(self._poids)

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
