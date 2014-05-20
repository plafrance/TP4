import partie
import joueur
import contrôleconsole
import arme
import armure


joueur1=joueur.Joueur("Bob", ContrôleConsole())
joueur2=joueur.Joueur("Roger", ContrôleConsole())

items=(Arme(1), Arme(2), Armure(1), Armure(2))

partie=Partie((joueur1, joueur2),2)
partie.items=items

partie.populer_équipes()
partie.répartir_items()
partie.démarrer_partie()
