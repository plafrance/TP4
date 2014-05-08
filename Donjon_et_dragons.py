# -*- coding: utf-8 -*-
from random import randint
from math import ceil

# ---------------------------------------- #
#              Classe Combat               #
# ---------------------------------------- #
class Combat:
    @property
    def coin_droit(self):
        return self._coin_droit

    @property
    def coin_gauche(self):
        return self._coin_gauche
    
    def __init__(self):
        self._coin_droit = Guerrier()
        self._coin_gauche = Mage()
        self._coin_droit.arme = 2
        self._coin_gauche.arme = 3
        self._coin_droit.armure = 2
        self._coin_gauche.armure = 3

    def combattre(self):
        tour = 1
        fin_combat = False
        while not fin_combat:
            if tour == 1:
                print(self._coin_droit.nom + " attaque " + self._coin_gauche.nom + "\n")
                self._coin_droit.attaquer(self._coin_gauche)
                print(self._coin_gauche.pts_vie + " points de vie restants\n")
                tour = 2
            else:
                print(self._coin_gauche.nom + " attaque " + self._coin_droit.nom + "\n")
                self._coin_gauche.attaquer(self._coin_droit)
                print(self._coin_droit.pts_vie + " points de vie restants\n")
                tour = 1
            if not self._coin_droit.pts_vie > 0 or not self._coin_gauche.pts_vie > 0:
                fin_combat = True
                
# ---------------------------------------- #
#           Classe Belligérant             #
# ---------------------------------------- #
class Belligérant:

    @property
    def nom(self):
        return self._nom

    @property
    def pts_vie(self):
        return self._pts_vie

    @property
    def défense(self):
        return self._défense

    @property
    def force(self):
        return self._force
    
    def __init__(self, un_nom):
        _nom = un_nom
        _pts_vie = 1000
        _défense = 0
        _force = 0

    def parer(self):
        parade_de_base = 5
        coup_parer = random.randint(1, 100)
        if coup_parer >= 100-parade_de_base:
            return True
        else:
            return False

    def subir_dégâts(self, impact):
        if self.parer():
            impact = 0
        if impact > 0:
            pts_vie(impact * -1)
        else:
            pts_vie(impact)
            
    def pts_vie(self, ajustement):
        self._pts_vie += ajustement
        if self._pts_vie < 0:
            self._pts_vie = 0

# ---------------------------------------- #
#                Classe Mage               #
# ---------------------------------------- #
class Mage(Belligérant):
    @property
    def armure(self):
        return self._armure
    @armure.setter
    def armure(self, armure_id):
        self._armure = armure_id

    @property
    def arme(self):
        return self._arme
    @arme.setter
    def arme(self, arme_id):
        self._arme = arme_id

    @property
    def force(self):
        return self.__force
    @force.setter
    def force(self, une_force):
        self.__force = une_force

    @property
    def endurance(self):
        return self.__endurance
    
    def __init__(self):
        self._armure = Armure()
        self._armure.équipé = 1
        self._arme = Arme()
        self._arme.équipé = 1
        self.__force = 400
        self.__endurance = 100

    def parer(self):
        parade_de_base = 5 + (self.__endurance * 4)/20
        coup_parer = random.randint(1, 100)
        self.__endurance -= 10
        if self.__endurance < 0:
            self.__endurance = 0
        if coup_parer >= 100-parade_de_base:
            return True
        else:
            return False

    def attaquer(self, cible):
        print("Utilise: " + self.arme.get_arme(self._arme.équipé)[0] + " sur: " + cible.get_armure()[0] + "\n")
        dégâts = Dégâts(self._arme.get_arme(self._arme.équipé)[1], self._arme.get_arme(self._arme.équipé)[2], self.__force, 0, cible.get_armure()[1], cible.get_armure()[2])
        infliction = cible.subir_dégâts(dégâts)
        if infliction == 0:
            print("Parré\n")
        else:
            print(cible.nom() + " -" + infliction + "\n")
            
# ---------------------------------------- #
#             Classe Guerrier              #
# ---------------------------------------- #
class Guerrier(Belligérant):
    @property
    def armure(self):
        return self._armure
    @armure.setter
    def armure(self, armure_id):
        self._armure = armure_id

    @property
    def arme(self):
        return self._arme
    @arme.setter
    def arme(self, arme_id):
        self._arme = arme_id

    @property
    def force(self):
        return self.__force
    @force.setter
    def force(self, une_force):
        self.__force = une_force
    
    def __init__(self):
        self._armure = Armure()
        self._armure.équipé = 1
        self._arme = Arme()
        self._arme.équipé = 1
        self.__force = 400

    def attaquer(self, cible):
        print("Utilise: " + self.arme.get_arme(self._arme.équipé)[0] + " sur: " + cible.get_armure()[0] + "\n")
        dégâts = Dégâts(self._arme.get_arme(self._arme.équipé)[1], self._arme.get_arme(self._arme.équipé)[2], self.__force, 0, cible.get_armure()[1], cible.get_armure()[2])
        infliction = cible.subir_dégâts(dégâts)
        if infliction == 0:
            print("Parré\n")
        else:
            print(cible.nom() + " -" + infliction + "\n")
            
# ---------------------------------------- #
#               Classe Arme                #
# ---------------------------------------- #
class Arme:
    @property
    def équipé(self):
        return self.__équipé
    @équipé.setter
    def équipé(self, arme_id):
        self.__équipé = arme_id
    
    @property
    def dégâts_min(self):
        return self.__dégâts_min

    @property
    def dégâts_max(self):
        return self.__dégâts_max
    
    @property
    def nom_arme(self):
        return self.__nom_armure

    @property
    def entrées(self):
        return self.__entrées
    
    def __init__(self):
        """
        Instancie une arme

        Retour: Aucun

        Paramètre: Aucun
            
        """
        self.__équipé = None
        self.__nom_arme = None
        self.__dégâts_min = None
        self.__dégâts_max = None
        self.configurer("Coup de Poing", 3, 5)
        
    def __arme(self, arme_id):
        """
        Sert à récupéré l'arme équipée à partir de la base de donnée via la méthode get_arme()

        Retour: Aucun

        Paramètre:
            arme_id: Un entier représentant l'id de l'arme dans la base de donnée
            
        """
        try:
            fichier = open("armes.data", 'r')
        except FileNotFoundError as e:
            return "Le fichier est inexistant ou aucune arme n'a été configurée\n\n"
        except PermissionError as e:
            return "Vous n'avez pas la permission de lire le fichier.\n\n"
        try:
            ligne = fichier.readlines()[arme_id]
        except OSError as e:
            return "Erreur de lecture"
        except IndexError as e:
            return "L'id de l'arme est inexistant"
        for i in range(0, len(ligne)):
            if "(" in ligne[i]:
                paramètre1_début = i+1
            if "," in ligne[i]:
                paramètre1_fin = i
                paramètre2_début = i+1
            if ")" in ligne[i]:
                paramètre2_fin = i
        self.__nom_arme = ligne[:paramètre1_début-1]
        self.__dégâts_min = int(ligne[paramètre1_début:paramètre1_fin])
        self.__dégâts_max = int(ligne[paramètre2_début:paramètre2_fin])
        fichier.close()

    def configurer(self, un_nom, minimum, maximum):
        """
        Sert à créé une arme dans la base de donnée

        Retour: Aucun

        Paramètre:
            un_nom: Chaîne de caractère représentant le nom
            minimum: Entier représentant les dégâts minimaux de base de l'arme
            maximum: Entier représentant les dégâts maximaux de base de l'arme
            
        """
        try:
            fichier = open("armes.data", 'r')
            for arme in fichier:
                if un_nom in arme:
                    return
            fichier.close()
        except FileNotFoundError as e:
            print("Erreur lors de la tentative d'ouverture du fichier 'armes.data', fichier introuvable. Le fichier à été créé.")
        except Exception as e:
            print("Il y a eu une erreur lors de la lecture.")
        try:
            fichier = open("armes.data", 'a')
        except Exception as e:
            return "Erreur"
        try:
            fichier.write(un_nom + "(" + str(minimum) + "," + str(maximum) + ")\n")
        except OSError as e:
            return "Erreur d'écriture"
        fichier.close()
                

    def get_arme(self, arme_id):
        """
        Sert à récupéré l'arme équipée à partir de la base de donnée

        Retour: L'arme sous un ensemble représentant: (son nom:str, dégâts minimaux:entier, dégâts maximaux:entier)

        Paramètre:
            arme_id: Un entier représentant l'id de l'arme dans la base de donnée
            
        """
        if not arme_id > 0:
            return "L'id de l'arme est inexistant"
        
        self.__arme(arme_id-1)
        return self.__nom_arme, int(self.__dégâts_min), int(self.__dégâts_max)

# ---------------------------------------- #
#               Classe Armure              #
# ---------------------------------------- #
class Armure:
    @property
    def équipé(self):
        return self.__équipé
    @équipé.setter
    def équipé(self, armure_id):
        self.__équipé = armure_id

    @property
    def nom_armure(self):
        return self.__nom_armure

    @property
    def rés_pourc(self):
        return self.__rés_pourc

    @property
    def rés_fixe(self):
        return self.__rés_fixe

    @property
    def entrées(self):
        return self.__entrées
    
    def __init__(self):
        """
        Instancie une armure

        Retour: Aucun

        Paramètre: Aucun
            
        """
        self.__équipé = None
        self.__nom_armure = None
        self.__rés_pourc = None
        self.__rés_fixe = None
        self.configurer("Pagne du belligérant", 0, 0)
        
    def __armure(self, armure_id):
        """
        Sert à récupéré l'armure équipée à partir de la base de donnée via la méthode get_armure()

        Retour: Aucun

        Paramètre:
            armure_id: Un entier représentant l'id de l'armure dans la base de donnée
            
        """
        try:
            fichier = open("armures.data", 'r')
        except FileNotFoundError as e:
            return "Le fichier est inexistant ou aucune armure n'a été configurée\n\n"
        except PermissionError as e:
            return "Vous n'avez pas la permission de lire le fichier.\n\n"
        try:
            ligne = fichier.readlines()[armure_id]
        except OSError as e:
            return "Erreur de lecture"
        except IndexError as e:
            return "L'id de l'armure est inexistant"
        for i in range(0, len(ligne)):
            if "(" in ligne[i]:
                paramètre1_début = i+1
            if "," in ligne[i]:
                paramètre1_fin = i
                paramètre2_début = i+1
            if ")" in ligne[i]:
                paramètre2_fin = i
        self.__nom_armure = ligne[:paramètre1_début-1]
        self.__rés_pourc = float(ligne[paramètre1_début:paramètre1_fin])
        self.__rés_fixe = int(ligne[paramètre2_début:paramètre2_fin])
        fichier.close()

    def configurer(self, un_nom, une_rés_pourc, une_rés_fixe):
        """
        Sert à créé une armure dans la base de donnée

        Retour: Aucun

        Paramètre:
            un_nom: Chaîne de caractère représentant le nom
            une_rés_pourc: Float représentant une résistance en pourcentage; 0.0 à 1.0;  1.0 représentant 100% de résistance
            une_rés_fixe: Entier représentant une résistance fixe
            
        """
        try:
            fichier = open("armures.data", 'r')
            for armure in fichier:
                if un_nom in armure:
                    return
            fichier.close()
        except FileNotFoundError as e:
            print("Erreur lors de la tentative d'ouverture du fichier 'armures.data', fichier introuvable. Le fichier à été créé.")
        except Exception as e:
            print("Il y a eu une erreur lors de la lecture.")
        try:
            fichier = open("armures.data", 'a')
        except Exception as e:
            return "Erreur"
        try:
            fichier.write(un_nom + "(" + str(une_rés_pourc) + "," + str(une_rés_fixe) + ")\n")
        except OSError as e:
            return "Erreur d'écriture"
        fichier.close()
                

    def get_armure(self, armure_id):
        """
        Sert à récupéré l'armure équipée à partir de la base de donnée

        Retour: L'armure sous un ensemble représentant: (son nom:str, sa résistance en pourcentage:float, sa résistance fixe:entier)

        Paramètre:
            armure_id: Un entier représentant l'id de l'armure dans la base de donnée
            
        """
        if not armure_id > 0:
            return "L'id de l'armure est inexistant"
        
        self.__armure(armure_id-1)
        return self.__nom_armure, float(self.__rés_pourc), int(self.__rés_fixe)
        

# ---------------------------------------- #
#                Classe Dé                 #
# ---------------------------------------- #
class Dé:
    def __init__(self, minimum, maximum):
        """
        Instancie un dé

        Retour: Aucun

        Paramètre: Aucun
            
        """
        self.__jet_max = maximum
        self.__jet_min = minimum

    def calcul_du_jet(self):
        """
        Retourne un jet de dé

        Retour: Retour une valeur aléatoire entre le chiffre minimum du dé et le chiffre maximum

        Paramètre: Aucun
            
        """
        return random.randint(self.__jet_min, self.__jet_max)

# ---------------------------------------- #
#              Classe Dégâts               #
# ---------------------------------------- #
class Dégâts(Dé):
    @property
    def min_dégâts(self):
        return self.__min_dégâts

    @property
    def max_dégâts(self):
        return self.__max_dégâts
    
    @property
    def force(self):
        return self.__force

    @property
    def dommage(self):
        return self.__dommage
    
    @property
    def rés_fixe(self):
        return self.__rés_fixe
    
    @property
    def rés_pourc(self):
        return self.__rés_pourc

    @property
    def dégâts(self):
        return self.__dégâts
    
    def __init__(self, dommage_minimum, dommage_maximum, puissance, dommage_fixe, résistance_ennemi_fixe, résistance_ennemi_pourcentage):
        """
        Instanciation des dégâts infligés
        
        """
        self.__min_dégâts = dommage_minimum
        self.__max_dégats = dommage_maximum
        self.__force = puissance
        self.__dommage = dommage_fixe
        self.__rés_fixe = résistance_ennemi_fixe
        self.__rés_pourc = résistance_ennemi_pourcentage
        self.__dégâts = 0

    def attaque(self):
        """
        Retourne les dégâts infligés à l'adversaire en fonction de sa résistance

        """
        calcul_dégâts()
        return math.ceil(self.__dégâts - (self.__dégâts * self.__rés_pourc) - self.__rés_fixe)
        
    def calcul_dégâts(self):
        """
        Retourne les dégats causés par le joueur
        
        Le calcul des dégâts fonctionne comme suit: Dégâts = Base * (100 + force)/100 + dommage_fixe

        Les dégâts sont stoqués dans un tuple et seront envoyés à la classe Dé qui calculera la force de l'impact
        
        """
        probabilité = math.ceil(self.__min_dégâts * (100 + self.__force)/100 + self.__dommage), math.ceil(self.__max_dégâts * (100 + self.__force)/100 + self.__dommage)
        self.__dégâts = Dé.calcul_du_jet(probabilité[0], probabilité[1])
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
