#belligérant.py
#07/05/2104
#Alex Thibeault                                            et peut-être Billy? QUI SAIT!
#
#Contient la classe Belligérant qui est necessaire pour instancier un belligérant, un magoe ou un guerrier pour le tournoi pythonesque 4
from dé import Dé
class Belligérant:
    """
    Un belligérant capable de combattre à mains nues (et en pagne).

    Propriétés:
    _nom:Le nom du belligérant.
    _pts_vies:Le nombre de points de vie du belligérant.
    _défense:Le facteur de défense du belligérant. Plus ce facteur est élevé, plus le belligérant pourra résister aux attaques.
    _force:Le facteur de force du belligérant. Plus ce facteur est élevé, plus les attaques du belligérant seront efficaces.
    
    """
    def __init__(self,un_nom):
        """
        Initialise un belligérant. 
        
        Paramètre:
        un_nom:Nom qui sera attibué au belligérant.

        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.nom
        'Alex'
        """
        assert un_nom!=None or un_nom.trim()!="","Le nom du béligérant ne peut pas être vide"
        self._nom=un_nom
        self._force=Dé.lancer(12)
        self._défense=Dé.lancer(12)
        self._pts_vie=Dé.lancer(12)+Dé.lancer(12)+20
    
    def __str__(self):
        """
        Fournit une chaîne de caractère représentant le belligérant.

        Retour: Une chaîne représentant le belligérant de la forme <<nom (F:force D:défense V:pts_vie)>>
        """
        return self.nom+" (F:"+self.force+" D:"+self.défense+" V:"+self.pts_vie+")"
 
    def attaquer(self):
        """
        Calcule le coefficient d’attaque d’un assaut par la formule.
        
        Retour: Le coefficient d’attaque d’un assaut calculé.
        """
        return self.force+Dé.lancer(12)

    def parer(self):
        """
        Calcule le coefficient de parade lors d’un assaut.
        
        Retour:Le coefficient de parade lors d’un assaut calculé par la formule.
        """
        return self.défense+Dé.lancer()+Dé.lancer()
        
    def calculer_dégâts(self,impact):
        """
        Calcule le dégât subis par le belligérant.
        """
        return impact

    def subir_dégâts(self,impact):
        """
        Après avoir reçu une attaque, cette méthode calcule les dégâts subis 
        par le belligérant et les déduit de ses points de vie selon la formule.
        
        Paramètre:
        impact:La force d'impact de l'attaque reçue.
        """
        self.pts_vie=self.pts_vie-calculer_dégâts(impact)

    def est_mort(self):
        """
        détermine si un belligérant est mort.
        
        Retour:Vrai si et si seulement si pts_vie est 0 ou moins.
        """
        if self.pts_vie<=0:
            return True
        else:
            return False
        
    @property
    def nom(self):
        """
        Acceseur de self._nom
        
        Retour: Le nom du belligérant.
        """
        return self._nom
        
    @property
    def pts_vie(self):
        """
        Acceseur de self._pts_vie
        
        Retour: Le nombre de points de vie du belligérant.
        """
        return self._pts_vie

    @pts_vie.setter
    def pts_vie(self,un_nombre):
        """
        Mutateur de self._pts_vie
        """
        self._pts_vie=un_nombre

    @property
    def défense(self):
        """
        Acceseur de self._défense

        Retour: Le facteur de défense du belligérant.
        """
        return self._défense

    @property
    def force(self):
        """
        Acceseur de self._force
        
        Retour: Le facteur de force du belligérant.
        """
        return self._force

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
