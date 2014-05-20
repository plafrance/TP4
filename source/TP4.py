import partie
import joueur
import contrôleconsole
import arme
import armure


joueur1=joueur.Joueur("Bob", contrôleconsole.ContrôleConsole())
joueur2=joueur.Joueur("Roger", contrôleconsole.ContrôleConsole())

items=[arme.Arme(1,1000), arme.Arme(2,1500), armure.Armure(1, 1800), armure.Armure(2, 2200)]

partie=partie.Partie((joueur1, joueur2),1)
partie.items_épars=items

partie.populer_équipes()
partie.répartir_items()
partie.démarrer_partie()
