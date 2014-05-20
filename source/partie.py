class Partie:
    _la_partie = None

    def __new__(cls, *args, **kwargs):
        if not cls._la_partie:
            cls._la_partie = super(Partie, cls).__new__(
                                cls, *args, **kwargs)
        return cls._la_partie
            

    def la_partie():
        """
        Accesseur du singleton la_partie

        Exemple : 
        >>> Partie.la_partie() is Partie.la_partie()
        True
        >>> Partie() is Partie.la_partie()
        True
        """
        return Partie()

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
