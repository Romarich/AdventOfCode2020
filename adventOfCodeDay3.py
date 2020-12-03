#Part 1 AdventOfCode Day 3
def day3AdventOfCodePart1():
	f = open("input/inputDay3.txt","r")
	valeurARenvoyer = 0
	indice = 0
	for x in f:
		if(indice > (len(x)-2)):
			indice = indice - (len(x)-1)
		if(x[indice] == '#'):
			valeurARenvoyer += 1
		indice += 3
	return valeurARenvoyer
	
#Part 2 AdventOfCode Day 3
def day3AdventOfCodePart2():
	f = open("input/inputDay3.txt","r")
	valeurARenvoyer = 0
	valeurFinale = 1
	indice = 0
	for x in f:
		if(indice > (len(x)-2)):
			indice = indice - (len(x)-1)
		if(x[indice] == '#'):
			valeurARenvoyer += 1
		indice += 1

	valeurFinale *= valeurARenvoyer
	valeurARenvoyer = 0
	indice = 0
	f = open("input/inputDay3.txt","r")
	for x in f:
		if(indice > (len(x)-2)):
			indice = indice - (len(x)-1)
		if(x[indice] == '#'):
			valeurARenvoyer += 1
		indice += 3
	valeurFinale *= valeurARenvoyer
	valeurARenvoyer = 0
	indice = 0
	f = open("input/inputDay3.txt","r")
	for x in f:
		if(indice > (len(x)-2)):
			indice = indice - (len(x)-1)
		if(x[indice] == '#'):
			valeurARenvoyer += 1
		indice += 5
	valeurFinale *= valeurARenvoyer
	valeurARenvoyer = 0
	indice = 0
	f = open("input/inputDay3.txt","r")
	for x in f:
		if(indice > (len(x)-2)):
			indice = indice - (len(x)-1)
		if(x[indice] == '#'):
			valeurARenvoyer += 1
		indice += 7
	valeurFinale *= valeurARenvoyer
	valeurARenvoyer = 0
	indice = 0
	valeurProfondeur = 0
	f = open("input/inputDay3.txt","r")
	for x in f:
		
		if(valeurProfondeur % 2 == 0):
			if(indice > (len(x)-2)):
				indice = indice - (len(x)-1)
			if(x[indice] == '#'):
				valeurARenvoyer += 1
			indice += 1
		valeurProfondeur += 1
	valeurFinale *= valeurARenvoyer
	valeurARenvoyer = 0
	indice = 0
	return valeurFinale
	
print(day3AdventOfCodePart1())
print(day3AdventOfCodePart2())

