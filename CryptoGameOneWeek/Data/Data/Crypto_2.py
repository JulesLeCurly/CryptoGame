print('____________________________________________________________')
#Bonjour
#import
from random import randint
import time
from ast import literal_eval
#
import sys
#
from Data.Data.deff_crypto_v2 import deff_e
from Data.Data.v3 import v3
generate = v3()
from Data.Data.deff_menu2_crypto_v2 import deff_menu2
from Data.Data.deff_menu_crypto_v2 import deff_menu

deff = deff_e()
deff_m = deff_menu()
deff_m2 = deff_menu2()
#class
class v():
	nom_fichier = False
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
	#
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
	#
	no_taxe = False
	#
	error = False
# toute les variable
ok = 0
t1 = True
# debut de partie
def narative():
	print('________________')
	print('Explication narrative ne touche à rien!!!!!!!!')
	time.sleep(2)
	print('<><><><><><><>')
	print("Bonjour et bienvenue dans le jeu de cryptogame")
	time.sleep(4)
	print('Le but de ce jeu est simple avoir le plus d argent en une semaine')
	time.sleep(4)
	print('Au bout de la semaine vous ne pourrez plus à accéder au jeu')
	time.sleep(4)
	print('Le court arobase change toutes les 30 minutes même si vous restez déconnecter')
	time.sleep(2)
	print('vous n aurez pas besoin du wifi ni d Internet')
	time.sleep(2)
	print('Réfléchissez bien à votre stratégie')
	time.sleep(4)
	print('Que le meilleur gagne!!!!!!!!')
	print('<><><><><><><>')
	time.sleep(1)

print('Version: 2.0.38.' + str(randint(0,100)),'					V2')
print('                        ¤ Bienvenue ¤')
print('')
print('	   Crypto@@@ est un jeu de simulation')
print('		de minage de cryptomonnaie.')
print('')
ok = input('Entrer pour commencer:')
#Verifier que chunk est assez grand!!!!
start_time = 1704553142#30/01/2023 00:00:00
End_time = 1705157942
between_time = 1800

r = 25469

while time.time() < start_time:
    temps = int(start_time - time.time())
    days = str(temps // 86400)+'J'
    hours = str((temps % 86400) // 3600)+'H'
    minutes = str((temps % 3600) // 60)+'M'
    secondes = str(temps % 60)+'S'
    print("Il reste encore ",days,hours,minutes,secondes," avant le démarrage du concours.")
    time.sleep(1)

v.seed = 25044
variation_du_cours = (v.seed - (int(v.seed/10)*10))*50

v.nom_fichier = 'crypto@@@_Partie.json'
sortie = deff_e.lire_info(v)
if sortie != 'lunch':
	deff_e.choix_de_partie(v)
else:
	narative()

MAX = variation_du_cours+80
MIN = variation_du_cours*-1
vu = 0
RAM = 340
RAM2 = 0
j = 4
v.chunk = generate.chunk(r, RAM, RAM2, MAX, MIN, vu, j)
if v.error == True and 1 == 2:#####
	print('Le fichier de la sauvegarde a été corrompu')
	sys.exit()


print('')
#
def Actualisation(v):
	dif = v.toure_de_jeu
	v.toure_de_jeu = int((int(time.time())-start_time)/between_time)+1
	dif = v.toure_de_jeu - dif
	t = 0
	v.cours = v.cours1 = 70
	v.liste ={}
	while t != v.toure_de_jeu:
		t += 1
		v.cours1 = v.cours
		temp = int(v.cours/200)
		if v.cours > 300:			
			v.cours += v.chunk[t]-temp
			v.cours = int(v.cours)
		elif v.cours > 100:
			if v.chunk[t] < -10:
				v.cours += v.chunk[t]/10
				v.cours = int(v.cours*100)/100
			else:	
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
	t= 0
	while t != dif:
		t += 1
		deff_m.routine(v)
Actualisation(v)
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
v.nom_fichier = 'crypto@@@_Partie.json'
time_enregistrement = time.time()

if time.time() > End_time:
	while True:
		print('La partie est terminée voici votre score:')
		print('')
		print(' Power:',int(v.power),' |pool:',v.Pool)
		print(' Vous avez',v.arobase,'@ et',v.dollar,'$')
		print('')
		print('Vous pouvez voir le cours @;')
		try:
			deff_m.l(v)
		except:
			print('une erreur c est produite')

while True:
	deff_m.always(v)
	if time.time() > End_time:
		print('Le jeu est terminer')
		print('Reconecter vous pour voire votre score')
		time.sleep(3)
		break

	if v.toure_de_jeu < int((int(time.time())-start_time)/between_time)+1:
		Actualisation(v)
		if v.dollar < 0:
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('perdu Motif: vous n avez plus d argent')
			print('Voici votre score:')
			print('')
			print(' Power:',int(v.power),' |pool:',v.Pool)
			print(' Vous avez',v.arobase,'@ et',v.dollar,'$')
			print('Dépêchez-vous de revenir vous aurez peut-être encore une chance de gagner')
			time.sleep(4)
			deff_e.ecrire_info(v, 'lunch')
			sys.exit()

	if time_enregistrement+30 < time.time():
			time_enregistrement = time.time()
			print('~~~~~~~~~~~> Sauvegarde Automatique')
			deff_e.enregistrement(v)
	
	if v.toure_de_jeu > 3 and v.Pool ==' HELLO':
		print('+ détail (avec hello):	','-3:',v.liste[v.toure_de_jeu-3],'-2:',v.liste[v.toure_de_jeu-2],'-1:',v.liste[v.toure_de_jeu-1],'0:',v.cours)



	deff_m.arrond(v)
	print('____________________________________________________________')
	temps = int(End_time - time.time())
	days = str(temps // 86400)+'J'
	hours = str((temps % 86400) // 3600)+'H'
	minutes = str((temps % 3600) // 60)+'M'
	secondes = str(temps % 60)+'S'
	print("Il reste encore ",days,hours,minutes,secondes," avant la Fin du concours.")


	print('µµµµ')
	temp = (int( (int(time.time()) - start_time) /between_time )+1) * between_time
	temp = int(temp - int(time.time()-start_time))
	print('Temps avant le prochain changement d @',temp,'S')


	print('µµµµ')
	print('Valeur d @:',int(v.cours),'$|+/-:',int(v.cours-v.cours1))
	print('Power:',int(v.power),'  |tour:',v.toure_de_jeu,' |pool:',v.Pool)
	print('Vous avez',v.arobase,'@ et',v.dollar,'$')
	if v.vendre != 0:
		print('Il vous reste',v.vendre,'@ a vendre.')
	print('')
	print('  =[V] vendre			=[A] acheter')
	print('  =[E] enlever de la vente	=[Z] envoyer//recevoir.')
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
		deff_e.enregistrement(v)
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
		deff_m.l(v)
		try:
			deff_m.l(v)
		except:
			print('une erreur c est produite')
		
	elif ok == 'i':
		print('')
		print('		Tous les racourci:')
		print(' en -> i + 1 | enregistrement')
		print(' int         | arrondi de @ et de $')
		print('	quitte		| quitte le jeu')
		print('	vMAX		| mets en ventes touts ce que vous avez')
		input('ecrire pour continuer')	
		
	elif ok == 'a':
		deff_m.a(v)
		
	elif ok == 'v':
		deff_m.v(v)
						
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