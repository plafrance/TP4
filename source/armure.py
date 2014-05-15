# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                                                               #
#               Émile Brunelle                                  #
#               Début : 13 mai 2014                             #
#               Dernière modification : 15 mai 2014             #
#               Classe Armure                                   #
#               utf-8                                           #
#               armure.py                                       #
#                                                               #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    

class Armure :
    '''
    Classe Armure qui est l'armure du guerrier

    Contient la classe, l'usure, le bonus, l'ajustement de l'usure et le nom de l'armure

    '''

    @property
    def classe(self) :
        '''
        La classe de l'armure
        '''
        return self._classe

    @property
    def usure(self) :
        '''
        Usure de l'armure en pourcentage

        Retourne l'usure de l'armure

        Par exemple :

        >>> armure = Armure(30)
        >>> print(armure.usure)
        0
        >>> armure.usure = 10
        >>> print(armure.usure)
        10
        '''
        return self._usure

    @property
    def bonus(self) :
        return 0

# --------------------- #
#                       #
#         init          #
#                       #
# --------------------- #

    def __init__(self, une_classe) :
        '''
        Si une_classe est plus petit que 0, retourne un message d'erreur

        Place usure à 0
        '''  
        assert une_classe >= 0, "La classe (une_classe) est invalide"
        self._classe = une_classe
        self._usure = 0

    def __str__(self) :
        '''
        Sert à afficher le nom de l'armure

        Retour en string du nom de l'armure

        Par exemple :

        >>> armure = Armure(5)
        >>> print(armure)
        Armure 5
        '''
        return "Armure " + str(self._classe)

    @usure.setter
    def usure(self, ajustement) :
        '''
        Mutateur de l'usure

        Paramètres :

        ajustement(int) Ajustement de l'usure de l'armure

        
        '''
        self._usure += ajustement

if __name__ == "__main__":
    import doctest
    doctest.testmod()
