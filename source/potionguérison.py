#=================================
# Nom du fichier: potionguérison.py
# Auteur: Alexandre S. & Jessy B.
# Date: 2014-05-15
# Encodage: Encodage(UTF-8)
#=================================

# --- Importation des modules ---
from random import randint
import potion
import item

# --- Classe Potion Guérison ---
class PotionGuérison(potion.Potion):
	"""
	Potion permettant de rétablir des points de vie
	
	Hérite de Potion
	
	Propriété:
		pts_vie_par_part: int, nombre de pts de vie redonnés par cette potion pour chaque part bue
	
	"""
	
	# --- Initialise les paramètres ---
	def __init__(self, nb_parts, pts_vie_par_part):
		"""
		Paramètres:
			nb_parts: int, nombre d'utilisation possible
			pts_vie_par_part: int, nombre de vie affecter
			
		Exemple:
		>>> from belligérant import Belligérant
		>>> bob = Belligérant("Bob")
		>>> pts_avant = bob.pts_vie
		>>> potion = PotionGuérison(5, 5)
		>>> potion.activer(bob)
		>>> pts_apres = bob.pts_vie
		>>> pts_avant != pts_apres
		True
		
		"""
		
		super().__init__(nb_parts)
		self._nb_parts = nb_parts
		self._pts_vie_par_part = pts_vie_par_part
	
	# --- Fonction activer ---
	def activer(cible):
		"""
		Active l'éffet de la potion
			
			
		--- Condition pour guérison ---
		0-5%   = Endomage Belligérant
		6-100% = Guérit le Belligérant
		
		Paramètre:
			cible: Belligérant affecte par la potion 
		"""

		if randint(1, 100) < 6:
			cible.pts_vie = (cible.pts_vie - self.pts_vie_par_part)
			
		else:
			cible.pts_vie = (cible.pts_vie + self.pts_vie_par_part)


	
if __name__ == "__main__":
	import doctest
	doctest.testmod()

