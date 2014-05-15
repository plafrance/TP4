"""
sortdartdefeu.py

Jérôme Laporte
15-05-2014
"""
import dé
import sort

class SortDartDeFeu (sort.Sort):
    """
    Sort qui lance un dart de feu vers un belligérant.

    Paramètres:
		classe: int; Classe du sort (niveau)
		mana_requise: int; Nombre de manas requis pour invoquer le sort
    """
    def __init__ (self):
        """
        Constructeur de la classe SortDartDeFeu

        Exemple :
        >>> test = SortDartDeFeu()
        >>> print(test)
        Dart de feu : c=1;m=2
        """
        super().__init__(1,2)

    def __str__ (self):
        """
        Méthode str de la classe SortDartDeFeu

        Retourne :
            Une description du sort selon le format : « Dart de feu : c=1;m=2 »
        """
        return "Dart de feu : " + super().__str__()

    def activer(self, cible):
        """
        Lance le sort sur un ennemi

        Paramètre:
            cible : Belligérant, Belligérant sur lequel le sort sera lancé
        """
        attaque = dé.lancer(12)
        défense = cible.parer()
        if défense >= attaque:
            attaque_réelle = 0
        else:
            attaque_réelle = attaque - défense
        cible.subir_dégâts(attaque_réelle)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
