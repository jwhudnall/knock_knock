#This version is designed for multiple players.
#Future change should give an upper limit (10?)

#Knock Knock is a card game in which players start with 3 cards. Each successive round adds an additional card, all the way through 13.
#A player wins a round when all the cards they hold are either part of:
#a set of any suit (minimum of 3; ex: 3 Queens of different suits) or
#a run of the same suit (minimum of 3; ex: 4,5,6 of Hearts).

#Players with cards that do not belong to a set or run outlined above will have them counted against them if another player knocks,
#as follows:
#1-9 = 5 points 
#10-King = 10 points
#Ace = 15 points

#Points are bad! After 13 rounds have been played, the player with the least score wins.
#Points are doubled for rounds 12 and 13 


#Game starts with 3 cards i.e. hand = 3
players = {}
hand = 3
while True:
	try:
		player_count = int(input("Number of players: "))
	except ValueError:
		print("Please enter a number. ")
	else:
		break

#Populates the players dictionary with default scores of 0.

for num in range(1,player_count+1): 
	name = input(f"Who is player {num}? ")
	players.update({name.title(): 0})

#rounds 3 through 10
while hand <=10:
	print(f"We're on round {hand}.\n{hand}'s and Jokers are wild.\nDeal those cards!")
	print("*" * 30)
	while True:
		knocker = input(f"For round {hand}, who knocked? ")
		if knocker.title() not in players:
			print("Please enter a valid player name.")
		else:
			break

#loops through players dictionary and adds points for all players. The knocker is exempt.
	for k,v in players.items():
		if k.title() == knocker.title():
			round_winner = k.title() #establishes who won, but doesn't announce it. 
		else:
			while True: #ensures an integer is given
				try:
					point_accrual = int(input(f"How many points did {k.title()} have? "))
				except ValueError:
					print("Please enter a number. ")
				else:
					break
			players[k] += point_accrual
	print("="*30)
	print(f"At the end of round {hand}, the scores are: ")
	for player,points in players.items():
		print(f"{player}: {points}")

	print("="*30)
	hand += 1


#round 11
print(f"We're on round {hand}.\n Jacks and Jokers are wild.\n Deal those cards!")
print("*" * 20)
while True:
	knocker = input(f"For round {hand}, who knocked? ")
	if knocker.title() not in players:
		print("Please enter a valid player name.")
	else:
		break

#loops through players dictionary and adds points for all players. The knocker is exempt.
for k,v in players.items():
	if k.title() == knocker.title():
		round_winner = k.title() #establishes who won, but doesn't announce it. 
	else:
		while True: #ensures an integer is given
			try:
				point_accrual = int(input(f"How many points did {k.title()} have? "))
			except ValueError:
				print("Please enter a number. ")
			else:
				break
		players[k] += point_accrual
print(f"At the end of round {hand}, the scores are:\n{players}")
print("="*30)
hand += 1

#round12 = double points
print(f"We're on round {hand}.\n Queens and Jokers are wild, and points are doubled.\nDeal those cards!")
print("*" * 20)
while True:
	knocker = input(f"For round {hand}, who knocked? ")
	if knocker.title() not in players:
		print("Please enter a valid player name.")
	else:
		break

#loops through players dictionary and adds points for all players. The knocker is exempt.
for k,v in players.items():
	if k.title() == knocker.title():
		round_winner = k.title() #establishes who won, but doesn't announce it. 
	else:
		while True: #ensures an integer is given
			try:
				point_accrual = int(input(f"How many points did {k.title()} have? "))
			except ValueError:
				print("Please enter a number. ")
			else:
				break
		players[k] += point_accrual * 2
print(f"At the end of round {hand}, the scores are:\n{players}")
print("="*30)
hand += 1

#round13 = double points. Last round!
print(f"Last round of the game!\n Kings and Jokers are wild, and points are doubled.\nDeal those cards!")
print("*" * 20)
while True:
	knocker = input(f"For round {hand}, who knocked? ")
	if knocker.title() not in players:
		print("Please enter a valid player name.")
	else:
		break

#loops through players dictionary and adds points for all players. The knocker is exempt.
for k,v in players.items():
	if k.title() == knocker.title():
		round_winner = k.title() #establishes who won, but doesn't announce it. 
	else:
		while True: #ensures an integer is given
			try:
				point_accrual = int(input(f"How many points did {k.title()} have? "))
			except ValueError:
				print("Please enter a number. ")
			else:
				break
		players[k] += point_accrual * 2
print(f"At the end of the game, the final scores are:\n{players}")
print("="*30)

#Determines who won. Lower score is better
winner = min(players, key=players.get)
print("*"*30)
print("*"*30)
print("*"*30)
print(f"Congratulations, {winner} is the winner! ")
print("*"*30)
print("*"*30)
print("*"*30)




