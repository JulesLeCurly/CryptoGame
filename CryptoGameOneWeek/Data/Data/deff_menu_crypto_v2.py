from random import randint
from ast import literal_eval


class deff_menu(object):
	def always(self,v):
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
			
			
		v.taxe = v.max_dollar/100
		v.taxe = int(v.taxe)+v.toure_de_jeu
		
		
		
	def routine(self, v):
		if randint(0, 9) <= v.malus and v.no_taxe == True:
			deff_menu.malus(self, v)

		if randint(1,200) == 1 and v.Pool == '/':
			v.arobase += 100
			print('!')
			print('!')
			print('Vous avez valider un h en dehors d une pool')
			print('!')
			print('!')
			print('Vous avez reçus:',100,'@.')
			input('Ecrire pour continuer:')
		

		if randint(0, 9) <= v.malus and v.max_dollar > 1000:
			deff_menu.malus(self, v)
		deff_menu.arrond(self, v)
		####
		if v.cours_max == 'set':
			v.cours_max = v.cours_low = v.cours
		if v.cours > v.cours_max:
			v.cours_max = v.cours
		if v.cours < v.cours_low:
			v.cours_low = v.cours
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
		if v.Pool != '/':
			temp = (v.power+1)/100
			if temp < 0.2:
				temp = 0.2
			print('Vous avez reçu',temp,'@ du minage.')
			v.arobase += temp

   
			
			
			
	def l(self, v):
		ok = 0
		while ok != '4':
			if v.toure_de_jeu == 0 or v.toure_de_jeu == 1:
				print('error revenez plus tard SVP')
				break
			print('		Toure:',v.toure_de_jeu)
			print(' <1> Voir tout	<2> graphique	<3> Plus d options')
			print('		<4> quitter')
			ok = input()
			if ok == '4':
				break
			if ok == '1':
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
			elif ok == '2' or ok == '3':
				x = y = 1
				screen = {}
				while y < 31:
					screen[y,x] = ' '
					x = x+1
					if x > 30:
						y = y+1
						x = 1
				x = y = 0
				if ok == '2':
					pos1 = float(input('Position de debut:'))
					pos2 = float(input('Position de fin:'))
				else:
					print('________________')
					print(' <1> voir tout  <2> pos + MAX/MIN')
					print('________________')
					ok = input()
					if ok == '2':
						MAX = 0
						MIN = 0
						t = 0
						while True:
							t += 1
							temp = int(v.liste[t])
							if temp == int(v.cours_low):
								MIN = t
							elif temp == int(v.cours_max):
								MAX = t
							if MAX != 0 and MIN != 0:
								break
						print('________________')
						print(' Position de MAX:',MAX,' =',v.cours_max,'$')
						print(' Position de MIN:',MIN,' =',v.cours_low,'$')
						print('')
						print(' <1> pos1 + MAX')
						print(' <2> pos1 + MIN')
						print(' <3> MAX + pos2')
						print(' <4> MIN + pos2')
						print(' <5> MIN/MAX')
						print('________________')
						ok = input()
						if ok == '1':
							print(' pos2 = MAX')
							pos1 = float(input('Position de debut:'))
							pos2 = MAX
						elif ok == '2':
							print(' pos2 = MIN')
							pos1 = float(input('Position de debut:'))
							pos2 = MIN
						elif ok == '3':
							print(' pos1 = MAX')
							pos1 = MAX
							pos2 = float(input('Position de fin:'))
						elif ok == '4':
							print(' pos1 = MIN')
							pos1 = MIN
							pos2 = float(input('Position de fin:'))
						else:
							if MIN < MAX:
								pos1 = MIN
								pos2 = MAX
							else:
								pos1 = MAX
								pos2 = MIN

					else:
						pos1 = 1
						pos2 = v.toure_de_jeu
				if pos1 > pos2:
					print('Error')
					print('La position de debut ne peut pas etre plus grande que la position de fin.')
				elif pos1 < 1 or pos2 > v.toure_de_jeu:
					print('Error')
					print('Certaine position n existe pas')
				elif pos2 == pos1 == 0:
					print('Error')
					print('Les positions ne peuvent pas etre indentique')
				else:
					case = (pos2 - (pos1-1))/30
					#
					toure = 0
					temp_liste = {}
					MAX = MIN = 0
					if case >= 1:
						while toure < 30:
							toure += 1
							global_select = 0
							moy = 0
							while True:
								moy += v.liste[(pos1-1)+global_select+toure]
								global_select += 1
								if global_select >= case:
									moy = moy/global_select
									if moy - int(moy) > 0.5:
										moy += 1
									moy = int(moy)
									temp_liste[toure] = moy
									
									if toure == 1:			
										MAX = MIN = moy
									if moy > MAX:
										MAX = moy
									elif moy < MIN:
										MIN = moy
									break
						#
						toure = 0
						while toure < 30:
							toure += 1
							temp = ((temp_liste[toure]-MIN)*30)/(MAX-MIN)
							if temp < 1:
								temp = 1
							screen[int(temp), toure] = '#'
							
					else:	
						Toure = 0
						temp_liste = {}
						while Toure != pos2 - (pos1-1):
							Toure += 1
							sortie = v.liste[(pos1-1)+Toure]
							temp_liste[Toure] = sortie
							if Toure == 1:
								MAX = MIN = sortie
							if sortie > MAX:
								MAX = sortie
							elif sortie < MIN:
								MIN = sortie
						Toure = 0
						while Toure != pos2 - (pos1-1):
							Toure += 1
							sortie = temp_liste[Toure]
							sortie = int(((sortie-MIN)*30)/(MAX-MIN))
							if sortie == 0:
								sortie = 1
							screen[sortie, Toure] = '#'
					#
					print('_'*60)
					x = 1
					y = 30
					while y != 0:
						print(screen[y,1],screen[y,2],screen[y,3],screen[y,4],screen[y,5],screen[y,6],screen[y,7],screen[y,8],screen[y,9],screen[y,10],screen[y,11],screen[y,12],screen[y,13],screen[y,14],screen[y,15],screen[y,16],screen[y,17],screen[y,18],screen[y,19],screen[y,20],screen[y,21],screen[y,22],screen[y,23],screen[y,24],screen[y,25],screen[y,26],screen[y,27],screen[y,28],screen[y,29],screen[y,30])
						y -= 1
					print('_'*60)
					print(' Info:        (valeur arrondie)')
					print(' Max',MAX,' Min',MIN,' Tableau: 30X30')
					print(' un careaux horizontale = ',int((case)*100)/100,'Toures de jeu')
					print(' un careaux verticale = ',int((MAX/30)*100)/100,'$ (Valeurs arobase)')


		
		
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
		tg = randint(10+int(v.dollar*0.005),20+int(v.dollar*0.1))
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
			temp = randint(1,8)
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

			if temp >= 4 and temp <= 8:
				print('Question: A combien etait le dernier cours d @ ?')
				if float(input()) == v.cours1:
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