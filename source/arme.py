####################################
#      -*- encoding:utf-8 -*-      #
#arme.py                           #
#Dan Doroga&Alex Thibeault         #
#2014/05/13                        #
#Ce module contient la classe Arme.#
####################################

class Arme():

    ####################
    #                  #
    #    Propriétés    #
    #                  #
    ####################
    
    @property
    def classe(self):
        """
        La classe de l’arme.

        Exemple:
        >>> Épée = Arme(1)
        >>> print(Épée.classe)
        1
        """
        return self._classe
    @property
    def bonus(self):
        """
        Le bonus d’attaque accordé par l’arme.
        """
        return self._bonus

    ####################
    #                  #
    #   Constructeur   #
    #                  #
    ####################
    
    def __init__(self,une_classe):
        """
        Initialise une Arme avec sa classe.

        Paramètres :
            une_classe -> int, La classe de l'arme.
        """
        assert une_classe >= 0, "La classe (" + str(une_classe) + ") est invalide"
        self._classe=une_classe
        
    ####################
    #                  #
    #     Méthodes     #
    #                  #
    ####################
        
    def __str__(self):
        """
        Retourne une représentation en chaîne de caractère de l’arme.
        """
        return "Type d’arme (" + str(self.classe) + ")"
    def bonus(self):
        """
        Le bonus d’attaque accordé par l’arme.
        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
