# Tennis Scoring GUI Algorithm
# 14-2-17 15:00
# @Anurag A S
# Programming, Photography
# SJCE Mysuru
#---------------------------------------------------------------------------------------------------------------------------------------------
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
# Games and sets in a sets in a match
# Sets function:
# First player to reach 6 games with a difference of 2 wins ie 6-4 or 7-5
# Variable List
# gA, gB are the games in a set
# S Winner of the set
# gN Game Number
# sN Set Number
# M - Match Won 1-Player A , 2- Player B
# sA, sB Number of sets won by each player
# scA, scB Score of each set by Player A and Player B
#-----------------------------------------------------------------------------------------------------------------------------------------------
from tennis1 import*
from tennis2 import*
def match(A,B):
	sA = 0
	sB = 0
	sN = 1
	M = 0
	scA = []
	scB = []
	while M==0:
		(gA,gB,G) = set(A,B,sN)
		scA.append(gA)
		scB.append(gB)
		print(A,"||",scA)
		print(B,"||",scB)
		sN = sN+1
		if G == 1:
			sA += 1
		elif G == 2:
			sB += 1
		if sA == 2 and sB == 2:
			(gA,gB,M) = nobreak(A,B,sN)
		elif sA == 3 and (sB == 0 or sB == 1):
			M = 1
		elif sB == 3 and (sA == 0 or sA == 1):
			M = 2
	print("-"*50)
	print(A,"||",scA)
	print(B,"||",scB)
	if M == 1:
		return(A)
	elif M == 2:
		return(B)
		
match("Anurag","Ram")
