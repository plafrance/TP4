import partie
import joueur
import contrôleconsole
import arme
import armure


joueur1=joueur.Joueur("Bob", contrôleconsole.ContrôleConsole())
joueur2=joueur.Joueur("Roger", contrôleconsole.ContrôleConsole())

#items=[arme.Arme(1), arme.Arme(2), armure.Armure(1), armure.Armure(2)]

partie=partie.Partie((joueur1, joueur2),1)
#partie.items=items

partie.populer_équipes()
partie.répartir_items()
partie.démarrer_partie()
