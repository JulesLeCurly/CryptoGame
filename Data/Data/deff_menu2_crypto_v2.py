from random import randint
import time

class deff_menu2(object):
	def z(self, v):
		###
		if v.code != 'vide':
			if int(time.time()-(60+v.code[1]))*-1 < 0:
				v.code = 'vide'
				
		###
		if v.code == 'vide':
			ok = 0
			while ok != '1' and ok != '2' and ok != '3':
				print('		<1> Recevoir')
				print('		<2> Envoyer')
				print('		<3> Quitter')
				ok = input('->')
				if ok != '1' and ok != '2' and ok != '3':
					print('????')
			if ok == '1':
				print('Entrer le code de reception:')
				code = input()
				code = int(str(code).replace('e', '3').replace('m', '8').replace('j', '7').replace('t', '5'))
				
				div = code-(int(code/100)*100)
				code = int(code/100)
				code = code/div
				
				tip = code-(int(code/10)*10)
				time.sleep(1)
				if code != int(code) or code < 10**6 or div < 70 or div > 99 or tip != 1 and tip != 2:
					print('Ce code ne peut pas exister')
				else:
					code = int(code/10)
					code_time = code-(int(code/1000000)*1000000)
					security_id = time.time()
					security_id = security_id-(int(security_id/1000000)*1000000)
					code = int(code/1000000)
				
					if code_time > int(security_id) or code_time+60 < int(security_id):
						print('Ce code a expirer')
					else:
						if tip == 1:
							print('------$-$$$-$------')
							print('Vous avez reçu:',code,'$.')
							print('------$-$$$-$------')
							v.dollar += code
						if tip == 2:
							print('------@-@@@-@------')
							print('Vous avez reçu:',code,'@.')		
							print('------@-@@@-@------')
							v.arobase += code
								
								
				
				
				
				
				
			elif ok == '2':
				ok = 0
				while ok != '1' and ok != '2' and ok != '3':
					print('		<1> $')
					print('		<2> @')
					print('		<3> annuler')
					ok = input('->')
					if ok != '1' and ok != '2' and ok != '3':
						print('????')
						
				
				if ok == '1':
					print('Vous avez:',v.dollar,'$')
					print('Pour combien voulez vous envoyer?: $')
					ok = float(input('->'))
					if ok > v.dollar:
						print('Vous n avez pas assez de $.')
					elif ok < 0:
						print('Error')
					elif ok != int(ok):
						print('Vous ne pouvez pas envoyer des chiffres à virgules.')
					else:
						ok = int(ok)
						print('	',v.dollar,'$ -',ok,'$')
						ok2 = 0
						while ok2 != 'oui' and ok2 != 'non':
							print('confirmer?')
							print('<oui> / <non>')
							ok2 = input('->')
							if ok2 != 'oui' and ok2 != 'non':
								print('????')
						if ok2 == 'oui':
							security_id = time.time()
							security_id = security_id-(int(security_id/1000000)*1000000)
							code = int(ok*1000000+security_id)
							temp = randint(70, 99)
							tip = 1
							code = ((code*1000)+(tip*100))*temp
							code = code + temp
							code = str(code).replace('3', 'e').replace('8', 'm').replace('7', 'j').replace('5', 't')
							v.dollar -= ok
							v.code = code, time.time()
							print('	////////////////')
							print('	code d envoi:',code)
							print('	////////////////')
							print('votre compte a été débité de',ok,'$.')
						else:
							print('annuler')
				if ok == '2':
					print('Vous avez:',v.arobase,'@')
					print('Pour combien voulez vous envoyer?: @')
					ok = float(input('->'))
					if ok > v.arobase:
						print('Vous n avez pas assez de @.')
					elif ok < 0:
						print('Error')
					elif ok != int(ok):
						print('Vous ne pouvez pas envoyer des chiffres à virgules.')
					else:
						ok = int(ok)
						print('	',v.arobase,'@ -',ok,'@')
						ok2 = 0
						while ok2 != 'oui' and ok2 != 'non':
							print('confirmer?')
							print('<oui> / <non>')
							ok2 = input()
							if ok2 != 'oui' and ok2 != 'non':
								print('????')
						if ok2 == 'oui':
							security_id = time.time()
							security_id = security_id-(int(security_id/1000000)*1000000)
							code = int(ok*1000000+security_id)
							temp = randint(70, 99)
							tip = 2
							code = ((code*1000)+(tip*100))*temp
							code = code + temp
							code = str(code).replace('3', 'e').replace('8', 'm').replace('7', 'j').replace('5', 't')
							v.arobase -= ok
							v.code = code, time.time()
							print('	////////////////')
							print('	code d envoi:',code)
							print('	////////////////')
							print('votre compte a été débité de',ok,'@.')
						else:
							print('annuler')
		else:
			print('Il vous reste:',int(time.time()-(60+v.code[1]))*-1,'S avant que votre code expire, par la suite vous pourrez en créer un nouveau ou recevoir un code.')
			print('Votre code créé actuel:',v.code[0])
			print('')
			print('	<1> Voir le decompte	<Autre> Quitter')
			ok = input('->')
			if ok == '1':
				while int(time.time()-(60+v.code[1]))*-1 > -1:
					t = 60
					while t != 0:
						t -= 1
						print('')
					print('Il vous reste:',int(time.time()-(60+v.code[1]))*-1,'S | Code:',v.code[0])
					time.sleep(1)









	def c(self,v):
		ok = ok2 = 0
		while ok != '4':
			power = (v.carte_2080*2) + (v.carte_3070*5) + (v.carte_3090*10)
			print('')
			print('			BIENVENU AU shop')
			print('	Vous avez:')
			print('		2080:',v.carte_2080,'  3070:',v.carte_3070,'  3090:',v.carte_3090)
			print('	Objet:')
			print('		#',v.obj_h,'	!',v.obj_ex,'	?',v.obj_int)
			print('	Vous avez',v.dollar,'$')
			print('')
			print('	 <1> acheter')
			print('	 <2> vendre carte graphique')
			print('	 <3> autre')
			print('	 <4> quitter')
			ok = input('->')
			if ok == '3':
				while ok != '9':
					print('')
					print('Bienvenu')
					print('	Vous avez',v.dollar,'$')
					print('')
					print('	 <1> Voir le cours d arobase dans le futur')
					print('	 <9> Quitter')
					print('')
					ok = input('->')
					if ok == '1':
						print('Pour voir la prochaine valeur du cours il va faloir nous payer 10 000$')
						print('	 <1> Ok	<Autre> Quitter')
						ok = input('->')
						if ok == '1':
							if v.dollar < 10000:
								print('Vous n avez pas assez de $')
							else:
								print('-----')
								print('Le prochain cours d arobase est: +/-',v.chunk[v.toure_de_jeu + 1]-cours,'$ et',v.chunk[v.toure_de_jeu + 1]-cours)
								print('-----')
								print('		<Autre> Pour continuer')
							
			if ok == '2':
				while ok != '9':
					ok2 = 0
					print('	Vous avez:')
					print('		2080:',v.carte_2080,'  3070:',v.carte_3070,'  3090:',v.carte_3090)
					print('	Vous avez',v.dollar,'$')
					print('')
					print('  Revendre les cartes a 75% de leurs valeurs initiales')
					print('			    normale     75%')
					print('		  <1> 2080 |    6 000$ |  4 500$')
					print('		  <2> 3070 |   50 000$ |  37 500$')
					print('		  <3> 3090 |  100 000$ |  75 000$')
					print('		<9> Quitter')
					print('')
					ok = input('->')
					if ok == '1':
						print('	Revendre une 2080 pour 4 500$ ?')
						print('Vous en avez:',v.carte_2080)
						while ok2 != 'oui' and ok2 != 'non':
							print('confirmer?')
							print('<oui> / <non>')
							ok2 = input()
							if ok2 != 'oui' and ok2 != 'non':
								print('????')
						if ok2 == 'oui':
							if v.carte_2080 == 0:
								print('	Vous n avez pas assez de carte (0)')
							else:
								v.carte_2080 -= 1
								print('	Vendu')
								print('	Vous avez recu 4 500$')
								v.dollar += 4500
								input('	  <Autre> pour continuer:')
					elif ok == '2':
						print('	Revendre une 3070 pour 37 500$ ?')
						print('Vous en avez:',v.carte_3070)
						while ok2 != 'oui' and ok2 != 'non':
							print('confirmer?')
							print('<oui> / <non>')
							ok2 = input()
							if ok2 != 'oui' and ok2 != 'non':
								print('????')
						if ok2 == 'oui':
							if v.carte_3070 == 0:
								print('	Vous n avez pas assez de carte (0)')
							else:
								v.carte_3070 -= 1
								print('	Vendu')
								print('	Vous avez recu 37 500$')
								v.dollar += 37500
								input('	  <Autre> pour continuer:')
					elif ok == '3':
						print('	Revendre une 3090 pour 75 000$ ?')
						print('Vous en avez:',v.carte_3090)
						while ok2 != 'oui' and ok2 != 'non':
							print('confirmer?')
							print('<oui> / <non>')
							ok2 = input()
							if ok2 != 'oui' and ok2 != 'non':
								print('????')
						if ok2 == 'oui':
							if v.carte_3090 == 0:
								print('	Vous n avez pas assez de carte (0)')
							else:
								v.carte_3090 -= 1
								print('	Vendu')
								print('	Vous avez recu 75 000$')
								v.dollar += 75000
								input('	  <Autre> pour continuer:')
			elif ok == '1':
				while ok != '9':
					v.dollar = int(v.dollar*100)/100
					print('	Vous avez:')
					print('		2080:',v.carte_2080,'  3070:',v.carte_3070,'  3090:',v.carte_3090)
					print('	Objet:')
					print('		#',v.obj_h,'	!',v.obj_ex,'	?',v.obj_int)
					print('	Vous avez',v.dollar,'$')
					print('')
					print('		carte graphique:')
					print('		  <1> 2080 |    6 000$ max 5')
					print('		  <2> 3070 |   50 000$ max 6')
					print('		  <3> 3090 |  100 000$ max 5')
					print('		objet:')
					print('		  <4> # |   1 000 000$ max 9')
					print('		  <5> ! |  50 000 000$ max 9')
					print('		  <6> ? | juste info')
					print('		  <7> *  | Victoire')
					print('')
					print('		<9> Quitter')
					ok = input('->')
					if ok == '7':
						print('Acheter la victoire pour 600@ et 500 000 000$')
						print('	<1> acheter')
						print('	<Autre> pour continuer')
						ok = input('->')
						if ok == '1':
							if v.dollar >= 500_000_000 and v.arobase >= 600 and v.victoire == False:
								v.dollar -= 500_000_000
								v.arobase -= 600
								v.victoire = True
							elif v.dollar < 500_000_000:
								print('Vous n avez pas assez de $')
								print('')
								input('	  <Autre> pour continuer:')
							elif v.arobase < 600:
								print('Vous n avez pas assez d @')
								print('')
								input('	  <Autre> pour continuer:')
							else:
								print('Vous avez deja achetter la victoire')
								print('')
								input('	  <Autre> pour continuer:')
					elif ok == '1':
						print('Pour une carte graphique 2080 qui est la plus base game de carte le prix seleve a 6 000$. Parfaite pour un premier investissement!')
						print('Power 2')
						print('	<1> acheter')
						print('	<Autre> pour continuer')
						ok = input('->')
						if ok == '1':
							if v.dollar >= 6000 and v.carte_2080 != 5:
								v.carte_2080 += 1
								v.dollar -= 6000
							elif v.dollar < 6000:
								print('Vous n avez pas assez de $')
								print('')
								input('	  <Autre> pour continuer:')
							else:
								print('Vous avez deja 5 carte graphique de ce type')
								print('')
								input('	  <Autre> pour continuer:')
					elif ok == '2':
						print('La carte 3070 est une carte de tres bon chois! Une carte parfaite pour un budget moyen! Nous vous la proposont pour 50 000.')
						print('Power 5')
						print('	<1> acheter')
						print('	<Autre> pour continuer')
						ok = input('->')
						if ok == '1':
							if v.dollar >= 50000 and v.carte_3070 != 6:
								v.carte_3070 += 1
								v.dollar -= 50000
							elif v.dollar < 50000:
								print('Vous n avez pas assez de $')
								ok = input('->')
								print('')
								input('	  <Autre> pour continuer:')
							else:
								print('Vous avez deja 6 carte graphique de ce type')
								print('')
								input('	  <Autre> pour continuer:')
					elif ok == '3':
						print('La carte 3090 est la carte la plus puissante qui existe! Avec cella vous serrez sur de ne pas attendre des heure pendant votre minage! Nous vous la proposont pour 100 000.')
						print('Power 10')
						print('	<1> acheter')
						print('	<Autre> pour continuer')
						ok = input('->')
						if ok == '1':
							if v.dollar >= 100000 and v.carte_3090 != 5:
								v.carte_3090 += 1
								v.dollar -= 100000
							elif v.dollar < 100000:
								print('Vous n avez pas assez de $')
								print('')
								input('	  <Autre> pour continuer:')
							else:
								print('Vous avez deja 5 carte graphique de ce type')
								print('')
								input('	  <Autre> pour continuer:')
					elif ok == '4':
						print('Vous pouvez acheter ce premier objet [#] pour 1 000 000$. Nous le considerons comme un trophé pour dire que vous etes le meilleur! (Aucun remboursement)')
						print('	<1> acheter')
						print('	<Autre> pour continuer')
						ok = input('->')
						if ok == '1':
							if v.dollar >= 1000000 and v.obj_h != 9:
								v.obj_h = v.obj_h+1
								v.dollar = v.dollar-1000000
							elif v.dollar < 1000000:
								print('Vous n avez pas assez de $')
								print('')
								input('	  <Autre> pour continuer:')
							else:
								print('Vous avez deja 9 objets de ce type')
								print('')
								input('	  <Autre> pour continuer:')
					elif ok == '5':
						print('Vous pouvez acheter cet objet [!] pour 50 000 000$. Nous le considerons comme un trophé de PRO traider pour dire que vous etes le meilleur! (Aucun remboursement)')
						print('	<1> acheter')
						print('	<Autre> pour continuer')
						ok = input('->')
						if ok == '1':
							if v.dollar >= 50_000_000 and v.obj_ex != 9:
								v.obj_ex += 1
								v.dollar -= 50_000_000
							elif v.dollar < 50_000_000:
								print('Vous n avez pas assez de $')
								print('')
								input('	  <Autre> pour continuer:')
							else:
								print('Vous avez deja 9 objets de ce type')
								print('')
								input('	  <Autre> pour continuer:')
					elif ok == '6':
						print('L objet [?] est un objet et sobtient que si vous réussissez à atteindre 99,99% du minage. Voila a vous de jouer :)')
						print('')
						input('	  <Autre> pour continuer:')
			power = (v.carte_2080*2) + (v.carte_3070*5) + (v.carte_3090*10)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	def p(self, v):
		ok = 0
		while ok != '9':
			print('--------Pool de Minage--------')
			if v.Pool_toure != 0:
				print('Il vous resete',v.Pool_toure,'tour avant de pouvoir changer de pool')
			print('	Votre pool actuelle:',v.Pool)
			print('Voici les pools de minage:')
			print('---')
			print('		 <1>c53	<2>btc')
			print('		 <3>Fbg	<4>hello')
			print('		 <5>its	<6>+=+')
			print('---')
			print('		<8> Quittez la pool actuelle')
			print('		<9> Quitter')
			ok = input('->')
			if ok == '8':
				v.Pool = '/'
			if ok == '1' or ok == '2' or ok == '3' or ok == '4' or ok == '5' or ok == '6':
				print('')
				print('-')
				text = self.definir_text()
				print(text[int(ok)])
				print('')
				print('	<1> Entrer dans la pool')
				print('	<Autre> pour continuer')
				ok2 = input()
				if ok2 == '1' or ok2 == '3667':
					if v.Pool_toure == 0:
						v.Pool_toure = 10
						if ok == '1':
							v.Pool = 'C53'
						elif ok == '2':
							v.Pool = 'BTC'
						elif ok == '3':
							v.Pool = 'FBG'
						elif ok == '4':
							v.Pool = 'HELLO'
						elif ok == '6':
							v.Pool = '+=+'
						elif ok =='5' and ok2 == '3667' and v.Pool != 'ITS+':
							print('Nous savons que vous êtes une bonne personne nous sélectionnont les meilleures personne pour participer à notre pool. Grâce à nous vous ne perdrai moins d argents. Voici 250$.')
							print('		Vous avez reçu 250$')
							v.dollar += 250
							print('		',v.dollar,'$ +',250,'$ =', v.dollar + 250)
							print('')
							v.Pool = 'ITS+'
							v.malus = 1
							input('	  <Autre> pour continuer:')
						elif ok == '5':
							v.Pool = 'ITS'
					else:
						print('Votre delais n est pas terminer, il vous reste',v.Pool_toure,'toures.')
						input('	<Autre> pour continuer:')
						print('')
						print('')
				
				
				
	def definir_text(self):
		text = {}
		text[1] = 'Bonjour et bienvenue sur la pool de minage C53, nous vous proposons un partage équilibré entre chaque membre de notre pool. Si vous faites partie de nos membres nous vous donnerons 75$ par minage en échange de votre participation.'
		text[2] = 'BTC pour bienvenue à tous les concombres. Contrairement à ce que vous pourrez le penser nous prenons très au sérieux nos membres de notre pool. Grace a nous vous aurais un gain de + 0.25@ par minage'
		text[3] = 'FBG et une pool de minage actif. Avec nous vous serez certain de pouvoir vendre tous vos @ instantanement. Et vous n aurez plus a attendre qu il ce vende'
		text[4] = 'Bienvenue dans la pool de minage Hello. Si vous nous rejoignez nous vous informerons dès que le courss de @ sera au plus haut ou au plus bas. On vous permetra d avoir une coursbe du cours d @ dans longlet [l].'
		text[5] = 'Le respect de votre vie privée est notre priorité. Fuidifier le fonctionnement du minage, mesurer la fréquentation et permettre à la fois la publicité, le contenu personnalisé et le ciblage. Certains sont nécessaires au fonctionnement correct du site et ne peuvent être refusés. En outre, nous traitons également d autres donnés personnelles telles que votre adresse IP, votre géolocalisation afin de mieux personnaliser le contenu que nous vous proposons. aaaaaaaa. Certains partenaires s appuient sur leur intérêt légitime pour traiter vos données.Charles de Gaulle, communément appelé le général de Gaulle ou parfois simplement le Général, né le 22 novembre 1890 à Lille et mort le 9 novembre 1970 à Colombey-les-Deux-Églises, est un militaire, résistant, homme d État et écrivain français. Une cryptomonnaie, dite aussi cryptoactif, cryptodevise, monnaie cryptographique ou encore cybermonnaie, est une monnaie numérique émise de pair à pair, sans nécessité de banque centrale, utilisable au moyen d un réseau informatique décentralisé. PS: appuie sur 3667. Voila Voila.'
		text[6] = 'Bienvenue sur la pool de minage +=+. Clique ici pour avoir un iPhone 13. Heumm... pardon. Si vous nous rejoignez vous pouvez gagner jusqu à 1 milliard de $ grâce à nous. Et nous vous offrons une vie de rêve. REJOiGNER NOUS!!! iPhone 12 peut etre???'
		return text