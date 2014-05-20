# coding : utf-8
#potion.py
#Médard Jonathas
#15/05/2014
#
#Module pour la classe potion

import item
class Potion(item.Item):
    """
    Classe abstraite représentant une potion buvable par un Belligérant.

        Propriété:
            parts: Le nombre de parts que contient la fiole de potions.
            
    """

    def __init__(self, nb_part):
        """
        Initialise la potion avec son nombre de parts.

        Paramètre:
            nb_part: nombre de parts initial de la potion.

        >>> nbparts=Potion(3)
        >>> nbparts.parts
        3
        
        """
        self._parts= nb_part
        assert self._parts > 0, "Le nombre de part ne peut être plus petit que 1"

    @property
    def parts(self):
        """
        Retourne le nombre de parts.
        """
        return self._parts

    def faire_boire(self, cible):
        """
        Fait boire la potion par un belligérant

        Paramètre:
            cible: Belligérant qui va boire la potion

        >>> nbparts=Potion(3)
        >>> nbparts.faire_boire("Guerrier")
        >>> nbparts.parts
        2
        
        """
        
        self._parts -= 1
        self.activer(cible)

    def activer(self, cible):
        """
        Méthode abstraite qui exécute l'effet de la potion sur la cible

        Paramètres:
            cible: Bélligérant qui va consommer la potion.
        
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
