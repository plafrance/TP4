#partie.py
#13/05/2014
#Alex Thibeault, Dan Doroga et BillyGérantDuMaxi
#
#Une partie de Tournoi Pythonesque 4 entre deux ou plusieurs joueurs.
from random import randint

class Partie:
    _la_partie = None

    def __init__(self, les_joueurs, nb_belligérants):
        """
        Initialise la partie.
        """
        assert len(les_joueurs) > 1, "Il n'y a pas suffisamment de joueurs."
        self._joueurs = les_joueurs
        self._tour = 0
        self._premier_joueur = randint(0,len(les_joueurs)-1)
        self._items_épars = []
        self._nb_belligérants_par_équipe = nb_belligérants

    def populer_équipes(self):
        """
        Permet de créer tous les belligérants de toutes les équipes. Tour à tour,chaque joueur est invité à créer son belligérant. Le joueur qui commencer est choisi au hasard.
        
        """
        i = self._premier_joueur
        for j in range (0,self._nb_belligérants_par_équipe):
            #la première boucle s'assure d'ajouter tout les belligérant
            for k in range (0,len(self.joueurs)):
                #le deuxième boucle parcoure la liste de joueur
                self.créer_belligérant(self.joueurs[i])
                i = (i+1)%len(self.joueurs)

    def créer_belligérant(self,un_joueur):
        un_joueur.créer_belligérant()

    def jouer_tour(self):
        """
           Joue un tour de jeu. Tous les joueurs, à tour de rôle jouent leur tour.
        """
        i = self._premier_joueur
        for j in range (0,len(self.joueurs)):
            self.joueurs[i].jouer()
            i = (i+1)%len(self.joueurs)
        
    def __new__(cls, *args, **kwargs):
        if not cls._la_partie:
            cls._la_partie = super().__new__(cls)
        return cls._la_partie
            

    def la_partie():
        """
        Accesseur du singleton la_partie

        Exemple :
        >>> Partie.la_partie() is Partie.la_partie()
        True
        >>> #Partie() is Partie.la_partie()
        True
        """
        return Partie._la_partie

    def démarrer_partie  ( self ) :
        while len([x for x in self.joueurs if not x.équipe.est_éliminée()])> 1:
            self.jouer_tour()

    def répartir_items ( self ) :
        tour_joueur = self._premier_joueur
        liste_joueurs = self.joueurs
        while len(self._items_épars) > 0 and len(liste_joueurs) > 0 :
            for i in range (0,len(self.joueurs)-1):
                poid_min_requis=calculer_minimum_poid_requis(self._items_épars)
                belligérants_dispos = belligérants_disponibles(self.joueurs[tour_joueur].équipe,poid_min_requis)
                if len(belligérants_dispos) != 0 :
                    belligérant_choisi = self.liste_joueurs[tour_joueur].choisir(belligérants_dispos)
                    items_dispos = items_disponibles(belligérant_choisi,self._items_épars)
                    item_choisi = self.liste_joueurs[tour_joueur].choisir(items_dispos)
                    belligérant_choisi.prendre_item(item_choisi)
                else :
                    liste_joueurs.remove(self.joueurs[tour_joueur])
                tour_joueur = (tour_joueur+1)%len(liste_joueurs)

                    

    def belligérants_disponibles ( une_équipe, poid_requis) :
        """
            Permet de connaître tous les belligérants pouvant équiper le plus léger des items restants

            Retour : liste des belligérants qui peuvent équiper l'item le plus léger restant
        """
        belligérants_dispo = []
        total_poid_item = 0
        for x in une_équipe.combattants:
            for y in x.item :
                total_poid_item += y.poids
            if x.force * 5000 - total_poid_item >= poid_requis :
                belligérants_dispo.append(x)
        return belligérants_dispo

    def items_disponibles ( un_belligérant, liste_item ) :
        """
            Permet de renvoyer une liste d'items que le belligérant peut prendre

            Retour: Liste d'item disponible pour le belligérant
        """
        item_dispo = []
        total_poid_item = 0
        for item in un_belligérant.item :
            total_poid_item += item.poids
        for item in liste_item :
            if un_belligérant.force * 5000 - total_poid_item >= item.poids :
                item_dispo.append(item)
        return item_dispo

    def calculer_minimum_poid_requis (liste_item):
        poid_min_requis = liste_item[0]
        for x in liste_item :
            if poid_min_requis < x.poids :
                poid_min_requis = x.poids
        return poid_min_requis

    @property
    def équipes_actives(self):
        return [ joueur.équipe for joueur in self._joueurs if not joueur.équipe.est_éliminée() ]

    @property
    def joueurs (self):
        """
        Accesseur de joueurs.
        """
        return self._joueurs

if __name__ == "__main__":
    import doctest
    doctest.testmod()
