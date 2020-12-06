tabAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Part 1 AdventOfCode Day 6
def day6AdventOfCodePart1():
	f = open("input/inputDay6.txt","r")
	valeurARenvoyer = 0
	answerString = "";
	for x in f:
		if x == "\n":
			valeurARenvoyer += verification(answerString)
			answerString = ""
		else:
			answerString = answerString+x.replace("\n","")
	return valeurARenvoyer

def verification(answerString):
	print(answerString)
	valeur = 0
	for i in range(0,len(tabAlphabet)):
		if tabAlphabet[i] in answerString:
			valeur += 1
	print(valeur)
	return valeur

#Part 2 AdventOfCode Day 6
def day6AdventOfCodePart2():
	f = open("input/inputDay6.txt","r")
	valeurARenvoyer = 0
	answerString = "";
	nombreDePersonnes = 0
	for x in f:
		if x == "\n":
			valeurARenvoyer += verificationPart2(answerString,nombreDePersonnes)
			answerString = ""
			nombreDePersonnes = 0
		else:
			answerString = answerString+x.replace("\n","")
			nombreDePersonnes+=1
	return valeurARenvoyer

def verificationPart2(answerString,nombreDePersonnes):
	print(answerString)
	valeur = 0
	for i in range(0,len(tabAlphabet)):
		if(answerString.count(tabAlphabet[i]) == nombreDePersonnes):
			valeur += 1
	print(valeur)
	return valeur
	
#print(day6AdventOfCodePart1())
print(day6AdventOfCodePart2())
