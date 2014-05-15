# -*- encoding:utf-8 -*-
# Benjamion Bradley roy
#Module item

class Item():#Retourne un entier sous forme de gramme

    def __init__(self,un_poids,une_valeur):
        """
        Constructeur

        paramètre:
        un_poids: un entier représentant le poids.
        valeur: représentant une valeur. 
        """

        self._poids = un_poids
        self._valeur = une_valeur


    def __str__(self):
        """
        retourne « self._poids » en objet str.

        Exemple:
        >>> démonstration = Item(5,7)
        >>> print(démonstration)
        P = 5
        """
        

        return "P = " + str(self._poids)
    @property
    def poids(self):
        """
        retourne le poids seul.

        Exemple:
        >>> démonstration = Item(5,7)
        >>> print(démonstration.poids)
        5
        """
        return str(self._poids)

    @property
    def valeur(self):
        """
        retourne la valeur seul.

        Exemple:
        >>> démonstration = Item(5,7)
        >>> print(démonstration.valeur)
        7

        >>> démonstration = Item(5,7)
        >>> démonstration.valeur = 9
        >>> print(démonstration.valeur)
        9
        
        """
        return str(self._valeur)

    @valeur.setter
    def valeur(self,une_valeur):
        
        self._valeur = une_valeur


if __name__ == "__main__":
    import doctest
    doctest.testmod()
