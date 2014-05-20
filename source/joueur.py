#joueur.py
#13/05/2014
#Alexandre Lambert ,Jérôme Laporte et Andrew Caron
#
#Contient la classe Joueur

import belligérant
import contrôle
import équipe
import action
import partie

class Joueur:
    """
    Un joueur

    Attributs :
         _contrôle : Contrôle , Contient un contrôle
         
    Paramètres :
        _nom : str, le nom du joueur
        _équipe : Équipe, L'équipe que contrôle le joueur
        _actions_par_tour : int, Le nombre d'action que le joueur peut faire
    """
    def __init__( self , un_nom , un_contrôle , nombre_actions_par_tour = 3 ):
        """
        Initialise le Joueur avec un nom sans espaces au début et à la fin et un Contrôle.

        Paramètres :
           _un_nom : str, le pseudonyme du Joueur
           _un_contrôle: Contrôle, Le Contrôle par lequel le joueur interagira avec le jeu.
           
        Exemple :
        >>> Joueur1 = Joueur("Andrew",contrôleconsole.ContrôleConsole.Choisir)
        >>> print(Joueur1.nom)
        Andrew
        """
        self._nom = un_nom.strip()
        self._contrôle = un_contrôle
        self._actions_par_tour = nombre_actions_par_tour
        assert( self._nom == '' or self._nom == None) , " nom invalide "

    def __str__( self ):
        """
        Donne une représentation en chaîne de caractères du Joueur

        Retour : str, Le nom du joueur

        Exemple :
        >>> Joueur1 = Joueur("Andrew",contrôleconsole.ContrôleConsole.Choisir)
        >>> print(Joueur1)
        Andrew
        
        """
        return str(self._nom)

    def choisir_belligérant( self ):
        """
        Utilise le contrôle pour permettre au joueur de choisir un belligérant dans sa propre équipe.

        Retour : Belligérant, Le belligérant selectionné.

        """
        choisir_cible(self._équipe)

    def choisir_action( self , un_acteur ):
        """
        Utilise le contrôle pour permettre au joueur de choisir sa prochaine action.

        Paramètres :
            un_acteur : Belligérant, Le belligérant qui doit faire l'action

        Retour : Action, L'action choisie par le joueur
        """
        liste_actions = [action for action in enumerate(Action)]

        if not isinstance( un_acteur , Mage ):
            liste_actions.delete(Action.JETER_SORT)
            
        choix = self._contrôle.choisir(liste_actions)
        
    def choisir_cible( self , _équipe ):
        """
        Utilise le contrôle pour permettre au joueur de choisir un belligérant ciblé par une action. Le belligérant peut être de son équipe ou de celle d'un adversaire.

        Paramètres ;
            les équipes : Liste d'Équipe, La liste de toutes les équipes parmi lesquelles le joueur peut choisir sa cible.

        Retour : Belligérant, Le belligérant sélectionné.
        """
        liste_belligérant = []
        liste_belligérant_possible = []

        for i in range(len(self._équipe)):
            liste_belligérant += [self._équipe.belligérant(i)]

        for un_belligérant in liste_belligérant :
            if un_belligérant.pts_vie >= 1:
                liste_belligérant_possible += [un_belligérant]

        return contrôle.choisir_objet(liste_belligérant_possible)

    def créer_belligérant(self):
        """
        Crée un belligérant et l'ajoute à l'équipe du jouer.

        Retour : None
        """
        choix = contrôle.choisir(["Guerrier", "Mage"])
        if choix == 0:
            self._équipe.add(belligérant.Guerrier(contrôle.saisir("Choissez le nom de votre Guerrier")))
        elif choix == 1:
            self._équipe.add(belligérant.Mage(contrôle.saisir("Choissez le nom de votre Mage")))
    def jouer(self):
        """
        Utilise le contrôle pour permettre au joueur de jouer son tour.
        Un tour comporte les étapes suivantes :
        1.Choisir un belligérant dans son équipe.
        2.Choisir une action que ce belligérant doit effectuer.
        3.Si l'action est un attaque, choisir son adversaire.
        4.Si l'action concerne un item, choisir l'item.
        5.Si l'action est jeter un sort, choisir le sort et la cible.
        6.Effectuer l'action sur la cible.
        
        """
        for i in range(0, self.actions_par_tour):
            
            mon_belligérant = choisir_belligérant()
            action = choisir_action(mon_belligérant)
            
            if action == Action.ATTAQUER:
                cible = choisir_cible(Partie.la_partie().équipes_actives)
                mon_belligérant.attaquer(cible)
                
            elif action == Action.JETER_SORT:
                sort = self._contrôle.choisir(mon_belligérant.sorts)
                cible = choisir_cible(Partie.la_partie().équipes_actives)
                mon_belligérant.jeter_sort(sort, cible)
                
            elif action == Action.PRENDRE_ITEM:
                mon_belligérant.prendre_item(self.choisir_item(Partie.items_épars))
                
            elif action == Action.JETER_ITEM:
                mon_belligérant.jeter_item(self.choisir_item(mon_belligérant.items()))
                
            elif action == Action.UTILISER_ITEM:
                mon_belligérant.utiliser_item(self.choisir_item(mon_belligérant.items()))
                
            elif action == Action.RIEN:
                pass
            
            else:
                print("Le choix entré n'est pas valide, vous perdez une action")

    def choisir_item(self, une_liste):
        return Contrôle.choisir(une_liste)

    @property
    def nom( self ):
        """
        Accesseur de _nom

        Retour : _nom

        Exemple :
        >>> Joueur1 = Joueur("Andrew",contrôleconsole.ContrôleConsole.Choisir)
        >>> Joueur1.nom
        Andrew
        """
        return self._nom

    @property
    def équipe( self ):
        """
        Accesseur de _équipe

        Retour : _équipe

        Exemple :
        from Équipe import équipe
        >>> Joueur1 = Joueur("Andrew",contrôleconsole.ContrôleConsole.Choisir)
        >>> équipe1 = Équipe("1")
        >>> Joueur1._équipe = équipe1
        >>> print(Joueur1.équipe)
        1
        """
        return self.équipe
        

    @property
    def actions_par_tour( self ):
        """
        Accesseur de _actions_par_tour

        Retour : _actions_par_tour

        Exemple:
        >>> Joueur1 = Joueur("Andrew",contrôleconsole.ContrôleConsole.Choisir)
        >>> Joueur1.actions_par_tour = 3
        >>> print(Joueur1.actions_par_tour)
        3
        """
        return self._actions_par_tour

    @actions_par_tour.setter
    def actions_par_tour( self , nb_actions):
        self._actions_par_tour = nb_actions
