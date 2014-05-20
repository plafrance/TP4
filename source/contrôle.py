# -*- coding: utf-8 -*-
# =========================================================== #
#                        Classe Contrôle                      #
#                                                             #
# Jean-Philippe Mongeau                                       #
# Émile Brunelle                                              #
# contrôle.py                                                 #
# Version 1.0                                                 #
# Dernière modification: 15 mai 2014                          #
#                   Par: Jean-Philippe Mongeau                #
#                                                             #
# =========================================================== #

class Contrôle:
    """
    Classe permettant le contrôle de la sélection d'un objet

    Méthodes:
        choisir_objet(choix)
        
        abstraites:
            afficher_message(un_message, confirmation)
            choisir(choix)
            saisir(question)
    """
    def choisir_objet(self, choix):
        """
        Reçoit une liste d'objet pour faire sélectionner un objet par l'utilisateur

        Paramètres:
            choix: Liste des objets parmi lesquels choisir. (Par exemple, une liste de Belligérants ou d'Items.)

        Retour: L'objet sélectionné.

        """
        liste_de chaîne = []
        for i in range(0, len(choix)):
            liste_de chaîne.append(str(choix[i]))

        return choix[self.choisir(liste_de chaîne)]

    def afficher_message(self, un_message, confirmation = False):
        """
        Méthode abstraite qui permet d'afficher un message au joueur sans attendre de réponse de sa part.

        Paramètres:
            un_message: Chaîne de caractère contenant le message à afficher
            confirmation: Booléen qui détermine si la méthode doit attendre que le joueur ait confirmé la lecture du message pour continuer.
                          Valeur par défaut : False
        """
        pass

    def choisir(self, choix):
        """
        Méthode abstraite qui permet de choisir un élément dans une liste.

        Paramètres:
            choix: Liste des choix offerts aux joueurs.

        Retour: Entier retournant le numéro du choix sélectionné.
        """
        pass

    def saisir(self, question = None):
        """
        Méthode abstraite qui permet au joueur de saisir un texte.

        Paramètres:
            question: Chaîne de caractère représentant la question posée au joueur. Aucune question n'est posée si None.
                Valeur par défaut : None

        Retour: Chaîne de caractère contenant le texte saisi par le joueur.
        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
