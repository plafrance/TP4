__author__ = 'gilbert'

import urllib.request, urllib.parse, json, os, getpass

class Utils:
    def clear(self):
        os.system(['clear','cls'][os.name == 'nt'])
    def get(url):
        return urllib.request.urlopen(url).read().decode("utf-8")

    def post(url, data):
        data = urllib.parse.urlencode(data).encode()
        return urllib.request.urlopen(url,data).read().decode("utf-8")

    def json_decode(data):
        return json.loads(data)

    def input_validated(self, question, regex, message, password = False):
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

class API(Utils):
    SID = None
    def __init__(self):
        self.SID = Utils.json_decode(Utils.get("http://tournoipytonesque.tk/api/?SID"))['PHPSESSID']
    def login(self, username, password):
        data = Utils.post("http://tournoipytonesque.tk/api/?login&withMessage&PHPSESSID=%s" % self.SID, {"username": username, "password": password})
        data_decoded = Utils.json_decode(data)
        return data_decoded
    def register(self,firstname, lastname, username, password):
        data = Utils.post("http://tournoipytonesque.tk/api/?register&withMessage&PHPSESSID=%s" % self.SID,{"username": username, "password": password, "firstname": firstname, "lastname": lastname})
        data_decoded = Utils.json_decode(data)
        return data_decoded
    def username_check(self, username):
        data = Utils.get("http://tournoipytonesque.tk/api/?username="+username+"&PHPSESSID=%s" % self.SID)
        data_decoded = Utils.json_decode(data)
        return True if data_decoded['messageCode'] == 8 else False
    def user(self):
        return Utils.json_decode(Utils.get("http://tournoipytonesque.tk/api/?user&PHPSESSID=%s" % self.SID))