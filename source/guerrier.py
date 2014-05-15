# guerrier.py
# Andrew Caron
# 13 mai 2014

from armure import Armure
from arme import Arme
from belligérant import Belligérant
from dé import Dé

class Guerrier(Belligérant):
    """
    Un Guerrier

    Attributs :
        _armure : Armure, L’armure que porte actuellement le guerrier

        _arme : Arme,  L’arme qu’utilise actuellement le guerrier
        
    """
    def __init__ (self,un_nom):
        """
        Initialise un Guerrier

        Paramètre :
            un_nom : str, le nom du guerrier

        Exemple :
        >>> Andrew = Guerrier("Andrew")
        >>> Andrew.nom
        'Andrew'
        """
        super().__init__(un_nom)
        self._force += Dé.lancer(12)
        self._défense += Dé.lancer(12)
        self._pts_vie += Dé.lancer(20) + Dé.lancer(20)
        
    def calculer_dégâts (self,impact):
        """
        Calcule le dégâts subis par le guerrier et le retourne

        Paramètre :
            impact : int, l'impact recu par le guerrier

        Retour : int, dégâts recus par le guerrier

        Exemple :
        >>> Andrew = Guerrier("Andrew")
        >>> armure = Armure(6)
        >>> Andrew.armure = armure
        >>> Andrew.calculer_dégâts(13)
        10.0
        
        """
        dégâts = super().calculer_dégâts(impact)
        return dégâts - (self.armure.classe / 2)
        
    def attaquer (self):
        """
        Retourne le coefficient d'attaque d'un assaut.
        

        Retour: int,  Le coeﬃcient d’attaque d’un assaut.
        
        """
        attaque = super().attaquer()
        return attaque * self.arme.classe
    
    def subir_dégâts (self,impact):
        """
        Soustrait au Guerrier le nombre de points de vie calculé par calculer_dégâts

        Paramètres :
           impact : int, La force d’impact de l’attaque reçue.

        Exemple :
        >>> Andrew = Guerrier("Andrew")
        >>> Andrew.pts_vie=20
        >>> armure = Armure(6)
        >>> Andrew.armure = armure
        >>> Andrew.subir_dégâts(13)
        >>> Andrew.pts_vie
        10.0
        
        """
        dégâts = self.calculer_dégâts(impact)
        self.armure.usure = self.armure.usure - (dégâts / 5)
        self._pts_vie = self._pts_vie - dégâts

    @property
    def armure(self) :
        """
        Retourne le contenue de la variable _armure

        Exemple :
        >>> from armure import Armure
        >>> guerrier = Guerrier("Bob")
        >>> armure = Armure(123)
        >>> guerrier.armure = armure
        >>> guerrier.armure == armure
        True
        
        """
        return self._armure

    @armure.setter
    def armure(self,une_armure):
        self._armure = une_armure
    
    @property
    def arme(self):
        """
        Retourne le contenue de la variable _arme

        Exemple :
        >>> from arme import Arme
        >>> guerrier = Guerrier("Bob")
        >>> arme = Arme(123)
        >>> guerrier.arme = arme
        >>> guerrier.arme == arme
        True
        
        """
        return self._arme
    
    @arme.setter
    def arme(self,une_arme):
        self._arme = une_arme

if __name__ == "__main__":
    import doctest
    doctest.testmod()


        
