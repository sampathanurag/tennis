# Tennis Scoring GUI Algorithm
# 14-2-17 15:00
# @Anurag A S
# Programming, Photography
# SJCE Mysuru
#------------------------------------------------
#Points in a single game
# Variable List
# A,B- Player A & Player B respectively
# pA,pB- Points of player A and Player B in a game respectively
# Wpoint - Winner of the given point - 1-Player A, 2-Player B
# Wpoint1 - Inputting the winner of the point from user in string datatype and checking for correctness of entered value(Error Catching)
# Game - Winner of the current Game 1-PLayer A ,2-Player B
# pAs,pBs - Points of player A and player B shown as 0,15,30,40,Adv-Advantage
# GW - Game Winner
# gN - Game Number
# Function returns the value 1 - Player A and 2 - Player 2
def game(A,B,gN):
	pA=0
	pB=0
	G=0
	print("Game Number:",gN)
	print(A,":",pA)
	print(B,":",pB)
	while G==0:
		print("Point won by?")
		Wpoint1 = input("->")
		if Wpoint1 != "1" and Wpoint1 !="2" :
			print("Error:Inavlid Value")
		else:
			Wpoint = int(Wpoint1)
			if Wpoint == 1:
				pA = pA + 1
			elif Wpoint == 2:
				pB = pB + 1
		# Algorithm for advantage and deuce
		#print(pA,pB) Checking the working of points system
		if (pA == pB) and pB>=3:
			print("Deuce")
		if (pA-pB) == 1 and pA>=4:
			print("Advantage A")
		elif (pB-pA) == 1 and pB>=4:
			print("Advantage B")
		pAs,pBs = pointsAssign(pA,pB)
		print(A,":",pAs)
		print(B,":",pBs)
		if (pA - pB >=2) and pA>=4:
			G = 1
		elif (pB - pA >=2) and pB>=4:
			G = 2
	if G == 1:
		GW = A
	elif G == 2:
		GW = B
	print("Game",GW)
	return(G)	


def pointsAssign(pA,pB):
	if (pA == pB) and (pA >= 4 or pB >=4):
		pAs="40"
		pBs="40"
	elif (pA-pB) == 1 and pA>=4:
		pAs="Adv"
		pBs="40"
	elif (pB-pA) == 1 and pB>=4:
		pBs="Adv"
		pAs="40"
	elif (pA-pB)>=2 and pA>=4:
		pAs="Game"
		pBs=" "
	elif (pB-pA)>=2 and pB>=4:
		pBs="Game"
		pAs=" "	
	else:
		if pA == 0:
			pAs = "0"
		elif pA == 1:
			pAs = "15"
		elif pA == 2:
			pAs = "30"
		elif pA == 3:
			pAs = "40"
		if pB == 0:
			pBs = "0"
		elif pB == 1:
			pBs = "15"
		elif pB == 2:
			pBs = "30"
		elif pB == 3:
			pBs = "40"
	return(pAs,pBs)
	
def tiebreak(A,B):
	G=0
	pA=0
	pB=0
	while G==0:
		print("Point won by?")
		Wpoint1 = input("->")
		if Wpoint1 != "1" and Wpoint1 !="2" :
			print("Error:Inavlid Value")
		else:
			Wpoint = int(Wpoint1)
			if Wpoint == 1:
				pA = pA + 1
			elif Wpoint == 2:
				pB = pB + 1
		print(A,":",pA)
		print(B,":",pB)
		if pA >= 7 and pA-pB>=2:
			G = 1
			return(pA,pB,G)
		elif pB >= 7 and pB-pA>=2:
			G = 2
			return(pA,pB,G)
			
		
