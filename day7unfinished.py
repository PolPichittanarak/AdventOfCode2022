file = open("day7test.txt", "r")
filecontent = file.readlines()


filepath = []
print(filecontent)
currentdir = ""
for line in filecontent:
	linelist = line.split(" ")
	print(linelist)
	if linelist[0] == "$": # command
		if len(linelist) == 3:
			temdir = linelist[2].replace("\n", "")
			if temdir == "/": 
				currentdir = ""
			else:
				currentdir = temdir

		
	elif linelist[0] == "dir": #create directory
		for index, value in enumerate(filepath):
			if currentdir == "":
				filepath.append([linelist[1].replace("\n", "")])
			elif value[0] == currentdir:
				filepath[index].append([linelist[1].replace("\n", "")])
	elif linelist[0].isnumeric():
		for index, value in enumerate(filepath):
			if currentdir == "":
				filepath.append([linelist[1].replace("\n", ""), linelist[0]])
			elif value[0] == currentdir:
				filepath.append([linelist[1].replace("\n", ""), linelist[0]])
	

print(filepath)
		
	