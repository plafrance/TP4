#belligérant.py
#13/05/2014
#Alex Thibeault
#
#Contient la classe Belligérant qui est necessaire pour instancier un belligérant, un magoe ou un guerrier pour le tournoi pythonesque 4
from dé import Dé
from item import Item
class Belligérant:
    """
    Un belligérant capable de combattre à mains nues (et en pagne).

    Propriétés :
    nom(Type:str):Le nom du belligérant.
    pts_vies(Type:int):Le nombre de points de vie du belligérant.
    pts_vie_max(Type:int): Le nombre de point de vie maximal du belligérant.
    défense(Type:int):Le facteur de défense du belligérant. Plus ce facteur est élevé, plus le belligérant pourra résister aux attaques.
    force(Type:int):Le facteur de force du belligérant. Plus ce facteur est élevé, plus les attaques du belligérant seront efficaces.
    items(Type:Ensemble d'Items): Ensemble d'Items que possède le Belligérant.
    
    """
    def __init__(self,un_nom):
        """
        Initialise un belligérant. 
        
        Paramètre:
        un_nom(Type:str):Nom qui sera attibué au belligérant.

        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.nom
        'Alex'
        """
        assert un_nom!=None or un_nom.trim()!="","Le nom du béligérant ne peut pas être vide"
        self._nom=un_nom.strip()
        self._force=Dé.lancer(12)
        self._défense=Dé.lancer(12)
        self._pts_vie=Dé.lancer(12)+Dé.lancer(12)+20
        self._pts_vie_max=self.pts_vie
        self._items=[]
        self._classe=1
        self._bonus_défense=0.0

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
        Calcule le coefficient d’attaque d’un assaut.
        
        Retour: Le coefficient d’attaque d’un assaut calculé (force+ un dé 12).
        """
        return self.force+Dé.lancer(12)

    def parer(self):
        """
        Calcule le coefficient de parade lors d’un assaut.
        
        Retour:Le coefficient de parade lors d’un assaut calculé par la formule (défense+ deux dé 6).
        """
        return self.défense+Dé.lancer()+Dé.lancer()
        
    def calculer_dégâts(self,impact):
        """
        Calcule le dégât subis par le belligérant (l'impact dans le cas échéant).
        
        Retour:l'impact de l'assaut.

        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.calculer_dégâts(13)
        13
        """
        return impact

    def subir_dégâts(self,impact):
        """
        Après avoir reçu une attaque, cette méthode calcule les dégâts subis 
        par le belligérant et les déduit de ses points de vie selon la formule(pts_vie-dégâts).
        
        Paramètre:
        impact(Type:int):La force d'impact de l'attaque reçue.

        Retour: le dégâts subi.
        
        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.pts_vie=20
        >>> Alex.subir_dégâts(15)
        15
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
        return  self.pts_vie<=0
            
    def prendre_item(self,un_item):
        """
        Ajoute un item à ceux que possède le Belligérant. Le poids total de ses items ne peut excéder 5Kg par point de force.
        
        Paramètre:
        -un_item(Type:Item): l'item à ajouter aux items du belligérant.
        
        Exemple:
        >>> Excalibur=Item(4999)
        >>> Alex=Belligérant("Alex")
        >>> Alex.prendre_item(Excalibur)
        >>> Alex.items[0] is Excalibur
        True

        """
        assert sum([x.poids for x in self.items])+un_item.poids<5000*self.force, "L'item est trop lourd pour être ajouté au Belligérant."
        self.items.append(un_item)

    def jeter_item(self,un_item):
        """
        Retire un item de la liste d'items détenus pas le Belligérant.
        
        Paramètre:
        -un_item(Type:Item):L'item à enlever.
        
        Exemple:
        >>> Excalibur=Item(4999)
        >>> Alex=Belligérant("Alex")
        >>> Alex.prendre_item(Excalibur)
        >>> Alex.jeter_item(Excalibur)
        >>> len(Alex.items)==0
        True
        """
        assert un_item in self._items,"L'item n'existe pas."
        self.items.remove(un_item)  

    @property
    def nom(self):
        """
        Accesseur de self._nom
        
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
        Accesseur de self._pts_vie
        
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
        Mutateur de pts_vie

        Paramètre:
        -un_nombre(type:int):la nouvelle valeur de pts_vie.
        
        """
        self._pts_vie=un_nombre

    @property
    def pts_vie_max(self):
        """
        Accesseur de pts_vie_max
        
        Retour: Les points de vie max du belligérant
        """
        return self._pts_vie_max

    @property
    def défense(self):
        """
        Accesseur de défense

        Retour: Le facteur de défense du belligérant.
        """
        return self._défense+self._bonus_défense

    @property
    def force(self):
        """
        Accesseur de force
        
        Retour: Le facteur de force du belligérant.
        """
        return self._force

    @property 
    def classe(self):
        """
        Accesseur de classe
        
        Retour: Le niveau du personnage 
        """
        return self._classe

    @classe.setter
    def classe(self,une_classe):
        """
-        Mutateur de classe
        
        Paramètre:
        -une_classe(Type:int):La nouvelle classe de l'attribut classe.
        """
        self._classe=une_classe
    
    @property
    def items(self):
        """
        Acceseur de items
        
        Retour: La liste d'items
        """
        return self._items

    @property
    def bonus_défense(self):
        """
        Accesseur de bonus_défense

        Retour: Le bonus de défense
        """
        return self._bonus_défense

    @bonus_défense.setter
    def bonus_défense(self,un_bonus_défense):
        """
        Mutateur de bonus_défense

        Paramètre:
        -un_bonus_défense(float): le bonus de défense
        
        Exemple:
        >>> Alex=Belligérant("Alex")
        >>> Alex.bonus_défense(6.5)
        >>> Alex.défense==Alex._défense+6.5
        True
        """
        self._bonus_défense=un_bonus_défense

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
