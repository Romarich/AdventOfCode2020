#Part 1 AdventOfCode Day 1
def day1AdventOfCodePart1():
	f = open("input/inputDay1.txt","r")
	tab = []
	for i in f:
		tab.append(i.split("\n")[0])
	
	for i in tab:
		for j in tab:
			if i != j and int(i)+int(j) == 2020:
				return(int(i)*int(j))
	#print(tab)

#Part 2 AdventOfCode Day 1
def day1AdventOfCodePart2():
	f = open("input/inputDay1.txt","r")
	tab = []
	for i in f:
		tab.append(i.split("\n")[0])
	
	for i in tab:
		for j in tab:
			for h in tab:
				if i != j and j != h and h != i and int(i)+int(j)+int(h) == 2020:
					return(int(i)*int(j)*int(h))
	
print(day1AdventOfCodePart1())
print(day1AdventOfCodePart2())

