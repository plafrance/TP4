# -*- coding: utf-8 -*-
#Frédérik Dumulong\Benjamin Bradley-Roy
#Classe Sort et ses attributs
#
class Sort:
    """
    Les différents sorts pouvant être lancés par le mage

    Propriétés:
    une_mana_requise:int,la quantité de mana nécessaire pour lancer le sort
    une_classe:int, la classe du sort, représentant sa difficulté à l'utiliser.

    Exemples:
    >>> print(Sort(1,6))
    c=1;m=6
    
    >>> print (Sort(3,5))
    c=3;m=5
    
    >>> b = Sort(5,6)
    >>> print(b.mana_requise)
    6

    >>> b = Sort(5,6)
    >>> print(b._classe)
    5
    
    """

    def __init__(self,une_classe,une_mana_requise):#Définition des variables à utiliser pour chaque sort
        self._classe = une_classe
        self._mana = une_mana_requise

    def __str__(self):#Retourne les valeurs propres à chaque sort
        return "c="+str(self._classe)+";"+"m="+str(self._mana)

    def activer(self,cible):
        pass

    @property #Propriété propre de la mana
    def mana_requise(self):
        return self._mana

    @property #Propriété propre d'une classe
    def classe(self):
        return self._classe

if __name__ == "__main__":
    import doctest
    doctest.testmod()
