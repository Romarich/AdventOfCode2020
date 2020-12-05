#Part 1 AdventOfCode Day 5
def day5AdventOfCodePart1():
	f = open("input/inputDay5.txt","r")
	valeurARenvoyer = 0
	numeroLigne = 0
	row = 0
	column = 0
	listOfSeatId = []
	for x in f:
		downRow = 0
		upRow = 127
		downColumn = 0
		upColumn = 7
		x= x.replace("\n","")
		for i in range(0,7):
			if i == 6:
				if x[i] == "F":
					row = downRow
				if x[i] == "B":
					row = upRow
			else:
				if x[i] == "F":
					if (upRow - downRow)%2 != 0:
						upRow = upRow - int((upRow - downRow +1)/2)
						upRow = int(upRow)
					else:
						upRow = upRow - int((upRow - downRow)/2)
						upRow = int(upRow)
				if x[i] == "B":
					if (upRow - downRow)%2 != 0:
						downRow = downRow + int((upRow - downRow + 1)/2)
						downRow = int(downRow)
					else:
						downRow = downRow + int((upRow - downRow)/2)
						downRow = int(downRow)
		for j in range(7,10):
			if j == 9:
				if x[j] == "R":
					column = upColumn
				if x[j] == "L":
					column = downColumn
			else:
				if x[j] == "L":
					if (upColumn - downColumn)%2 != 0:
						upColumn = upColumn - int((upColumn - downColumn + 1)/2)
						upColumn = int(upColumn)
					else:
						upColumn = upColumn- int((upColumn - downColumn)/2)
						upColumn = int(upColumn)
				if x[j] == "R":
					if (upColumn - downColumn)%2 != 0:
						downColumn = downColumn + int((upColumn - downColumn + 1)/2)
						downColumn = int(downColumn)
					else:
						downColumn = downColumn + int((upColumn - downColumn)/2)
						downColumn = int(downColumn)
		seatId = (row * 8) + column
		if valeurARenvoyer < seatId:
			valeurARenvoyer = seatId

	return valeurARenvoyer
	
#Part 2 AdventOfCode Day 5
def day5AdventOfCodePart2():
	f = open("input/inputDay5.txt","r")
	valeurARenvoyer = 0
	numeroLigne = 0
	row = 0
	column = 0
	listOfSeatId = []
	for x in f:
		downRow = 0
		upRow = 127
		downColumn = 0
		upColumn = 7
		x= x.replace("\n","")
		for i in range(0,7):
			if i == 6:
				if x[i] == "F":
					row = downRow
				if x[i] == "B":
					row = upRow
			else:
				if x[i] == "F":
					if (upRow - downRow)%2 != 0:
						upRow = upRow - int((upRow - downRow +1)/2)
						upRow = int(upRow)
					else:
						upRow = upRow - int((upRow - downRow)/2)
						upRow = int(upRow)
				if x[i] == "B":
					if (upRow - downRow)%2 != 0:
						downRow = downRow + int((upRow - downRow + 1)/2)
						downRow = int(downRow)
					else:
						downRow = downRow + int((upRow - downRow)/2)
						downRow = int(downRow)
		for j in range(7,10):
			if j == 9:
				if x[j] == "R":
					column = upColumn
				if x[j] == "L":
					column = downColumn
			else:
				if x[j] == "L":
					if (upColumn - downColumn)%2 != 0:
						upColumn = upColumn - int((upColumn - downColumn + 1)/2)
						upColumn = int(upColumn)
					else:
						upColumn = upColumn- int((upColumn - downColumn)/2)
						upColumn = int(upColumn)
				if x[j] == "R":
					if (upColumn - downColumn)%2 != 0:
						downColumn = downColumn + int((upColumn - downColumn + 1)/2)
						downColumn = int(downColumn)
					else:
						downColumn = downColumn + int((upColumn - downColumn)/2)
						downColumn = int(downColumn)
		seatId = (row * 8) + column
		listOfSeatId.append(seatId)
	listOfSeatId.sort()	
	seatNotThere = []
	for i in range(listOfSeatId[0],listOfSeatId[len(listOfSeatId)-1]):
		if i not in listOfSeatId:
			seatNotThere.append(i)
	return seatNotThere
	
#print(day5AdventOfCodePart1())
print(day5AdventOfCodePart2())


