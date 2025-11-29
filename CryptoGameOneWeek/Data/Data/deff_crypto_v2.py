from random import randint
import json
from ast import literal_eval

from Data.Data.deff_menu_crypto_v2 import deff_menu
deff_m = deff_menu()

class deff_e(object):
	
	def ecrire_info(v, temp):
		with open('Data/Save/'+str(v.nom_fichier), 'w') as fichier:
			json.dump(str(temp), fichier)

	def lire_info(v):
		with open('Data/Save/'+str(v.nom_fichier), 'r') as fichier:
			information_user = json.load(fichier)
			return information_user
	
	def hhh(encodage, code):
#		if code-int(code) != 0:
#			code = (int(code)*encodage), (int(str(code).split(".")[1])*encodage)
#		else:
#			code = int(code)*encodage, 0
		return code

		
	def hhh_prime(encodage, code, v):
#		try:
#			code_0 = float(code[0]/encodage)
#			code_1 = float(code[1]/encodage)
#			if code_0 != int(code_0) or code_1 != int(code_1):
#				print('error')
#				v.error = True
#			if code_1 != 0:
#				code = str(code_0) + "." + str(code_1)
#				return float(code)
#			else:
#				return int(code_0)
#		except:
#			print('error')
#			v.error = True
		return code#TAB

	def enregistrement(v):
		v.nom_fichier = 'crypto@@@_Partie.json'
		encodage = randint(50000,1000000)
		temp = {}
		temp['s'] = encodage
		temp['arobase'] = deff_e.hhh(encodage, v.arobase*100000)
		temp['dollar'] = deff_e.hhh(encodage, v.dollar*100)
		temp['cours'] = deff_e.hhh(encodage, v.cours)
		temp['cours_max'] = deff_e.hhh(encodage, v.cours_max)
		temp['cours_low'] = deff_e.hhh(encodage, v.cours_low)
		temp['toure_de_jeu'] = deff_e.hhh(encodage, v.toure_de_jeu)
		temp['vendre'] = deff_e.hhh(encodage, v.vendre*100000)
		temp['malus'] = deff_e.hhh(encodage, v.malus)
		temp['taxe'] = deff_e.hhh(encodage, v.taxe)
		#
		temp['carte_2080'] = deff_e.hhh(encodage, v.carte_2080)
		temp['carte_3070'] = deff_e.hhh(encodage, v.carte_3070)
		temp['carte_3090'] = deff_e.hhh(encodage, v.carte_3090)
		#
		#
		temp['sync_seed'] = deff_e.hhh(encodage, int(v.sync_seed))
		temp['seed'] = deff_e.hhh(encodage, int(v.seed))
		#
		temp['low_dollar'] = deff_e.hhh(encodage, v.low_dollar)
		temp['max_dollar'] = deff_e.hhh(encodage, v.max_dollar)
		temp['low_arobase'] = deff_e.hhh(encodage, v.low_arobase)
		temp['max_arobase'] = deff_e.hhh(encodage, v.max_arobase)
		temp['Pool'] = v.Pool
		temp['no_taxe'] = v.no_taxe
		#
		deff_e.ecrire_info(v, temp)
	
				
	def choix_de_partie(v): 
		v.nom_fichier = 'crypto@@@_Partie.json'
		temp = {}
		informations_utilisateur = literal_eval(deff_e.lire_info(v))
		temp = informations_utilisateur
		#
		encodage = int(temp['s'])
		if encodage <50000 or encodage > 1000000:
			v.error = True
		v.arobase = int(deff_e.hhh_prime(encodage, temp['arobase'], v))/100000
		v.dollar = int(deff_e.hhh_prime(encodage, temp['dollar'], v))/100
		v.cours = int(deff_e.hhh_prime(encodage, temp['cours'], v))
		v.cours_max = int(deff_e.hhh_prime(encodage, temp['cours_max'], v))
		v.cours_low = int(deff_e.hhh_prime(encodage, temp['cours_low'], v))
		v.toure_de_jeu = int(deff_e.hhh_prime(encodage, temp['toure_de_jeu'], v))
		v.vendre = int(deff_e.hhh_prime(encodage, temp['vendre'], v))/100000
		v.malus = int(deff_e.hhh_prime(encodage, temp['malus'], v))
		v.taxe = int(deff_e.hhh_prime(encodage, temp['taxe'], v))
		#
		v.carte_2080 = int(deff_e.hhh_prime(encodage, temp['carte_2080'], v))
		v.carte_3070 = int(deff_e.hhh_prime(encodage, temp['carte_3070'], v))
		v.carte_3090 = int(deff_e.hhh_prime(encodage, temp['carte_3090'], v))
		#
		#
		v.low_dollar = int(deff_e.hhh_prime(encodage, temp['low_dollar'], v))
		v.max_dollar = int(deff_e.hhh_prime(encodage, temp['max_dollar'], v))
		v.low_arobase = int(deff_e.hhh_prime(encodage, temp['low_arobase'], v))
		v.max_arobase = int(deff_e.hhh_prime(encodage, temp['max_arobase'], v))
		v.Pool = temp['Pool']
		v.no_taxe = temp['no_taxe']
		#
		v.power = (v.carte_2080*2) + (v.carte_3070*5) + (v.carte_3090*10)
		print('')
		print('		<_>Etat de la partie<_>')
		print('')
		print(' ',v.arobase,'@	',v.dollar,'$	coure d @:',v.cours,'$')
		print(' ',v.vendre,'@ a vendre |	tour:',v.toure_de_jeu)
		print('')
		print('  2080:',v.carte_2080,'  3070:',v.carte_3070,'  3090:',v.carte_3090)
		print('  Pool:',v.Pool,'	| Power:',v.power)
		print('		<_>Etat de la partie<_>')
		print('  ; )')
		print('')
		print('')
		input('	  <Autre> pour continuer:')