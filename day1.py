file = open("day1.txt", "r")
calories = file.readlines()



callist = list(calories)
calorder = []
tem = 0
max = 0
for elf in callist:
	#print(elf)
	if elf == ("\n"):
		calorder.append(tem)
		if tem >= max:
			max = tem
		tem = 0
	else: 
		elf = elf.replace("\n", "")
		tem = tem + int(elf)

calorder = sorted(calorder, reverse = True)
print(calorder[0] + calorder[2] +calorder[1])
print(max)
