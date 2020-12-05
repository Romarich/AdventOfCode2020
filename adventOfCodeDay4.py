import re
#Part 1 AdventOfCode Day 4
def day4AdventOfCodePart1():
	f = open("input/inputDay4.txt","r")
	valeurARenvoyer = 0
	passeport = {}
	for x in f:
		print(x)
		print(len(x))
		if len(x) > 1:
			element = x.split(" ")
			for i in element:
				elementPrecis = i.replace("\n","").split(":")
				passeport[elementPrecis[0]] = elementPrecis[1]
				print(passeport)
		else:
			#print(passeport)
			if "hgt" not in passeport:
				print("invalid")
			elif "cid" not in passeport:
				if "ecl" not in passeport or "pid" not in passeport or "eyr" not in passeport or "hcl" not in passeport or "byr" not in passeport or "iyr" not in passeport or "hgt" not in passeport: 
					print("invalid")
				else:
					valeurARenvoyer += 1
			else:
				if "byr" in passeport and "iyr" in passeport and "eyr" in passeport and "hgt" in passeport and "hcl" in passeport and "ecl" in passeport and "pid" in passeport and "cid" in passeport:
					valeurARenvoyer += 1
			"""if 'ecl' in passeport and 'pid' in passeport and 'eyr' in passeport and 'hcl' in passeport and 'byr' in passeport and 'iyr' in passeport and 'cid' in passeport and 'hgt' in passeport:
				valeurARenvoyer += 1
			elif 'hgt' not in passeport:
				print("invalid")
			elif 'cid' not in passeport:
				if 'ecl' in passeport and 'pid' in passeport and 'eyr' in passeport and 'hcl' in passeport and 'byr' in passeport and 'iyr' in passeport and 'hgt' in passeport:
					#print("")
					valeurARenvoyer += 1
				else:
					print("invalid")
			"""	#verification passeport
				#print(passeport)
			passeport = {}
	return valeurARenvoyer



#Part 2 AdventOfCode Day 4
def day4AdventOfCodePart2(file):
	f = open("input/inputDay4.txt","r")
	valeurARenvoyer = 0	
	passeport = {}
	for x in f:
		#print(x)
		#print(len(x))
		if len(x) > 1:
			element = x.split(" ")
			for i in element:
				elementPrecis = i.replace("\n","").split(":")
				passeport[elementPrecis[0]] = elementPrecis[1]
				#print(passeport)
		else:
			#print(passeport)
			if "hgt" not in passeport:
				print("")
			elif "cid" not in passeport:
				if "ecl" not in passeport or "pid" not in passeport or "eyr" not in passeport or "hcl" not in passeport or "byr" not in passeport or "iyr" not in passeport or "hgt" not in passeport: 
					print("")
				else:
					if verificationValeur(passeport):
						valeurARenvoyer+=1
					
			else:
				if "byr" in passeport and "iyr" in passeport and "eyr" in passeport and "hgt" in passeport and "hcl" in passeport and "ecl" in passeport and "pid" in passeport and "cid" in passeport:
					if verificationValeur(passeport):
						valeurARenvoyer+=1
					
			"""if 'ecl' in passeport and 'pid' in passeport and 'eyr' in passeport and 'hcl' in passeport and 'byr' in passeport and 'iyr' in passeport and 'cid' in passeport and 'hgt' in passeport:
				valeurARenvoyer += 1
			elif 'hgt' not in passeport:
				print("invalid")
			elif 'cid' not in passeport:
				if 'ecl' in passeport and 'pid' in passeport and 'eyr' in passeport and 'hcl' in passeport and 'byr' in passeport and 'iyr' in passeport and 'hgt' in passeport:
					#print("")
					valeurARenvoyer += 1
				else:
					print("invalid")
			"""	#verification passeport
				#print(passeport)
			passeport = {}
	return valeurARenvoyer

def verificationValeur(passeport):
	verification = 0
	if int(passeport["byr"]) >= 1920 and int(passeport["byr"]) <= 2002:
		verification += 1
	if int(passeport["iyr"]) >= 2010 and int(passeport["iyr"]) <= 2020:
		verification += 1
	if int(passeport["eyr"]) >= 2020 and int(passeport["eyr"]) <= 2030:
		verification += 1
	if "cm" in passeport["hgt"] and int(passeport["hgt"].replace("cm","")) >= 150 and int(passeport["hgt"].replace("cm","")) <= 193:
		verification += 1
	elif "in" in passeport["hgt"] and int(passeport["hgt"].replace("in","")) >= 59 and int(passeport["hgt"].replace("in","")) <= 76:
		verification += 1
	if passeport["hcl"][0] == '#' and len(passeport["hcl"]) == 7:
		verification += 1
		#print(passeport["hcl"])
		"""if re.match("^[a-f0-9]*$", passeport["hcl"]):
			print("test")
			print(passport["hcl"])
		"""
	if passeport["ecl"] == "amb" or passeport["ecl"] == "blu" or passeport["ecl"] == "brn" or passeport["ecl"] == "gry" or passeport["ecl"] == "grn" or passeport["ecl"] == "hzl" or passeport["ecl"] == "oth":
		verification += 1
	if len(passeport["pid"]) == 9:
		verification += 1
	print(verification)	
	if verification == 7:
		return True
	return False

	
#test("input/inputDay4.txt")	
#print(day4AdventOfCodePart1())
print(day4AdventOfCodePart2("input/inputDay4.txt"))

