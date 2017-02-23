# # Tennis Scoring GUI Algorithm
# 14-2-17 15:00
# @Anurag A S
# Programming, Photography
# SJCE Mysuru
#------------------------------------------------
from tennis1 import*
# Games and sets in a sets in a match
# Sets function:
# First player to reach 6 games with a difference of 2 wins ie 6-4 or 7-5
# Variable List
# gA, gB are the games in a set
# S Winner of the set
# gN Game Number
# sN Set Number
def set(A,B,sN):
	gA = 0
	gB = 0
	S=0
	gN = 1
	print("Set Number::",sN)
	print(A,"::",gA)
	print(B,"::",gB)
	while S == 0:
		G = game(A,B,gN)
		if G == 1:
			gA += 1
		elif G == 2:
			gB += 1
		if (gA == 6 and gB <=4) or (gA == 7 and gB <= 5):
			S = 1
		elif (gB == 6 and gA <=4) or (gB == 7 and gA <= 5):
			S = 2
		elif gA ==6 and gB ==6:
			print(A,"::",gA)
			print(B,"::",gB)
			print("TieBreak")
			(pA,pB,G)=tiebreak(A,B)
			S=G
			if G == 1:
				gA = [7,pA]
				gb = [6,pB]
			elif G == 2 :
				gA = [6,pA]
				gB = [7,pB]
		print(A,"::",gA)
		print(B,"::",gB)
		gN += 1
	return(gA,gB,G)
		
def nobreak(A,B,sN):
	gA = 0
	gB = 0
	S=0
	gN = 1
	print("Set Number::",sN)
	print(A,"::",gA)
	print(B,"::",gB)
	while S == 0:
		G = game(A,B,gN)
		if G == 1:
			gA += 1
		elif G == 2:
			gB += 1
		if (gA >= 6 and gA-gB >=2):
			S = 1
		elif (gB >= 6 and gB-gA >=2):
			S = 2
	return(gA,gB,S)
		
		
