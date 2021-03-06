# -*- coding: utf-8 -*-
#Frédérik Dumulong
#Module du contrôle de la console standard
#15/05/2014

from contrôle import Contrôle

class ContrôleConsole(Contrôle):
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
        valide=False
        while valide != True:
            compteur=1
            for i in choix:
                print (compteur,"-",i)
                compteur+=1
            réponse=self.saisir("Veuillez choisir une option:")
            valide=True
            if not str.isdigit(réponse):
                print("Ceci n'est pas un nombre entier.")
                valide=False
            
            if int(réponse)>len(choix):
                print("Votre choix est invalide.Veuillez entrer un nombre correspondant")
                valide=False
                
        return int(réponse)-1
    def afficher_message(self,un_message,confirmation=False):
        """
        Module permettant d'afficher un message envoyé par un utilisateur

        Retourne le message affiché et sélectionné

        Propriétés:
        un_message:str,le message affiché à l'écran
        confirmation:bool,retourne un booléen représentant si l'utilisateur confirme son choix
        """
        print (un_message)
        if confirmation:
            input()
            
    def saisir(self,question=None):
        """
        Module représentant des messages à saisir

        Retourne un message sélectionné par l'utilisateur

        Propriété:
        question:str,la question qui est posée au joeur s'il veut saisir un texte   
        """
        if question==None:
            return input()
        else:
            print (question)
            return input()
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
