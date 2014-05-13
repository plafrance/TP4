# -*- encoding:utf-8 -*-
#start.py
#Gilbert Paquin
#2014/05/13
#
# Fichier principale

import getpass
from api import API, progress_bar_loading


p = progress_bar_loading()
p.start()

import time
time.sleep(5)
p.stop(True)


#Initialisation de l'API
API = API()
API.clear()
#Debut du programme
print('''
+--------------------------------------------+
|                                            |
|           Tournoi pytonesque 4             |
|                                            |
|  A. Connexion                              |
|  B. Inscription                            |
+--------------------------------------------+
''')

#premier menu
choix_menu = API.choix_menu(['A', 'B'])

if choix_menu == "A":
    API.clear()
    username = password = ""
    logged = {"messageCode": 3}
    while logged["messageCode"] == 3:
        while username == "":
            username = input("Nom d'utilisateur: ").strip()

        while password == "":
            password = getpass.getpass("Mot de passe: ").strip()

        logged = API.login(username, password)

        if(logged["messageCode"] == 3):
            API.clear()
            print(logged["message"])
            username = password = ""


    data_user = API.user()
    API.clear()
    print('''
+--------------------------------------------+
|
| Bienvenue, %s
| Vous avez %i py en se moment
| Nombre de victoire: %i
| Nombre de defaite: %i
|
| a. Jouer
| b. Aller dans le magasin
| c. Quitter
+--------------------------------------------+
    ''' % (data_user['firstname']+" "+data_user['lastname'], int(data_user['money']), int(data_user['win']), int(data_user['loose'])))

    #------ MENU 2 ------#
    choix_menu_2 = API.choix_menu(['A', 'B', 'C'])
    if choix_menu_2 == "A":
        API.clear()
        print('''
+--------------------------------------------+
| a. Jouer contre une autre personne localement
| b. Crée contre un adversaire en ligne (HOST)
| c. Rejoindre une partie
| d. Quitter
+--------------------------------------------+
    ''')
        #----- MENU 3 -----#
        choix_menu_3 = API.choix_menu(['A', 'B', 'C'])
        if choix_menu_3 == 'A':
            print("Le blabla local qui n'existe pas encore")

        if choix_menu_3 == 'B':
            API.clear()
            print('''
+--------------------------------------------+
| Choissisez votre personnage
|
| a. Un mage
| b. Un guerrier
+--------------------------------------------+
            ''')
            choix_personnage = API.choix_menu(['A', 'B'])

            session = API.startGame(choix_personnage)
            API.clear()
            if session["messageCode"] != 13:
                print("ERROR: %s" % session["message"])
            else:
                print('''
+--------------------------------------------+
|
| Le numéro de votre partie est: #%s
|
+--------------------------------------------+
                ''' % session["id"])

        if choix_menu_3 == 'D':
            quit()
    if choix_menu_2 == "B":
        options = []
        data_store = API.getStore()
        API.clear()
        print('''
+--------------------------------------------+
|
| Les armes''')
        for arme in data_store["weapons"]:
            options += [arme["code"]]
            print("| %s) %s <%s py> Attaque min: %s max: %s" % (arme["code"], arme["name"], arme["price"], arme["min"], arme["max"]))
        print("|\n| Les boucliers")
        for arme in data_store["shields"]:
            options += [arme["code"]]
            print("| %s) %s <%s py> Protection: %s" % (arme["code"], arme["name"], arme["price"], arme["strength"]))
        print('''|
+--------------------------------------------+''')
        choix_achat = API.choix_menu(options)
        #A faire
        #API.buy(choix_achat)

    if choix_menu_2 == "C":
        quit()
if choix_menu == "B":
    API.clear()
    print('''
+--------------------------------------------+
|                                            |
|           Tournoi pytonesque 4             |
|                                            |
|               Inscription                  |
|                                            |
+--------------------------------------------+
''')
    firstname = API.input_validated("Prenom: ", "^[a-zA-Z0-9]{3,50}$", "Caractere alphanumerique entre 3 et 50 caracteres")
    lastname = API.input_validated("Nom de famille: ", "^[a-zA-Z0-9]{3,50}$", "Caractere alphanumerique entre 3 et 50 caracteres")

    username = API.input_validated("Nom d'utilisateur: ", "^[a-zA-Z0-9-_]{3,50}$", "Caractere alphanumerique entre 3 et 50 caracteres")
    while not API.username_check(username):
        username = API.input_validated("Le nom d'utilisateur choisi est deja pris :-(\nNom d'utilisateur: ", "^[a-zA-Z0-9-_]{3,50}$", "Caractere alphanumerique entre 3 et 50 caracteres")

    password = API.input_validated("Mot de passe: ", "^.{8,}$", "Le mot de passe doit avoir 8 caracteres minimum", True)
    password2 = API.input_validated("Confirmation du mot de passe: ", "^.{8,}$", "Le mot de passe doit avoir 8 caracteres minimum", True)
    while password != password2:
        password2 = API.input_validated("Les mot de passe ne corresponde pas veuillez ressayer.\nConfirmation du mot de passe: ", "^.{8,}$", "Le mot de passe doit avoir 8 caracteres minimum", True)

    data = API.register(firstname, lastname, username, password)
    if(data["messageCode"] == -1):
        raise Exception("Veuillez redemarrer le programme et essayer de nouveau, car il y a eu un probleme cote serveur lors tu traitement de votre demande")
    print(data["message"])

