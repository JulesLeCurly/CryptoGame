print('____________________________________________________________')
#Bonjour
#import
from random import randint
import time
import json
from ast import literal_eval
#
import sys
#
from Data.Data.deff_crypto_v2 import deff_e
from Data.Data.v3 import v3
v3 = v3()
from Data.Data.deff_menu2_crypto_v2 import deff_menu2
from Data.Data.deff_menu_crypto_v2 import deff_menu

deff = deff_e()
deff_m = deff_menu()
deff_m2 = deff_menu2()
#

#dictionaire

#class
class v():
	arobase = 0
	dollar = 250
	cours = 70
	cours1 = 70
	cours_max = 'set'
	cours_low = 'set'
	toure_de_jeu = 0
	vendre = 0
	taxe = 0
	malus = 0
	liste = {}
	#
	gain = 0
	#
	code = 'debut', time.time()
	#
	carte_2080 = 0
	carte_3070 = 0
	carte_3090 = 0
	obj_h = 0
	obj_ex = 0
	obj_int = 0
	victoire = False
	#
	score = 0
	#
	sync_seed = 0
	seed = 0
	partie = 0
	#
	chunk = {}
	#
	power = (carte_2080*2) + (carte_3070*5) + (carte_3090*10)
	#stat
	max_dollar = dollar
	low_dollar = dollar
	max_arobase = arobase
	low_arobase = arobase
	#
	Pool = '/'
	Pool_toure = 5
	#
	no_taxe = False
	#
	error = False
# toute les variable
ok = 0
t1 = True
time_enregistrement = time.time()
# debut de partie
print('Version: 2.0.38.' + str(randint(0,100)),'					V2')
print('                        ¤ Bienvenue ¤')
print('')
print('	   Crypto@@@ est un jeu de simulation')
print('		de minage de cryptomonnaie.')
print('')
while ok != '1' and ok != '2':
	print('	<1> nouvelle partie	<2> charger une partie')
	ok = input()
if ok == '2':
	deff.choix_de_partie(v)
	if v.error == True:#####
		print('Le fichier de la sauvegarde a été corrompu nous devront donc là supprimer!!!')
		deff.ecrire_info('Fichier Vide')
		print(' Le fichier a été vider')
		time.sleep(4)
		sys.exit()
else:
	print('Seed:')
	print('  Conseil de seed: 35042 or 1 	| Partie rapide: 2')
	print('  Partie difficile: 3 		| seed au hasard: 4')
	v.seed = int(input('seed:'))
	if v.seed > 99999 or v.seed < 0:
		print('La seed n est pas conforme elle sera donc 35042')
		v.seed = 35042
		input('	  <Autre> pour continuer:')
		print('')

	print('		-----Seed de synchronisation:-----')
	print(' <1> pour hazard / <Autre> pour rentrer une seed')
	v.sync_seed = int(input(' 	->'))
	if v.sync_seed == 1:
		v.sync_seed = int(randint(1000,99999))
		print('Seed de synchronisation:',v.sync_seed)
		print('')
		print('')
		input('	  <Autre> pour continuer:')


#on change les variable
if v.seed == 4:
	v.seed = randint(0,999)+randint(4,6)*1000+randint(0,9)*10000
elif v.seed == 2:
	v.seed = 44066
elif v.seed == 1:
	v.seed = 35042
elif v.seed == 0:
	v.seed = 30042
elif v.seed == 3:
	v.seed = 66021
#

variation_du_cours = (v.seed - (int(v.seed/10)*10))*50
MAX = variation_du_cours+50
MIN = variation_du_cours*-1
print(MAX, MIN)
vu = 2#0rien / 1% / 2...
RAM = 100_000
RAM2 = 0
j = 4
v.chunk = v3.chunk(v.sync_seed, RAM, RAM2, MAX, MIN, vu, j)
print('')
#
print('Veuillez patienter')
time.sleep(1)
#Si il y a une partie de charger on retablit les donner du cours d @
if v.partie != 0:
	t = 0
	v.cours = v.cours1 = 70
	while t != v.toure_de_jeu:
		t += 1
		v.cours1 = v.cours
		temp = int(v.cours/200)
		if v.cours > 100:			
			v.cours += v.chunk[t]-temp
			v.cours = int(v.cours)
		elif v.cours < 100:
			v.cours += v.chunk[t]/10
			v.cours = int(v.cours*100)/100
		if v.cours < 1:
			v.cours = 1
		####
		if v.cours_max == 'set':
			v.cours_max = v.cours_low = v.cours
		if v.cours > v.cours_max:
			v.cours_max = v.cours
		if v.cours < v.cours_low:
			v.cours_low = v.cours
		v.liste[t] = int(v.cours)
print('Terminer!')

k = (int(v.seed/1000))-((int(v.seed/10000))*10)
if v.seed != 0 and k < 4 and v.seed != 30042:
	v.seed += (4-k)*1000
	k += 4-k
difficulte_minage = 10**k
#
v.malus = int(v.seed/10000)
v.gain = str(v.seed)
v.gain = int(v.gain[2] + v.gain[3])/10

time.sleep(1)
temp = 600
while temp != 0:
	temp -= 1
	print('')
#jeux
while True:
	deff_m.always(v)
	if time_enregistrement+30 < time.time() and v.partie != 0:
			time_enregistrement = time.time()
			print('~~~~~~~~~~~> Sauvegarde Automatique')
			deff.enregistrement(v)
	
	if v.toure_de_jeu > 3 and v.Pool ==' HELLO':
		print('+ détail (avec hello):	','-3:',v.liste[v.toure_de_jeu-3],'-2:',v.liste[v.toure_de_jeu-2],'-1:',v.liste[v.toure_de_jeu-1],'0:',v.cours)
###ne pas toucher a la suite
	print('____________________________________________________________')
	print('Valeur d @:',int(v.cours),'$|+/-:',int(v.cours-v.cours1))
	print('Power:',int(v.power),'  |tour:',v.toure_de_jeu,'	| Score:',int(v.score),' |pool:',v.Pool)
	print('Vous avez',v.arobase,'@ et',v.dollar,'$')
	if v.vendre != 0:
		print('Il vous reste',v.vendre,'@ a vendre.')
	print('')
	print('  =[V] vendre			=[A] acheter')
	print('  =[E] enlever de la vente	=[M] minage intensif')
	print('  =[R] miner			=[Z] envoyer//recevoir.')
	print('  =[L] pour liste		=[I] pour info')
	print('  =[P] pool de minage		=[c] shop')
	if randint(1,20) == 1 and t1 == True:
		pepe = True
		print('  =[pepe] Pepe the frog')
	else:
		pepe = False
	print('____________________________________________________________')

	ok = input().lower()
	#racourci
	if ok == 'quitte':
		break
	
	elif ok != 'v' and 'v' in ok:
		if ok == 'vmax':
			if v.arobase != 0 and v.dollar > v.taxe:
				v.vendre += v.arobase
				v.arobase = 0
				v.dollar -= v.taxe
			else:
				print('error')
		elif ok[0] == 'v':
			ok = ok.replace('v', '')
			print(ok)
			try:
				float(ok)
				ok = float(ok)
				if v.arobase > ok and v.dollar > v.taxe:
					v.arobase -= ok
					v.vendre += ok
					v.dollar -= v.taxe
				else:
					print('error')
			except ValueError:
				print('heum...','v'+ok,'???')
			


	elif ok == 'int':
		v.arobase = int(v.arobase*10)/10
		v.dollar = int(v.dollar)
		print(' Les valeurs ont été arrondis')
	elif ok == 'en':
		if v.partie == 0:
			print('La partie est enregistrer sur aucun emplacement')
		else:
			deff.enregistrement(v)
			time_enregistrement = time.time()
			print('Enregistrement reussi!')

	#
	elif ok == 'pepe' and pepe == True:
		pepe = False
		deff_m.pepe(v)
		
	elif ok == 'p':
		deff_m2.p(v)
		
	elif ok == 'c':
		deff_m2.c(v)
		
	elif ok == 'e':
		v.arobase += v.vendre
		v.vendre = 0
		
	elif ok == 'l':
		print('HS')
		#deff_m.l(v)
		#try:
		#	deff_m.l(v)
#		except:
	#		print('une erreur c est produite')
		
	elif ok == 'i':
		deff_m.arrond(v)
		deff.i(v)
		
	elif ok == 'a':
		deff_m.a(v)
		
	elif ok == 'v':
		deff_m.v(v)
	
	elif ok == 'r':
		deff.minage(1, int(difficulte_minage*((100-v.power)/100)), v)
		t1 = True
		
	elif ok == 'm':
		print('--------Minage intensif--------')
		try:
			ok = int(input('Nombre de tours:'))
		except:
			ok = 1
		if ok < 2:
			print('Annuler')
		else:
			deff.minage(ok, int(difficulte_minage*((100-v.power)/100)), v)
			t1 = True
				
				
	elif ok == 'z':
		if v.code[0] == 'debut':
			if int(time.time()-(60+v.code[1]))*-1 < 0:
				v.code = 'vide'
				deff_m2.z(v)
			else:
				print('	Ce service est indisponible revenez dans:',int(time.time()-(60+v.code[1]))*-1,'S')
				print('')
				print('		<Autre> Pour continuer')
				ok = input()
		else:
			deff_m2.z(v)
			
	else:
		print('heum...',ok,'???')
	t1 = False