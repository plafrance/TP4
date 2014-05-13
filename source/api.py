# -*- encoding:utf-8 -*-
#api.py
#Gilbert Paquin
#2014/05/13
#
# API

#Importation des différents libraires requise
import urllib.request, urllib.parse, json, os, getpass, sys, time, threading

"""
    Class Utils
    Contiens différentes fonctions pratique
"""
class Utils:
    def clear(self):
        '''
        Efface l'affichage du system
        '''
        os.system(['clear','cls'][os.name == 'nt'])
    def get(url):
        '''
        Effectu une requête HTTP de type GET

        Paramètre:
        url: (string) L'url qu'on veut récupérer

        Retour: une chaine UTF-8
        '''
        return urllib.request.urlopen(url).read().decode("utf-8")

    def post(url, data):
        '''
        Effectu une requête HTTP de type POST

        Paramètre:
        url: (string) L'url qu'on veut récupérer
        post: (dict) Données à poster

        Retour: une chaine UTF-8
        '''
        data = urllib.parse.urlencode(data).encode()
        return urllib.request.urlopen(url,data).read().decode("utf-8")

    def json_decode(data):
        '''
        Décode une chaine json

        Paramètre:
        data: (str) La chaine a décoder

        Retour: (dict) Données décoder
        '''
        return json.loads(data)

    def choix_menu(self, options_valides):
        '''
        Demande à l'utilisateur de choisir une option

        Paramètre:
        options_valide: (list) Liste des options valides à la sélection

        Retour: le choix de l'utlilisateur
        '''
        choix_menu = None
        while choix_menu == None:
            choix_menu = input("Choisir une option: ")
            if choix_menu[:1].upper() not in options_valides:
                choix_menu = None

        choix_menu = choix_menu[:1].upper()
        return choix_menu

    def input_validated(self, question, regex, message, password = False):
        '''
        Valide par le billet d'une regex la valeur saisie au clavier

        Paramètre:
        question: (str) La question à afficher à l'utilisateur
        regex: (str) L'expression régulière de validation
        message: (str) Le message d'erreur si la valeur saisie n'est pas valide
        password: (bool) Si True n'affiche pas les caractères saisie au clavier à l'utilisateur

        Retour: La valeur valide saisie
        '''
        import re

        if password:
            reponse = getpass.getpass(question)
        else:
            reponse = input(question)

        while re.match(regex, reponse) is None:
            if password:
                reponse = getpass.getpass(message+"\n"+question)
            else:
                reponse = input(message+"\n"+question)
        return reponse

class progress_bar_loading(threading.Thread):
    _stop = False
    def run(self):
            print('Loading....  ',sys.stdout.flush())
            i = 0
            while self._stop != True:
                    if (i%4) == 0:
                        sys.stdout.write('\b/')
                    elif (i%4) == 1:
                        sys.stdout.write('\b-')
                    elif (i%4) == 2:
                        sys.stdout.write('\b\\')
                    elif (i%4) == 3:
                        sys.stdout.write('\b|')

                    sys.stdout.flush()
                    time.sleep(0.2)
                    i+=1


            print('\b\b done!')


    def stop(self, value):
        self._stop = value



"""
    Class API
    Les différentes fonctions afin de faciliter l'utilisation de l'API
"""
class API(Utils):
    SID = None
    def __init__(self):
        '''
        Store le session ID afin de pouvoir rester connecter tout au long
        '''
        self.SID = Utils.json_decode(Utils.get("http://tournoipytonesque.tk/api/?SID"))['PHPSESSID']
    def login(self, username, password):
        '''
        Connexion de l'utilisateur

        Paramètres:
        username: (str) Le nom d'utilisateur
        password: (str) Le mot de passe

        Retour: (dict) Donnée json décoder fournis par l'API
        '''
        data = Utils.post("http://tournoipytonesque.tk/api/?login&withMessage&PHPSESSID=%s" % self.SID, {"username": username, "password": password})
        data_decoded = Utils.json_decode(data)
        return data_decoded
    def register(self,firstname, lastname, username, password):
        '''
        Inscription de l'utilisateur

        Paramètres:
        firstname: (str) Le nom de l'utilisateur
        lastname: (str) Le prénom de l'utilisateur
        username: (str) Le nom d'utilisateur
        password: (str) Le mot de passe

        Retour: (dict) Donnée json décoder fournis par l'API
        '''
        data = Utils.post("http://tournoipytonesque.tk/api/?register&withMessage&PHPSESSID=%s" % self.SID,{"username": username, "password": password, "firstname": firstname, "lastname": lastname})
        data_decoded = Utils.json_decode(data)
        return data_decoded
    def username_check(self, username):
        '''
        Vérification pour voir si le nom d'utilisateur est déjà pris

        Paramètres:
        username: (str) Le nom d'utilisateur à vérifier

        Retour: (bool) Vrai si l'utilisateur existe, Faux si il n'existe pas
        '''
        data = Utils.get("http://tournoipytonesque.tk/api/?username="+username+"&PHPSESSID=%s" % self.SID)
        data_decoded = Utils.json_decode(data)
        return True if data_decoded['messageCode'] == 8 else False
    def user(self):
        '''
        Récupération des données de l'utilisateur

        Retour: (dict) Donnée json décoder fournis par l'API
        '''
        return Utils.json_decode(Utils.get("http://tournoipytonesque.tk/api/?user&PHPSESSID=%s" % self.SID))
    def getStore(self):
        '''
        Récupération de la boutique

        Retour: (dict) Donnée json décoder fournis par l'API
        '''
        data = Utils.get("http://tournoipytonesque.tk/api/?getStore&PHPSESSID=%s" % self.SID)
        data_decoded = Utils.json_decode(data)
        return data_decoded
    def buy(self, store_id):
        '''
        Faire l'achat d'un élément dans la boutique

        Paramètres:
        store_id: (int) l'ID de l'item à acheter

        Retour: (dict) Donnée json décoder fournis par l'API
        '''
        data = Utils.post("http://tournoipytonesque.tk/api/?login&withMessage&PHPSESSID=%s" % self.SID, {"store_id": store_id})
        data_decoded = Utils.json_decode(data)
        return data_decoded

    def startGame(self, type_of_character):
        return Utils.json_decode(Utils.post("http://tournoipytonesque.tk/api/?startGame&PHPSESSID=%s" % self.SID, {"type_of_chracter": type_of_character}))