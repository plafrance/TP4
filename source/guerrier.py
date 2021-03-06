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
        self._arme = None
        self._armure = None
        
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
        10
        
        """
        dégâts = super().calculer_dégâts(impact)
        return dégâts if self.armure is None else round(dégâts - self.armure.classe/2) 
        
    def attaquer (self):
        """
        Retourne le coefficient d'attaque d'un assaut.
        

        Retour: int,  Le coeﬃcient d’attaque d’un assaut.
        
        """
        attaque = super().attaquer()
        return attaque if self.arme is None else attaque * self.arme.classe
    
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
        10
        
        """
        dégâts = self.calculer_dégâts(impact)
        if self.armure is not None :
            self.armure.usure = self.armure.usure - (dégâts / 5)

        self._pts_vie = round(self._pts_vie - dégâts)

    @property
    def armure(self) :
        """
        Accesseur de _armure

        Retour : _armure

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
        Accesseur de _arme

        Retour : _arme

        Exemple :
        >>> from arme import Arme
        >>> guerrier = Guerrier("Bob")
        >>> arme = Arme(1)
        >>> guerrier.arme = arme
        >>> guerrier.arme == arme
        True
        
        """
        return self._arme
    
    @arme.setter
    def arme(self,une_arme):
        assert une_arme.classe <= self.classe , "Le Guerrier ne peut utiliser une arme dont la casse est plus grande que la sienne."
        self._arme = une_arme

if __name__ == "__main__":
    import doctest
    doctest.testmod()


        
