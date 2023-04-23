import string
import re
file = open("day3.txt", "r")
filecontent = file.readlines()
alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

threelinesplit = []
temarray = []
for line in filecontent:
	temarray.append(line.replace("\n", ""))
	if len(temarray) == 3:
		threelinesplit.append(temarray)
		temarray = []



groupletter = []
temarray = []
for group in threelinesplit:
	for letter in group[0]:
		if letter in group[1]:
			if letter in group[2]:
				if letter not in temarray:
					
					temarray.append(letter)
					
	groupletter += temarray
	temarray = []
print(groupletter)


	

faultlist = []
numreturn = 0

for line in filecontent:
	compartment1 = line[:len(line)//2]
	compartment2 = line[len(line)//2:]

	faultlinetem = []
	for letter in compartment1:
		if letter in compartment2:
			if letter not in faultlinetem:
				faultlinetem.append(letter)
	faultlist += faultlinetem


for char in groupletter:
	numreturn += alphabets.index(char) + 1

print(numreturn)
	