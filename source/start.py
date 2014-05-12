__author__ = 'gilbert'
import getpass
from api import API

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

choix_menu = None
while choix_menu == None:
    choix_menu = input("Choisir une option: ")
    if choix_menu[:1].upper() not in ['A', 'B']:
        choix_menu = None

choix_menu = choix_menu[:1].upper()



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
+--------------------------------------------+
    ''' % (data_user['firstname']+" "+data_user['lastname'], 0, 0, 0))
elif choix_menu == "B":
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

