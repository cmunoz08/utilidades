import re

def dv(r):
	if r==0: return 0
	elif (r>0 and r!=1): return (11-r)
	elif r==1: return "K"

def suma_ponderada(nv):
	sp = 0
	nv.reverse()
	for i in range (len(nv)):
		sp = sp + nv[i]*(i+2)
	r = sp%11
	return dv(r)

def validar(request):
	regex = re.compile('[A-Z]{4}[0-9]{2}')
	if regex.match(request):
		return True
	else: return False

def nd(patente):
	nd = []

	for i in range(0,4):
		if patente[i]== "P":
			nd.append(0)
			continue;
		if patente[i]== "B":
			nd.append(1)
			continue;
		if patente[i]== "C" or patente[i]== "R":
			nd.append(2)
			continue;
		if patente[i]== "D" or patente[i]== "S":
			nd.append(3)
			continue;
		if patente[i]== "F" or patente[i]== "T":
			nd.append(4)
			continue;
		if patente[i]== "G" or patente[i]== "V":
			nd.append(5)
			continue;
		if patente[i]== "H" or patente[i]== "W":
			nd.append(6)
			continue;
		if patente[i]== "J" or patente[i]== "X":
			nd.append(7)
			continue;
		if patente[i]== "K" or patente[i]== "Y":
			nd.append(8)
			continue;
		if patente[i]== "L" or patente[i]== "Z":
			nd.append(9)
			continue;
	nv = nd
	nv.append(int(patente[4]))
	nv.append(int(patente[5]))

	print "DV: ", suma_ponderada(nv)

def calculo_DV():

	patente = raw_input()
	if validar(patente)==True:
		nd(patente)
	elif validar(patente)==False:
		print "Error al digitar la patente: Ej: LLLLNN"
		calculo_DV()	

if __name__ == "__main__":
	calculo_DV()