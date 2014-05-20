class Partie:
    _la_partie = None

def __new__(cls, *args, **kwargs):
        if not cls._la_partie:
            cls._la_partie = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._la_partie
            
