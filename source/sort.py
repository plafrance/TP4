# -*- coding: utf-8 -*-
#Frédérik Dumulong\Benjamin Bradley-Roy
#Classe Sort et ses attributs
#15/05/2014
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
>>> print(b.classe)
5
"""
    
    def __init__(self,une_classe,une_mana_requise):#Définition des variables à utiliser pour chaque sort
        """
        Variables présentes dans la fonction Sort, à utiliser par les sous-classes

        Retourne les variables de mana requises et la classe du sort spécifique
        """
        self._classe = une_classe
        self._mana = une_mana_requise

    def __str__(self):#Retourne les valeurs propres à chaque sort
        """
        Variables affichés à l'écran pour désigner la mana requise et la classe

        Retourne les attributs sous formes de chaînes de caractères
        
        """
        return "c="+str(self._classe)+";"+"m="+str(self._mana)

    def activer(self,cible):
        """
        Action d'activer le sort via les sous-classes utilisant Sort,pour cibler un objet de type Belligérant

        Retourne la variable pour l'utilisation des différents sorts prenant pour cible un Belligérant
        """
        pass

    @property #Propriété propre de la mana
    def mana_requise(self):
        """
        Variable de la mana requise pour lancer un sort spécifique

        Propriété:
        mana:int,mana nécessaire pour lancer le sort
        

        Exemples:
        >>> b = Sort(7,9)
        >>> print(b.mana_requise)
        9
        """
        return self._mana

    @property #Propriété propre d'une classe
    def classe(self):
        """
        Variable de la classe du sort utilisé

        Propriété:
        classe:int,numéro correspondant à la classe du sort

        Exemples:
        >>> b = Sort(7,9)
        >>> print(b.classe)
        7
        """
        return self._classe

if __name__ == "__main__":
    import doctest
    doctest.testmod()
