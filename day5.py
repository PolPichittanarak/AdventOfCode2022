import string
file = open("day5.txt", "r")
filecontent = file.readlines()
lettermap = list()

stacks = [["B", "L","D", "T","W", "C","F", "M",], ["N", "B", "L"], ["J", "C","H", "T","L", "V"],["S", "P","J", "W"], ["Z", "S","C", "F","T", "L","R"], ["W", "D","G", "B","H", "N","Z"], ["F", "M","S", "P","V", "G","C", "N"], ["W", "Q","R", "J","F", "V","C", "Z"], ["R", "P","M", "L","H"]]

moveint = []
intflag = False
for line in filecontent:
	if intflag:
		moveint.append(line.replace("\n", ""))
	if line == "\n":
		intflag = True
#move 1, 2 to 1
for instruction in moveint:
	intlist = instruction.split(" from ")
	quantity = int(intlist[0].replace("move ", ""))
	direction = intlist[1].strip().split(" to ")

	origin = int(direction[0])
	target = int(direction[1])
	#print("origin: ", str(origin))
	#print("target: ", str(target))

	for move in range(quantity * -1, 0, 1):
		stacks[target - 1].append(stacks[origin - 1][move])
		stacks[origin - 1].pop(move)
		
		
#print(stacks)
for i in stacks:
	print(i[-1], end = "")