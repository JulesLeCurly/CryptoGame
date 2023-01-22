from random import randint
import time
import json
from ast import literal_eval

from Data.Data.deff_menu_crypto_v2 import deff_menu
deff_m = deff_menu()


class deff_e(object):
	def __init__(self):
		self.nom_fichier = False
	
	def ecrire_info(self, temp):
		with open('Data/Save/'+str(self.nom_fichier), 'w') as fichier:
			json.dump(str(temp), fichier)

	def lire_info(self):
		with open('Data/Save/'+str(self.nom_fichier), 'r') as fichier:
			information_user = json.load(fichier)
			return information_user
	
	def hhh(encodage, code):
		if code-int(code) != 0:
			code = (int(code)*encodage), (int(str(code).split(".")[1])*encodage)
		else:
			code = int(code)*encodage, 0
		return code
		
	def hhh_prime(encodage, code, v):
		code_0 = int(code[0]/encodage)
		code_1 = int(code[1]/encodage)
		if code_0 != int(code_0) or code_1 != int(code_1) or encodage != int(encodage):
			print('error')
			v.error = True
		if code_1 != 0:
			code = str(code_0) + "." + str(code_1)
			return float(code)
		else:
			return int(code_0)
		
	def enregistrement(self, v):
		if v.partie == 1:
			self.nom_fichier = 'crypto@@@_Partie_1.json'
		if v.partie == 2:
			self.nom_fichier = 'crypto@@@_Partie_2.json'
		if v.partie == 3:
			self.nom_fichier = 'crypto@@@_Partie_3.json'
		encodage = randint(50000,1000000)
		temp = {}
		temp['s'] = encodage**2
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
		temp['obj_h'] = deff_e.hhh(encodage, v.obj_h)
		temp['obj_ex'] = deff_e.hhh(encodage, v.obj_ex)
		temp['obj_int'] = deff_e.hhh(encodage, v.obj_int)
		temp['victoire'] = deff_e.hhh(encodage, v.victoire)
		#
		temp['score'] = deff_e.hhh(encodage, int(v.score))
		#
		temp['sync_seed'] = deff_e.hhh(encodage, int(v.sync_seed))
		temp['seed'] = deff_e.hhh(encodage, int(v.seed))
		#
		temp['low_dollar'] = deff_e.hhh(encodage, v.low_dollar)
		temp['max_dollar'] = deff_e.hhh(encodage, v.max_dollar)
		temp['low_arobase'] = deff_e.hhh(encodage, v.low_arobase)
		temp['max_arobase'] = deff_e.hhh(encodage, v.max_arobase)
		temp['Pool'] = v.Pool
		temp['Pool_toure'] = deff_e.hhh(encodage, v.Pool_toure)
		temp['no_taxe'] = v.no_taxe
		#
		deff_e.ecrire_info(self, temp)
	
	
	
			#1 toure # 2 difficilter_minage
	def minage(self, toure_minage, difficulte_minage, v):
		while toure_minage != 0:
			nb_error = t = hm = 0
			l = {}
			h = randint(0,difficulte_minage)# le h
			while hm != h:
				hm = randint(0,difficulte_minage)# h en cours
				if nb_error > 1000000:
					print(hm,'	|',(int((t*100/(difficulte_minage+nb_error))*10000))/10000,'%	|',int(t/1000),'K,h|error:',int(nb_error/1000000),'M,',(int((nb_error/1000000)+1000)-int(nb_error/1000))*-1,'K|',toure_minage)
				elif nb_error > 1000:
					print(hm,'	|',(int((t*100/(difficulte_minage+nb_error))*10000))/10000,'%	|',int(t/1000),'K,h|error:',int(nb_error/1000),'K|',toure_minage)
				else:
					print(hm,'	|',(int((t*100/(difficulte_minage+nb_error))*10000))/10000,'%	|',int(t/1000),'K,h|error:',nb_error,'U|',toure_minage)
				if hm in l:
					nb_error += 1
				l[hm] = 1
				t += 1
			print('		========================') 
			print(' H trouver:',h,'|Nombre d error:',str(nb_error)+'.')
			print(' Pourcentage final',(int((t*100/(difficulte_minage+nb_error))*10000))/10000,'% |Nombre de h testés:',str(t)+'.')
			deff_m.routine(v)
			if (int((t*100/(difficulte_minage+nb_error))*10000))/10000 >= 99.99 and v.seed != 30042:
				toure_minage = 0
				v.obj_int += 1
				print('Vous avez fait plus de 99,99 % du minage vous recevez donc l objet [?]')
				print('Vous avez',v.obj_int,'objet [?].')
				input('Ecrire pour continuer:')
				ok = 0
			elif randint(1,200) == 1 and v.Pool == '/' and v.seed != 30042:
				v.arobase += int((1_000_000/v.cours)*1000)/1000
				print('!')
				print('!')
				print('Vous avez valider un h en dehors d une pool')
				print('!')
				print('!')
				print('Vous avez reçus:',int((1_000_000/v.vours)*1000)/1000,'@.')
				input('Ecrire pour continuer:')
				ok = 0
			else:
				toure_minage -= 1
				
				
				
	def choix_de_partie(self, v):
		ok = 0
		while ok < 1 or ok > 3:
			print('Quelle partie voulez vous charger?')
			print(' 1 2 3')
			ok = v.partie = float(input())
		if v.partie == 1:
			self.nom_fichier = 'crypto@@@_Partie_1.json'
		if v.partie == 2:
			self.nom_fichier = 'crypto@@@_Partie_2.json'
		if v.partie == 3:
			self.nom_fichier = 'crypto@@@_Partie_3.json'
		#
		temp = {}
		informations_utilisateur = literal_eval(deff_e.lire_info(self))
		temp = informations_utilisateur
		#
		encodage = int(temp['s'])**0.5
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
		v.obj_h = int(deff_e.hhh_prime(encodage, temp['obj_h'], v))
		v.obj_ex = int(deff_e.hhh_prime(encodage, temp['obj_ex'], v))
		v.obj_int = int(deff_e.hhh_prime(encodage, temp['obj_int'], v))
		v.victoire = int(deff_e.hhh_prime(encodage, temp['victoire'], v))
		#
		v.score = int(deff_e.hhh_prime(encodage, temp['score'], v))
		#
		v.sync_seed = int(deff_e.hhh_prime(encodage, temp['sync_seed'], v))
		v.seed = int(deff_e.hhh_prime(encodage, temp['seed'], v))
		#
		v.low_dollar = int(deff_e.hhh_prime(encodage, temp['low_dollar'], v))
		v.max_dollar = int(deff_e.hhh_prime(encodage, temp['max_dollar'], v))
		v.low_arobase = int(deff_e.hhh_prime(encodage, temp['low_arobase'], v))
		v.max_arobase = int(deff_e.hhh_prime(encodage, temp['max_arobase'], v))
		v.Pool = temp['Pool']
		v.Pool_toure = int(deff_e.hhh_prime(encodage, temp['Pool_toure'], v))
		v.no_taxe = temp['no_taxe']
		#
		v.power = (v.carte_2080*2) + (v.carte_3070*5) + (v.carte_3090*10)
		print('')
		print('		<_>Etat de la partie<_>')
		print('	Seed:',v.seed)
		print('Seed de synchronisation:',v.sync_seed)
		print('')
		print(' ',v.arobase,'@	',v.dollar,'$	coure d @:',v.cours,'$')
		print(' ',v.vendre,'@ a vendre |	tour:',v.toure_de_jeu)
		print('')
		print('  2080:',v.carte_2080,'  3070:',v.carte_3070,'  3090:',v.carte_3090)
		print('  objet:	#',v.obj_h,'	!',v.obj_ex,'	?',v.obj_int)
		print('  Pool:',v.Pool,'	| Power:',v.power,'	| Score',v.score)
		print('		<_>Etat de la partie<_>')
		print('  ; )')
		print('')
		print('')
		input('	  <Autre> pour continuer:')
		
		
	def i(self, v):
		print('---------')
		print('Seed:',v.seed)
		print('Seed de syncronisation:',int(v.sync_seed))
		print('  <>1 enregistrer	<>2 modifier	<>3 raccourci')
		print('---------')
		ok = input()
		if ok == '3':
			print('')
			print('		Tous les racourci:')
			print(' en -> i + 1 | enregistrement')
			print(' int         | arrondi de @ et de $')
			print('	quitte		| quitte le jeu')
			print('	vMAX		| mets en ventes touts ce que vous avez')
			ok = input('ecrire pour continuer')	
		if ok == '1':
			if v.partie == 0:
				print('La partie est enregistrer sur aucun emplacement')
			else:
				deff_e.enregistrement(v)
				print('Enregistrement reussi!')

		elif ok == '2':
			if v.partie != 0:
				print('Emplacement actuelle:',v.partie)
			else:
				print('Aucun emplacement')
			print('')
			print('Choisissez votre emplacement')
			print('	1 2 3')
			v.partie = float(input())
			if v.partie > 3 or v.partie < 1:
				print('error')
			else:
				if v.partie == 1:
					nom_fichier = 'crypto@@@_Partie_1.json'
				if v.partie == 2:
					nom_fichier = 'crypto@@@_Partie_2.json'
				if v.partie == 3:
					nom_fichier = 'crypto@@@_Partie_3.json'