#joueur.py
#13/05/2014
#Alexandre Lambert ,Jérôme Laporte et Andrew Caron
#
#Contient la classe Joueur

import belligérant
import contrôle
import équipe
import action

class Joueur:
    def __init__( self , un_nom , un_contrôle ):
        self._nom = un_nom.strip()
        self._contrôle = un_contrôle
        assert( self._nom == '' or self._nom == None) , " nom invalide "

    def __str__( self ):
        return str(self._nom)

    def choisir_belligérant( self ):
        liste_belligérant = []
        liste_belligérant_possible = []

        for i in range(len(self._équipe)):
            liste_belligérant += [self._équipe.belligérant(i)]

        for un_belligérant in liste_belligérant :
            if un_belligérant.pts_vie >= 1:
                liste_belligérant_possible += [un_belligérant]

        return contrôle.choisir_objet(liste_belligérant_possible)

    def choisir_action( self , un_acteur ):

        choix = self._contrôle.choisir([action for action in enumerate(Action)])

        if not isinstance( un_acteur , Mage ):
            choix.delete(Action.JETER_SORT)
        
    def choisir_cible( self , _équipe ):
        pass

    def créer_belligérant():
         return belligérant.Belligérant(contrôle.saisir("Choissez le nom de votre belligérant"))

    def jouer():
        pass

    def actions_par_tour():
        pass

    @property
    def nom( self ):
        return self._nom

    @property
    def équipe( self ):
        return self.équipe

    @property
    def actions_par_tour( self ):
        return self._actions_par_tour

    @actions_par_tour.setter
    def actions_par_tour( self , nb_actions):
        self._actions_par_tour = nb_actions