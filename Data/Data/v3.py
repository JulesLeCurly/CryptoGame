import time

class v3(object):
	def arroud(self, nb):
		if nb - int(nb) > 0.5:
			nb = nb+1
		return int(nb)
	    
	def nob(self, seed , toure):
		nb = seed
		t = 1
		while nb < 10**700:
			t += 1+toure*seed
			nb = nb*t
		return nb
	
	def chunk(self, seed, RAM, RAM2, MAX, MIN, vu, k):
		#
		pr = ('Encore ---- S')
		debut = time.time()
		ALL_time = time.time()
		#
		seed = int(seed)
		tim = 0
		nb = str(self.nob(seed, 1))
		t = moy = 0
		toure = RAM2
		chunk = {}
		difference = MAX - MIN
		if MAX < MIN or difference > 10**20:
		   	print('v3 Error')
		else:
			while toure != RAM:
				toure += 1
				t += k
				if t > 500:
					t = 0
					nb = str(self.nob(seed, toure))
				tt = fin = 0
				while tt != k:
					fin += int(nb[t + tt])*(10**tt)
					tt += 1
				fin = (fin*difference)/10**k
				chunk[toure] = self.arroud(fin) + MIN
				####
				if vu == 1:
					if toure == int(toure/(RAM/100))*RAM/100:
						print(' ',int(toure/(RAM/100)),'%')
				elif vu == 2:
					if toure == int(toure/(RAM/100))*RAM/100:
						print(str(int(toure/(RAM/100)) ) + '%	' + pr)
						moy += time.time() - debut
						moy = int(moy*100)/100
						pr = int(((moy/int(toure/(RAM/100))) * (((100 - int(toure/(RAM/100)))*100)/100))*100)/100
						pr = 'Encore ' + str(pr) + 'S'
						pr = str(pr)
						debut = time.time()
				####
			if vu == 2:
				print('Finish:',time.time() - ALL_time,'S')
			return chunk