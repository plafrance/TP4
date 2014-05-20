# -*- coding: utf-8 -*-
#Gilbert Paquin
#Module du contrôle de la console http
#15/05/2014

from contrôle import Contrôle

class ContrôleHTTP(Contrôle):
    """
    Console interactive permettant différentes actions a effectuer

    Retourne les différents actions utilisable par la console

    Propriétés:
    afficher_message:bool,affiche un message envoyé via la console interactive
    choisir:int,donne une liste de choix à la disposition,composé de nombres entier
    saisir:str,saisir un texte selectionné par le joueur
    """
    def choisir(self,choix):
        """
        Console interactive qui affiche les différentes opérations possible

        Retourne les choix proposés en une liste de string

        Propriété:
        choix:int,chiffre correspondant au choix approprié
        """
        pass
    def afficher_message(self,un_message,confirmation=False):
        """
        Module permettant d'afficher un message envoyé par un utilisateur

        Retourne le message affiché et sélectionné

        Propriétés:
        un_message:str,le message affiché à l'écran
        confirmation:bool,retourne un booléen représentant si l'utilisateur confirme son choix
        """
        pass
            
    def saisir(self,question=None):
        """
        Module représentant des messages à saisir

        Retourne un message sélectionné par l'utilisateur

        Propriété:
        question:str,la question qui est posée au joeur s'il veut saisir un texte   
        """
        pass
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
