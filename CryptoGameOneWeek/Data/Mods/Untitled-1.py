class v():
    liste = {1: 65, 2: 66, 3: 65, 4: 63, 5: 64, 6: 76, 7: 70, 8: 80, 9: 77, 10: 92, 11: 104, 12: 205, 13: 244, 14: 358, 15: 409, 16: 518, 17: 486, 18: 512, 19: 486, 20: 490, 21: 428, 22: 505, 23: 607, 24: 570, 25: 492, 26: 613, 27: 592, 28: 606, 29: 617, 30: 726, 31: 658, 32: 723, 33: 754, 34: 807, 35: 794, 36: 742, 37: 831, 38: 913, 39: 963, 40: 1033, 41: 1027, 42: 976, 43: 1043, 44: 1034, 45: 1135, 46: 1084, 47: 1074, 48: 1197, 49: 1142, 50: 1149, 51: 1278, 52: 1374, 53: 1271, 54: 1283, 55: 1312, 56: 1266, 57: 1326, 58: 1257, 59: 1274, 60: 1181, 61: 1110, 62: 1052, 63: 1006, 64: 1150, 65: 1077, 66: 974, 67: 933, 68: 836, 69: 862, 70: 905, 71: 944, 72: 870, 73: 805, 74: 883, 75: 872, 76: 775, 77: 845, 78: 780, 79: 897, 80: 985, 81: 1112, 82: 1055, 83: 1151, 84: 1189, 85: 1284, 86: 1359, 87: 1451, 88: 1476, 89: 1592, 90: 1502, 91: 1553, 92: 1468, 93: 1393, 94: 1457, 95: 1426, 96: 1504, 97: 1458, 98: 1561, 99: 1554, 100: 1536}
    cours_max = 1592
    cours_low = 63.1
    toure_de_jeu = 100







def l(v):
    ok = 0
    while ok != '4':
        print('		Toure:',v.toure_de_jeu)
        print(' <1> Voir tout	<2> graphique	<3> Plus d options')
        print('		<4> quitter')
        ok = input()
        if v.toure_de_jeu == 0 or v.toure_de_jeu == 1 and ok != '4':
            print('error revenez plus tard SVP')
            ok = 'okjbn'
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

while True:
    if False:
        try:
            l(v)
        except:
            print('une erreur c est produite')
    else:
        l(v)