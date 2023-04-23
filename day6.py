file = open("day6.txt", "r")
filecontent = file.readlines()
print(len(filecontent[0]))
text = ""
for letter in range(len(filecontent[0]) - 14):
	text = filecontent[0][letter] + filecontent[0][letter + 1] + filecontent[0][letter + 2] + filecontent[0][letter + 3] + filecontent[0][letter + 4] + filecontent[0][letter + 5]+ filecontent[0][letter + 6]+ filecontent[0][letter + 7]+ filecontent[0][letter + 8]+ filecontent[0][letter + 9] + filecontent[0][letter + 10] + filecontent[0][letter + 11] + filecontent[0][letter + 12] + filecontent[0][letter + 13]
	temarray = []
	for i in text:
		if i not in temarray:
			temarray.append(i)
	#print(temarray)
	if len(temarray) == 14:
		print(letter + 1 + 13)
		break