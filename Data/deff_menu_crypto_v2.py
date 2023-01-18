from random import randint
import time
import json
from ast import literal_eval



class deff_menu(object):
	def always(self,v):
		temp_score = v.dollar + (v.arobase*v.cours) + ((v.carte_2080*6000) + (v.carte_3070*50000) + (v.carte_3090*100000)+(v.obj_h*1000000)+(v.obj_ex*10000000))
		temp_score = int(temp_score*0.8)
		temp_score = int(temp_score*0.001)-17
		if temp_score > v.score:
			v.score = temp_score
		
		deff_menu.arrond(self, v)
		if v.dollar > v.max_dollar:
			v.max_dollar = v.dollar
		if v.dollar < v.low_dollar:
			v.low_dollar = v.dollar
			#
		if v.arobase > v.max_arobase:
			v.max_arobase = v.arobase
		if v.arobase < v.low_arobase:
			v.low_arobase = v.arobase
			
		if v.dollar > 1000:
			v.no_taxe = True
			
			
		v.taxe = v.max_dollar/1000
		v.taxe = int(v.taxe)
		
		
		
	def routine(self, v):
		if randint(0, 9) <= v.malus and v.no_taxe == True:
			deff_menu.malus(self, v)
		if v.Pool_toure > 0:
			v.Pool_toure -= 1
		v.toure_de_jeu += 1
		v.cours1 = v.cours
		temp = int(v.toure_de_jeu/35)
		if temp > 25:
			temp = 25
		if v.cours > 100:			
			v.cours += v.chunk[v.toure_de_jeu]-temp
			v.cours = int(v.cours)
		elif v.cours < 100:
			v.cours += v.chunk[v.toure_de_jeu]/10
			v.cours = int(v.cours*100)/100
		if v.cours < 1:
			v.cours = 1
		if randint(0, 9) <= v.malus and v.max_dollar > 1000:
			deff_menu.malus(self, v)
		deff_menu.arrond(self, v)
		####
		if v.cours > v.cours_max:
			v.cours_max = v.cours
			if v.Pool == 'HELLO':
				print('!')
				print('by hello:')
				print('Le cours de @ est au plus bas')
				print('!')
				if v.toure_minage != 0:
					print(' <Autre> pour continuer / <1> pour arreter')
					ok = input()
					if ok == '1':
						v.toure_minage = 0
		if v.cours < v.cours_low:
			v.cours_low = v.cours
			if v.Pool == 'HELLO':
				print('!')
				print('by hello:')
				print('Le cours de @ est au plus bas')
				print('!')
				if v.toure_minage != 0:
					print(' <Autre> pour continuer / <1> pour arreter')
					ok = input()
					if ok == '1':
						v.toure_minage = 0
		####
		if v.vendre != 0:
			vente_temp = v.vendre
			v.vendre = int(v.vendre)
			v.vendre -= randint(int(v.vendre*0.7),v.vendre)
			if v.Pool == 'FBG':
				v.vendre = 0
			print('')
			print('Vendu:',vente_temp-v.vendre,'@.')
			v.dollar += (vente_temp-v.vendre)*v.cours
		v.liste[v.toure_de_jeu] = int(v.cours)
		if v.Pool == 'C53':
			print('{{{{{{{{{')
			print('Vous avez reçu 75$')
			v.dollar += 75
			print('C53	:)')
			print('{{{{{{{{{')
		if v.Pool == 'BTC':
			print('{{{{{{{{{')
			print('Vous avez reçu 0.25 @')
			v.arobase += 0.25
			print('BTC	;^)')
			print('{{{{{{{{{')
		if v.Pool != 'ITS+':
			v.malus = int(v.seed/10000)
		if v.Pool == '+=+':
			print('{{{{{{{{{')
			print('Vous avez perdu 1000$')
			v.dollar -= 1000
			print('+=+	heum...')
			print('{{{{{{{{{')
		if v.Pool != '/':
			print('Vous avez reçu',v.gain,'@ du minage.')
			v.arobase += v.gain
			
			
			
	def l(self, v):
		y = 1
		x = 0
		screen = {}
		while y < 30:
			x += 1
			screen[y, x] = '.'
			if x == 30:
				x = 0
				y += 1
		ok = 0
		while ok != '3':
			print(' 1 Voir tout	2 graphique	3 quitter')
			ok = input()
			if ok == '1':
				if v.toure_de_jeu == 0:
					print('error')
				else:
						print('Vours d @:')
						print(v.liste)
						t = 0
						moy = 0
						while t != v.toure_de_jeu:
							t += 1
							moy += v.liste[t]
						moy = int(moy/v.toure_de_jeu)
						print('Maximum:',int(v.cours_max),'Minimum:',int(v.cours_low),'Moyenne:',moy,'	by HELLO')
						print('')
			elif ok == '2':
				x = y = 1
				screen = {}
				while y < 31:
					screen[y,x] = '.'
					x = x+1
					if x > 30:
						y = y+1
						x = 1
				x = y = 0
				pos1 = float(input('Position de debut:'))-1
				pos2 = float(input('Position de fin:'))
				if pos1 > pos2:
					print('Error')
					print('La position de debut ne peut pas etre plus grande que la position de fin.')
				elif pos1 < 1 or pos2 > v.toure_de_jeu:
					print('Error')
					print('Certaine position n existe pas')
				elif pos2 - pos1 == 0:
					print('Error')
				else:
					temp = (pos2 - pos1)/30
					#
					toure = 0
					max = 0
					min = 'debut'
					temp_liste = {}
					while toure != 30:
						toure += 1
						t = 0
						moy = 0
						while t < temp:
							t += 1
							if int((toure*temp)+t+pos1) in v.liste:
								moy += v.liste[int((toure*temp)+t+pos1)]
							else:
								t -= 1
								break
						if min == 'debut':
							min = moy
							max = moy
						if moy > max:
							max = moy
						if moy < min:
							min = moy
						temp_liste[toure] = int(moy/t)
					t = 0
					if max == min:
						print('error')
					else:
						while t != 30:
							t += 1
							j = temp_liste[t]-min
							j = (j*30)/(max-min)
							if j - int(j) > 0.5:
								j += 1 
							if j < 1:
								j = 1
							j = int(j)
							screen[j, t] = '#'
						#
						x = 1
						y = 30
						while y != 0:
							print(screen[y,1],screen[y,2],screen[y,3],screen[y,4],screen[y,5],screen[y,6],screen[y,7],screen[y,8],screen[y,9],screen[y,10],screen[y,11],screen[y,12],screen[y,13],screen[y,14],screen[y,15],screen[y,16],screen[y,17],screen[y,18],screen[y,19],screen[y,20],screen[y,21],screen[y,22],screen[y,23],screen[y,24],screen[y,25],screen[y,26],screen[y,27],screen[y,28],screen[y,29],screen[y,30])
							y = y-1
		

		
		
	def malus(self, v):
		tg = randint(1,30)
		print('')
		print('%%%%%%%%%%%%')
		if tg == 1:
			print('Vous n avez pas declare votre pissine!!!')
		if tg == 2:
			print('C est un jour comme un autre')
		if tg == 3:
			print('vous avez faim c est l heure de faire vos coursses')
		if tg == 4:
			print('Allo??? la police? on m a vole')
		if tg == 5:
			print('C est l anniversaire de votre amie')
		if tg == 6:
			print('Abonnement Netflix')
		if tg == 7:
			print('Votre facture de gaz')
		if tg == 8:
			print('Votre facture d electricite')
		if tg == 9:
			print('Cette fois c est la facture d eau')
		if tg == 10:
			print('il va falloir vous racheter un frigo')
		if tg == 11:
			print('Vous etes gentil et vous offrez un peu d argent a un sdf')
		if tg == 12:
			print('Il y a une fuite dans votre toit')
		if tg == 13:
			print('Je me demande si vous avez encore de l argent')
		if tg == 14:
			print('Votre carte graphique est cassee')
		if tg == 15:
			print('Vous avez attrape un rhume')
		if tg == 16:
			print('Vous vous etes blesse rendez vous a l hopital')
		if tg == 17:
			print('Vous vous etes fait arnaquer')
		if tg == 18:
			print('hey votre pote relou')
		if tg == 19:
			print('Vous avez besoin de vous deplacer payez votre nouvelle voiture!')
		if tg == 20:
			print('Payer vos etudes!')
		if tg == 21:
			print('Votre chat a casse votre rig de minage')
		if tg == 22:
			print('Votre chat est mort')
		if tg == 23:
			print('Amende pour exces de vitesse')
		if tg == 24:
			print('Facture de telephone')
		if tg == 25:
			print('Payez l addition')
		if tg == 26:
			print('Vous n avez pas gagne au loto: Dommage!')
		tg = randint(10+int(v.dollar*0.1),20+int(v.dollar*0.3))
		print('		vous avez perdu',tg,'$')
		print('	',v.dollar,'$ -',tg,'$ =',int(v.dollar-tg))
		v.dollar = int(v.dollar-tg)
		print('%%%%%%%%%%%%')

	def v(self, v):
		print('Taxe:',v.taxe,'$')
		try:
			jj = float(input('Vendre combien de @:'))
		except:
			print('Error')
		else:
			if v.taxe > v.dollar:
				print('vous n avez pas assez de $ pour payer les taxes')
			elif jj > v.arobase:
				print('vous n avez pas assez d @')
			elif jj < 0:
				print('error')
			elif jj != 0:
				v.arobase -= jj
				v.vendre += jj
				v.dollar -= v.taxe


###
	def a(self, v):
		print('Taxe:',v.taxe,'$ | Vous pouvez acheter au maximum pour:',v.dollar-v.taxe,'$')
		try:
			jj = float(input('Acheter pour combien en $:'))
		except:
			print('Error')
		else:
			if jj+v.taxe > v.dollar and jj <= v.dollar:
				print('vous n avez pas assez de $ pour payer les taxes')
			elif jj > v.dollar:
				print('vous n avez pas assez de $')
			elif jj < 0:
				print('error')
			elif jj != 0:
				v.dollar -= jj
				v.arobase += jj/v.cours
				v.dollar -= v.taxe
	



	def arrond(self, v):
		v.dollar = int((v.dollar+0.00001)*100)/100
		v.arobase = int((v.arobase+0.0000001)*100000)/100000
		v.vendre = int((v.vendre+0.0000001)*100000)/100000


	def pepe(self, v):
		print(' Pepe: Bonjour je suis pepe the frog')
		print(' Pepe: Est tu pres?')
		ok = input('oui ou non: ')
		if ok == 'oui':
			print('Nous allons voir si tu merite ton argents:')
			print('')
			temp = randint(1,9)
			correct = False
			if temp == 1:
				print('Question: Combien coûte une 2080?')
				if float(input()) == 6000:
					correct = True		
			if temp == 2:
				print('Question: Combien coûte une 3070?')
				if float(input()) == 50000:
					correct = True
			if temp == 3:
				print('Question: Combien coûte une 3090?')
				if float(input()) == 100000:
					correct = True
			if temp == 4:
				print('Question: Combien coûte l objet [#]?')
				if float(input()) == 1000000:
					correct = True
			if temp == 5:
				print('Question: Combien coûte l objet [!]?')
				if float(input()) == 50000000:
					correct = True
			if temp >= 6 and temp <= 8:
				print('Question: A combien etait le dernier cours d @ ?')
				if float(input()) == cou1:
					correct = True
			if temp == 9:
				print('Question: Combien vous raporte la pool C53 en $ ?')
				if float(input()) == 75:
					correct = True
			if correct == True:
				print('')
				print(' Pepe: mmm... Vous avez juste!')
				print(' Pepe: Vous mertiez votre argent')
				print(' Pepe: Je vais la multiplier par 1,5')
				print('')
				v.dollar = v.dollar*1.5
				deff_menu.arrond(self, v)
				print(' Pepe: Vous avez maintenant:',v.dollar,'$.')
			else:
				print(' Pepe: c est faux c est bien dommage je vais devoire diviser votre argents par 2 car vous ne la meriter pas!')
				print(' Pepe: Peut-être que la prochaine fois vous en serais plus digne.')
				print('')
				print(v.dollar,'$ /2 =',int(v.dollar/2),'$')
				v.dollar = int(v.dollar/2)
		elif ok == 'non':
				print(' Pepe: Ok a la prochaine fois.')
		else:
			print('Parle tu notre langue?')
		ok = input('Ecrire pour continuer')