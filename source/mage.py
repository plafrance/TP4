# -*- coding:utf-8 -*-
# Mage.py
# Billy Chamberland
# 2014-05-13
# Module du Mage et toutes ses fonctions
#
from belligérant import Belligérant
from dé import Dé
from sort import Sort
class Mage(Belligérant) :
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

        Propriétés :
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
        >>> un_mage = Mage("Merlin")
        >>> print(un_mage.sorts)
        []
        """
        return self._sorts
    @sorts.setter
    def sorts ( self, ajout_sort) :
        """
        Mutateur de _sorts
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
    def jeter_sort ( self , sort, cible) :
        """
        Jete un sort vers une cible

        Paramètres :
            un_sort : Sort, sort lancé vers la cible
            cible : Belligérant, cible du sort
        """
        assert self.puissance > un_sort.classe,\
               "Puissance ("+str(self.puissance)+") <"\
               " un_sort.classe ("+strun_sort.classe+")"
        assert self.mana >= un_sort.mana_requise,\
               "Mana ("+mana+") < un_sort.mana_requise"\
               "("+un_sort.mana_requise+")"

        sort.activer(cible)
        self.mana(self.mana-sort.mana_requise)
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
        Exemples :
        >>> un_mage = Mage("Merlin")
        >>> print(un_mage.sorts)
        []
        >>> un_sort = SortDartDeFeu()
        >>> un_mage.sorts(un_sort)
        >>> print(un_mage.sorts)
        [Dart de feu]

        """
        assert sort != item in self.sorts,\
               "Le sort ("+str(sort)+") existe déjà"
        sorts(sort)
        return
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

