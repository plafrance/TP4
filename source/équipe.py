#équipe.py
#13/05/2014
#Alexandre Lambert
#
#Contient la classe Équipe pour faire une équipe de belligérant

class Équipe :
    def __init__( self , un_nom ):
        """
        Initialise une équipe avec un nom mais sans belligérants immédiatement.
        Exemples:
        >>> équipe1 = Équipe("Toto")
        >>> équipe1.nom
        'Toto'
        """
        self._nom = un_nom
        self._combattants = []

    def __len__( self ):
        """

        Retourne le nombre d’éléments dans l’équipe. 
       
        Retour : Le nombre de belligérants dans l’équipe


        >>> from belligérant import Belligérant
        >>> équipe_test = Équipe("Toto")
        >>> Bob = Belligérant("Bob")
        >>> Boby = Belligérant("Boby")
        >>> équipe_test.ajouter_belligérant(Bob)
        >>> équipe_test.ajouter_belligérant(Boby)
        >>> len(équipe_test)
        2
        """
        return len(self._combattants)

    def ajouter_belligérant( self , un_belligérant ):
        """
        Ajoute un belligérant dans une équipe

        """
        self._combattants += [un_belligérant]

    
    def belligérant( self , indice : int = None , nom : str = None):
        """
        Vérifie si un combattant est présent dans l'équipe

        Paramètre :
            indice : indice d'un belligérant dans l'équipe
            nom : nom d'un belligérant

        retourne le belligérant si l'indice est présent
        retourne le belligérant si le nom est dans la liste de belligérant

        Exemple:
        >>> from belligérant import Belligérant
        >>> équipe_test = Équipe("Toto")
        >>> Bob = Belligérant("Bob")
        >>> équipe_test.ajouter_belligérant(Bob)
        >>> équipe_test.belligérant( None , "blablablablabla")
        Traceback (most recent call last):
        AssertionError: «nom ' { blablablablabla }' est invalide»
        >>> équipe_test.belligérant( 4578 )
        Traceback (most recent call last):
        AssertionError: «indice { 4578 } invalide»
        >>> équipe_test.belligérant()
        >>> équipe_test.belligérant( nom = "Bob" ) == Bob
        True
        """
        if nom == None and indice == None:
            return None

        assert (indice != None and indice < len(self._combattants)) or nom, "«indice { " + str(indice) + " } invalide»"
        assert(nom in [un_combattant.nom for un_combattant in self._combattants]), "«nom ' { " + nom + " }' est invalide»"

        if indice != None :
            return self._combattants[indice]
        if nom != None :
            for un_combattant in self._combattants:
                if un_combattant.nom == nom :
                    return un_combattant
    @property
    def nom( self ):
        """
        Accesseur de self.nom

        retourne self.nom
        """
        return self._nom

if __name__ == "__main__":
    import doctest
    doctest.testmod()
