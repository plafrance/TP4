# -*- coding:utf-8 -*-
# mage.py
# Billy Chamberland
# 2014-05-13
# Module du Mage et toutes ses fonctions
#
from belligérant import Belligérant
from dé import Dé
from sort import Sort

class Mage(Belligérant):
    """
    Un belligérant de type mage capable de jeter des sorts.

    Propriétés :
        _puissance : int, La puissance du Mage.
        _mana : int, La quantité d'énergie magique que possède le Mage.
        _sorts : list, Liste des sorts que possède le Mage.

    """
    def __init__ ( self, un_nom):
        """
        Initialise un Mage. Sa puissance est donnée par un dé6
        et sa mana par 2xDé20. Initialement, il ne possède aucun sort.

        Paramètre :
            un_nom : str, nom du belligérant de type mage.

        Exemples :
        >>> Merlin = Mage("Merlin")
        >>> print(Merlin.nom)
        Merlin
        """
        super().__init__(un_nom)
        self._puissance = Dé.lancer(6)
        self._mana = Dé.lancer(20) + Dé.lancer(20)
        self._sorts = []
    @property
    def puissance ( self ) :
        """
        Accesseur de _puissance
        Retour : _puissance
        """
        return self._puissance
    @puissance.setter
    def puissance ( self, ajustement ) :
        """
        Mutateur de _puissance

        Paramètre :
            ajustement : int, nouvelle puissance
        Exemples :
        >>> un_mage = Mage("Merlin")
        >>> un_mage.puissance(3)
        >>> print(un_mage.puissance)
        3
        
        """
        self._puissance = ajustement
    @property
    def mana ( self ) :
        """
        Accesseur de _mana
        Retour : _mana
        """
        return self._mana
    @mana.setter
    def mana ( self , ajustement ) :
        """
        Mutateur de _mana

        Paramètre :
            ajustement : int, mana après réduction
        Exemples :
        >>> un_mage = Mage("Merlin")
        >>> un_mage.mana(30)
        >>> print(un_mage.mana)
        30
        """
        self._mana = ajustement
    @property
    def sorts ( self ) :
        """
        Accesseur de _sorts
        Retour : _sorts
        Exemples :
        >>> from mage import Mage
        >>> un_mage = Mage("Merlin")
        >>> print(un_mage.sorts)
        []
        """
        return self._sorts
    @sorts.setter
    def sorts ( self, ajout_sort) :
        """
        Mutateur de _sorts

        Paramètre :
            ajout_sort : Sort, nouveau sort à ajouter
        Exemples :
        >>> un_mage = Mage("Merlin")
        >>> print(un_mage.sorts)
        []
        >>> un_sort = SortDartDeFeu()
        >>> un_mage.sorts(un_sort)
        >>> print(un_mage.sorts)
        [Dart de feu]
        """
        self._sorts.append(ajout_sort)
    def jeter_sort ( self , un_sort, cible) :
        """
        Jete un sort vers une cible

        Paramètres :
            un_sort : Sort, sort lancé vers la cible
            cible : Belligérant, cible du sort
        """
        assert self.puissance > un_sort.classe,\
               "Puissance ("+str(self.puissance)+") <"\
               " un_sort.classe ("+str(un_sort.classe)+")"
        assert self.mana >= un_sort.mana_requise,\
               "Mana ("+str(self.mana)+") < un_sort.mana_requise"\
               "("+str(un_sort.mana_requise)+")"

        un_sort.activer(cible)
        self.mana= self.mana-un_sort.mana_requise
        def parer ( self ) :
            """
            Calcule le coefficient de parade lors d’un assaut. Puisque
            le Mage est plus agile que le Belligérant moyen, son coefficient
            est 10% par point de puissance de plus que celui calculé
            par Belligérant.parer.

            Retour : coefficient de parade lors d'un assaut d'un mage
            """
            base_parer = super().parer()
            return round(base_parer + base_parer* 0.1 * self.puissance)
        
    def ajouter_sort( self, sort):
        """
        Ajoute un sort à la liste des sorts connus par le Mage.

        Paramètre :
            sort : Sort, sort à ajouter.
        Exemples :
        >>> from sortdartdefeu import SortDartDeFeu
        >>> un_mage = Mage("Merlin")
        >>> print(un_mage.sorts)
        []

        """
        assert sort != item in self.sorts,\
               "Le sort ("+str(sort)+") existe déjà"
        self._sorts += [sort]
        return
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()


