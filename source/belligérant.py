#belligérant.py
#13/05/2014
#Alex Thibeault
#
#Contient la classe Belligérant qui est necessaire pour instancier un belligérant, un magoe ou un guerrier pour le tournoi pythonesque 4
from dé import Dé
class Belligérant:
    """
    Un belligérant capable de combattre à mains nues (et en pagne).

    Propriétés:
    _nom:Le nom du belligérant.
    _pts_vies:Le nombre de points de vie du belligérant.
    _pts_vie_max: Le nombre de point de vie maximal du belligérant.
    _défense:Le facteur de défense du belligérant. Plus ce facteur est élevé, plus le belligérant pourra résister aux attaques.
    _force:Le facteur de force du belligérant. Plus ce facteur est élevé, plus les attaques du belligérant seront efficaces.
    _items: Ensemble d'Items que possède le Belligérant.
    
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
        self._pts_vie_max=self.pts_vie
        self._items=[]
        self._classe=1

    def __str__(self):
        """
        Fournit une chaîne de caractère représentant le belligérant.

        Retour: Une chaîne représentant le belligérant de la forme <<nom (F:force D:défense V:pts_vie)>>
        
        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> str_test=Alex.nom+" (F:"+str(Alex.force)+" D:"+str(Alex.défense)+" V:"+str(Alex.pts_vie)+")"
        >>> str_test==str(Alex)
        True
        """
        return self.nom+" (F:"+str(self.force)+" D:"+str(self.défense)+" V:"+str(self.pts_vie)+")"
 
    def attaquer(self):
        """
        Calcule le coefficient d’attaque d’un assaut par la formule(self.force+Dé.lancer(12) par défaut).
        
        Retour: Le coefficient d’attaque d’un assaut calculé.
        """
        return self.force+Dé.lancer(12)

    def parer(self):
        """
        Calcule le coefficient de parade lors d’un assaut(self.défense+Dé.lancer()+Dé.lancer() par défaut).
        
        Retour:Le coefficient de parade lors d’un assaut calculé par la formule.
        """
        return self.défense+Dé.lancer()+Dé.lancer()
        
    def calculer_dégâts(self,impact):
        """
        Calcule le dégât subis par le belligérant.

        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.calculer_dégâts(13)
        13
        """
        return impact

    def subir_dégâts(self,impact):
        """
        Après avoir reçu une attaque, cette méthode calcule les dégâts subis 
        par le belligérant et les déduit de ses points de vie selon la formule.
        
        Paramètre:
        impact:La force d'impact de l'attaque reçue.

        Retour: le dégâts subi.
        
        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.pts_vie=20
        >>> Alex.subir_dégâts(15)
        >>> Alex.pts_vie
        5
        """
        dégâts=self.calculer_dégâts(impact)
        self.pts_vie=self.pts_vie-dégâts
        return dégâts

    def est_mort(self):
        """
        détermine si un belligérant est mort.
        
        Retour:Vrai si et si seulement si pts_vie est 0 ou moins.

        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.est_mort()
        False
        >>> Alex.pts_vie=0
        >>> Alex.est_mort()
        True
        """
        if self.pts_vie<=0:
            return True
        else:
            return False
            
    def prendre_item(self,un_item):
        """
        Ajoute un item à ceux que possède le Belligérant. Le poids total de ses items ne peut excéder 5Kg par point de force.
        
        Paramètre:
        -un_item: l'item à ajouter aux items du belligérant.
        
        Exemple:
        A FAIRE 
        ATTENDRE MODULE ITEM
        """
        assert sum([x.poids for x in self.items])+un_item.poids<5, "L'item est trop lourd pour être ajouté au Belligérant."
        self.items+=[un_item]

    def jeter_item(self,un_item):
        """
        Retire un item de la liste d'items détenus pas le Belligérant.
        
        Paramètre:
        -un_item:L'item à enlever.
        
        Exemple:
        A FAIRE 
        ATTENDRE LE MODULE ITEM
        """
        assert [x for x in self.items]==un_item,"L'item n'existe pas."
        self.items.remove(un_item)                

    @property
    def nom(self):
        """
        Acceseur de self._nom
        
        Retour: Le nom du belligérant.

        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.nom
        'Alex'
        """
        return self._nom
        
    @property
    def pts_vie(self):
        """
        Acceseur de self._pts_vie
        
        Retour: Le nombre de points de vie du belligérant.
        >>> Alex=Belligérant("Alex")
        >>> Alex.pts_vie=10
        >>> Alex.pts_vie
        10
        """
        return self._pts_vie

    @pts_vie.setter
    def pts_vie(self,un_nombre):
        """
        Mutateur de self._pts_vie
        """
        self._pts_vie=un_nombre

    @property
    def pts_vie_max(self):
        """
        Accesseur de self._pts_vie_max
        
        Retour: Les points de vie max du belligérant
        """
        return self._pts_vie_max

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

    @property 
    def classe(self):
        """
        Accesseur de self._classe
        
        Retour: Le niveau du personnage 
        """
        return self._classe

    @classe.setter
    def classe(self,une_classe):
        """
        Mutateur de self._classe
        """
        self._classe=une_classe


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
