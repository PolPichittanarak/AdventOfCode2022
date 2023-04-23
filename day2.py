file = open("day2.txt", "r")
filecontent = file.readlines()
#A for Rock, B for Paper, and C for Scissors
#X for Lose, Y for Draw, and Z for Win
#1 for Rock, 2 for Paper, and 3 for Scissors

score = 0

for round in filecontent:
	#print(round)
	player1 = round.split(" ")[0]
	player2 = round.split(" ")[1]
	player2 = player2.replace("\n", "")

	
	if player2 == "X" and player1 == "A": #scissor
		score += 3

	elif player2 == "X" and player1 == "B": #rock
		score += 1

	elif player2 == "X" and player1 == "C": #paper
		score += 2

	elif player2 == "Y" and player1 == "A": #rock
		score += 4

	elif player2 == "Y" and player1 == "B": # paper
		score += 5

	elif player2 == "Y" and player1 == "C": #scissor
		score += 6

	elif player2 == "Z" and player1 == "A": #Paper
		score += 8

	elif player2 == "Z" and player1 == "B": #scissor
		score += 9

	elif player2 == "Z" and player1 == "C": #rock
		score += 7
	#print(score)
print(score)