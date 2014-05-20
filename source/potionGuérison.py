#=================================
# Nom du fichier: potionGérison.py
# Auteur: Alexandre S. & Jessy B.
# Date: 2014-05-15
# Encodage: Encodage(UTF-8)
#=================================

# --- Importation des modules ---
from random import randint

# --- Classe Potion Guérison ---
class PotionGuérison:
	"""
	Potion permettant de rétablir des points de vie
	
	Hérite de Potion
	
	Propriété:
		pts_vie_par_part: int, nombre de pts de vie redonnés par cette potion pour chaque part bue
	
	"""
	
	# --- Initialise les paramèteres ---
	def __init__(self, nb_parts, pts_vie_par_parts):
		"""
		Paramètres:
			nb_parts: int, nombre d'utilisation possible
			pts_vie_par_parts int, nombre de vie affecter
			
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
		self.nb_parts = nb_parts
		self.pts_vie_par_parts = pts_vie_par_parts
		
		# --- Validation du nombre de part ---
		assert nb_parts < 1, "Le nombre de part ne peut être plus petit que 1 "
	
	# --- Fonction activer ---
	def activer(self, cible):
		"""
		Active l'éffet de la potion
			
		Paramètre:
			cible: Belligérant affecte par la potion 
		"""

		# --- Condition pour guérison ---
		# 0-5%   = Endomage Belligérant
		# 6-100% = Guérie le Belligérant
		if randint(0, 100) < 6:
			cible.pts_vie = (cible.pts_vie - self.pts_vie_par_parts)
			self.nb_parts -= 1
			
		else:
			cible.pts_vie = (cible.pts_vie + self.pts_vie_par_parts)
			self.nb_parts -= 1


	
if __name__ == "__main__":
	import doctest
	doctest.testmod()

