# coding: utf-8

#sortguérison.py
#Médard Jonathas
#13/05/2014
#
#Module pour la classe guérison

import sort
from dé import Dé

class SortGuérison(sort.Sort):
    """
    Sort qui permet d'augmenter le nombre de points de vie d'un belligérant
            
    """

    def __init__(self):
        """
        Initialise le Sort avec sa classe (1) et sa mana (4).
        
        """
        super().__init__(1,4)
        

    def __str__(self):
        """
        Fournit une représentation en chaîne de caractères du Sort.

        Exemple:
        >>> objet_test=SortGuérison()
        >>> objet_test.__str__()
        'Guérison: c=1;m=4'
        
        """

        return "Guérison: " + super().__str__()

    def activer(self, cible):
        """
        Sort qui permet d'augmenter le nombre de point de vie d'un belligérant

        Paramètres:
            cible: Type Belligérant. Cible qui sera affecté par le sort.

        Exemple:
        >>> import guerrier
        >>> cible = guerrier.Guerrier("biab")
        >>> vie=cible.pts_vie
        >>> sort=SortGuérison()
        >>> sort.activer(cible)
        >>> cible.pts_vie > vie
        True
        
        """
        #Le dé determine le nb de points de guérison
        pts_guérison= Dé.lancer(20)
        
        # Si la cible a plus que 0 points de vie alors il recoit les pts de guérison détermniné par le dé
        if cible.pts_vie > 0:
            cible.pts_vie += pts_guérison


if __name__ == "__main__":
    import doctest
    doctest.testmod()
            
        
