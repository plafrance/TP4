#SortGuérison.py
#Médard Jonathas
#13/05/2014
#
#Module pour la classe guérison

import Sort
import dé

class SortGuérison(Sort):
    """
    Sort qui permet d'augmenter le nombre de points de vie d'un belligérant

    Hérite de sort
        Attributs hérités:
            classe: Entier qui représente la classe du sort
            mana_requise: Entier qui représente la quantité de mana requise par le sort
            
    """

    def __init__(self):
        super().__init__(1,4)
        

    def __str__(self):

        return "Guérison:" + super().__str__()

    def activer(self, cible):
        """
        Sort qui permet d'augmenter le nombre de point de vie d'un belligérant

        Paramètres:
            cible: Type Belligérant. Cible qui sera affecté par le sort.

        Exemple:

        >>> cible = Guerrier("biab")
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
        
            
            
                
                
            
        
