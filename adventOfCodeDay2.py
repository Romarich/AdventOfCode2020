#Part 1 AdventOfCode Day 2
def day2AdventOfCodePart1():
	f = open("input.txt","r")
	compteurFinal = 0
	for x in f:
		element = x.split(" ");
		bonTableau = element[0].split("-")
		bonTableau.append(element[1].split(":")[0])
		bonTableau.append(element[2].split("\n")[0])
		compteurLettre = 0
		for i in bonTableau[3]:
			if i == bonTableau[2]:
				compteurLettre += 1
		if compteurLettre >= int(bonTableau[0]) and compteurLettre <= int(bonTableau[1]):
			compteurFinal += 1
	print(compteurFinal)

#Part 2 AdventOfCode Day 2
def day2AdventOfCodePart2():
	f = open("input.txt","r")
	compteurFinal = 0
	for x in f:
		element = x.split(" ");
		bonTableau = element[0].split("-")
		bonTableau.append(element[1].split(":")[0])
		bonTableau.append(element[2].split("\n")[0])
		compteurLettre = 1
		firstIsOk = False
		secondIsOk = False
		if bonTableau[3][int(bonTableau[0])-1] == bonTableau[2]:
			firstIsOk = True
		if bonTableau[3][int(bonTableau[1])-1] == bonTableau[2]:
			secondIsOk = True
		if firstIsOk and not secondIsOk:
			compteurFinal += 1
		elif not firstIsOk and secondIsOk:
			compteurFinal += 1
	print(compteurFinal)

day2AdventOfCodePart1();
day2AdventOfCodePart2();