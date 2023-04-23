file = open("day8test.txt", "r")
filecontent = file.readlines()

map = []

for i in filecontent:
	temmap = []
	for tree in i:
		if tree != "\n":
			temmap.append(tree)
	map.append(temmap)
	
count = 0

def horizontalcheck(row):
	count1 = 0

	for index, tree in enumerate(row):
		if index == 0 or index ==len(row) - 1:
			pass
		elif tree > row[index - 1]:
			count1 += 1

for indexy, horizontal in enumerate(map):
	if indexy == 0 or indexy == len(map) - 1:
		count += len(horizontal)
		print("first count:", str(count))
	else:
		count += horizontalcheck(horizontal)
		
	for indexx, vertical in enumerate(horizontal):
		if indexy != 0 and indexy != len(vertical) - 1:
			if indexx == 0 or indexx == len(vertical) - 1:
				count += 1
		
print(count)
print(map)
	
	