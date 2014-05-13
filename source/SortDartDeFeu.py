import Dé
import Belligérant

class SortDartDeFeu (Sort):
    """
    Sort qui lance un dart de feu vers un belligérant.

    Méthode :
        __init__ : SortDartDeFeu, Constructeur du sort
        activer : int, Retourne la puissance d'attaque du sort
    """
    def __init__ (self, une_classe, une_mana_requise):
        """
        Constructeur de la classe SortDartDeFeu

        Paramètre :
            une_classe : int, Niveau de puissance du sort
            une_mana_requise : int, Nombre de manas que requiert le sort pour être lancé

        Exemple :
        >>> test = SortDartDeFeu()
        >>> print(test)
        Dart de Feu C=1; M=2
        """
        super().__init__(1,2)

    def __str__ (self):
        """
        Méthode str de la classe SortDartDeFeu

        Retourne :
            Une description du sort selon le format : « Dart de feu : C=1; M=2 »
        """
        return "Dart de feu : " + super().__str__()

    def activer(self, cible):
        """
        Lance le sort sur un ennemi

        Attributs :
            cible : Belligérant, Belligérant sur lequel le sort sera lancé
        """
        attaque = Dé.lancer(12)
        défense = cible.parer()
        if défense >= attaque:
            attaque_réelle = 0
        else:
            attaque_réelle = attaque - défense
        cible.subir_dégâts(attaque_réelle)

if __name__ == "__main__":
    import doctest
    doctest.testmod()