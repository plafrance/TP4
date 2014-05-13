# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                                                               #
#               Émile Brunelle                                  #
#               Début : 13 mai 2014                             #
#               Dernière modification : 13 mai 2014             #
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
        return self._classe

    @property
    def usure(self) :
        '''
        Usure de l'armure en pourcentage

        Retourne l'usure de l'armure
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
        self._classe = une_classe
        self._usure = 0

    def __str__(self) :
        '''
        Sert à afficher le nom de l'armure

        Retour en string du nom de l'armure
        '''
        
        return "Armure" + str(self._classe)

    @usure.setter
    def usure(self, ajustement) :
        '''
        Retour ajustement de l'usure
        '''
        self._usure += ajustement

if __name__ == "__main__":
    import doctest
    doctest.testmod()
