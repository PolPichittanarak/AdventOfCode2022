file = open("day4.txt", "r")
filecontent = file.readlines()
count = 0
count1 = 0
for line in filecontent:
	line = line.replace("\n", "")
	linesplit = line.split(",")
	#print(linesplit)
	listone = []
	ponelist = linesplit[0].split("-")
	#print(ponelist)
	for num1 in range(int(ponelist[0]), int(ponelist[1]) + 1):
		listone.append(num1)
	#print("listone: ", end="")
	#print(listone)

	listtwo = []
	ptwolist = linesplit[1].split("-")
	#print(ptwolist)
	for num2 in range(int(ptwolist[0]), int(ptwolist[1]) + 1):
		listtwo.append(num2)

	overlap = False

	for number in listone:
		if number in listtwo:
			overlap = True

	if overlap == True:
		count1 += 1
	#print("listtwo: ", end="")
	#print(listtwo)

	#print()

	#if listtwo[0] in listone and listtwo[-1] in listone:
		#count += 1
		#print("1 over 2", end=" ")
		#print(line)

	#elif listone[0] in listtwo and listone[-1] in listtwo:
			#count += 1
			#print("2 over 1", end=" ")
			#print(line)
			
	#if int(ponelist[0]) >  int(ptwolist[0]) and int(ponelist[1]) < int(ptwolist[1]):
		#count += 1
		#print("condition1 True", line)

	#elif int(ptwolist[0]) > int(ponelist[0]) and int(ptwolist[1]) < int(ponelist[1]):
		#count += 1
			#print("condition2 True", line)
	#if int(ponelist[1]) < int(ptwolist[0]) or int(ptwolist[0]) > int(ponelist[1]):
		#count1 += 1

print(count1)
	