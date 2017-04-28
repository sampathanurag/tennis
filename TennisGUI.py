# -*- coding: iso-8859-1 -*-
#!/usr/bin/python

# Tennis Scoring GUI Algorithm
# 15-3-17 21:08
# @Anurag A S

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
#---------------------------------------------------
# Games and sets in a sets in a match
# Sets function:
# First player to reach 6 games with a difference of 2 wins ie 6-4 or 7-5
# Variable List
# gA, gB are the games in a set
# S Winner of the set
# gN Game Number
# sN Set Number
# Q - Server
# Qs - Server for the set
#-----------------------------------------------------
# To do list
# 1 - Serve - Done
# 2 - Break Point - Done
# 3 - No. of break points won
# 4 - Image of ball for serve - Done
#-------------------------------------------------------


import time;



from tkinter import *
from sup import*
from sys import argv
global pname1
global Q
global pname2
script  , pname1, pname2 , Q = argv
global plabel


global pA
global pB
global pAs
global pBs
global G
global gN
gN = 0
pA = 0
pB = 0
global gA,gB
gA = 0
gB = 0
global sA ,sB
sA = 0
sB = 0 
global M
M = 0
global fl
fl = 0
global sN
#global Q
sN = 1
global scA ,scB
scA = ""
scB = ""
Q = int(Q)
global Qs
Qs = Q
print("Qs == ",Qs)

def match(sA,sB):
  M = 0
  global pname1,pname2
  #if sA == 2 and sB == 2:
    #(gA,gB,M) = nobreak(A,B,sN)
  if sA == 3 and (sB == 0 or sB == 1 or sB == 2):
    M = 1
  elif sB == 3 and (sA == 0 or sA == 1 or sA == 2):
    M = 2
  #print("-"*50)
  return(M)
    
    
    
    
    
    
    
    









def set(gA , gB):
  S = 0
  global sN
  global pname1,pname2
  #print("Set Number::",sN)
  print(pname1,"::",gA)
  print(pname2,"::",gB)
  if (gA == 6 and gB <=4) or (gA == 7 and gB <= 5) or (gA>=6 and gA-gB==2) or (gA == 7 and gB == 6 and sN != 5):
    S = 1
  elif (gB == 6 and gA <=4) or (gB == 7 and gA <= 5) or (gB>=6 and gB-gA==2) or (gA == 6 and gB == 7 and sN != 5):
       S = 2
  #elif gA ==6 and gB ==6:
  # print(A,"::",gA)
  # print(B,"::",gB)
  #   print("TieBreak")
  #   (pA,pB,G)=tiebreak(A,B)
  #   S=G                                             TIEBREAK CLAUSE
  #   if G == 1:
  #     gA = [7,pA]
  #     gb = [6,pB]
  #   elif G == 2 :
  #     gA = [6,pA]
  #     gB = [7,pB]
  # print(A,"::",gA)
  # print(B,"::",gB)
  # gN += 1
  return(S)
  
  
  
  
  
  
  
  
  

def game(pA,pB,fl):
  G=0
  global pAs,pBs
  global gA,gB
  global pname1,pname2
  #print("Game Number:",gN)
  print(pname1,":",pA)
  print(pname2,":",pB)
    #print("Point won by?")
    #Wpoint1 = input("->")
    #if Wpoint1 != "1" and Wpoint1 !="2" :
    # print("Error:Inavlid Value")
    #else:
    # Wpoint = int(Wpoint1)
    # if Wpoint == 1:
    #   pA = pA + 1
    # elif Wpoint == 2:
    #   pB = pB + 1
    # Algorithm for advantage and deuce
    #print(pA,pB) Checking the working of points system
  if fl == 0:
    if (pA == pB) and pB>=3:
      print("Deuce")
    elif (pA-pB) == 1 and pA>=4:
      print("Advantage A")
    elif (pB-pA) == 1 and pB>=4:
      print("Advantage B")
    #pAs,pBs = pointsAssign(pA,pB)
    #print(pname1,":",pAs)
    #print(pname2,":",pBs)
    if (pA - pB >=2) and pA>=4:
      G = 1
    elif (pB - pA >=2) and pB>=4:
      G = 2
    #if G == 1:
      #GW = A
    #elif G == 2:
      #GW = B
    #print("Game",GW)
  elif fl == 1:
    if (pA - pB >=2) and pA>=7:
      G = 1
    elif (pB - pA >=2) and pB>=7:
      G = 2
  return(G) 




def pointsAssign(pA,pB,fl):
        global G
        if sN == 5:
          fl = 0
        if fl == 0:
                if (pA-pB) == 1 and (pA>=4):
                    pAs = "Adv"
                    pBs = "40"
                elif (pA == pB) and (pA>=4 or pB>=4):
                    pAs = "40"
                    pBs = "40"
                elif (pB-pA) == 1 and (pB>=4):
                    pBs="Adv"
                    pAs="40"
                elif (pA-pB)>=2 and pA>=4:
                    pAs = "Game"
                    pBs  = " "
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
                G = game(pA,pB , fl)
        elif fl == 1:
                pAs = pA
                pBs = pB
                G = game(pA ,pB , fl)
        return(pAs,pBs,G)


    

  

      
      
      
      
      
      
      
      
      
      
      
      
print("QQQQQQQQQQQQQQQ",Q)    
      
      
      
      
      
      
      
      

# Empty Label
#label = Label(self,anchor="w",fg="white")
#label.grid(column=1,row=0,columnspan=2,sticky='EW')
global year
global month
global day
global hour
global min
global sec
global date
global time


class Application(Frame):
  global year
  global month
  global day
  global hour
  global min
  global sec
  global date
  global time
  global Q
  global Qs
  # Time 
  global pA,pB
  global pAs,pBs
  global M
  
  def pl1(self):
    global M
    if M == 0:
      global pname1,pname2
      global pA,pB
      global pAs,pBs
      global gA,gB
      global sA , sB , fl
      global sN
      global scA , scB
      global S
      global Q
      global Qs

      sN = sA + sB + 1
      pA=pA+1
      a = 1
      print("SN",sN)
      if gA == 6 and gB == 6 and sN == 5:
        fl = 0
      elif gA == 6 and gB == 6 and sN != 5:
        fl = 1
      print("FL",fl)
      pAs, pBs , G = pointsAssign(pA,pB,fl)
      print (G)
      print(pAs,pBs)
      self.plabel1.set(pname1)
      #self.plabel2.set("")
      self.point1label.set(pAs)
      self.point2label.set(pBs) 


      if G == 1 and fl == 0:
        gA+=1
        #print(fl)
        self.game1label.set(gA)
        self.game2label.set(gB)
        pA = 0
        pB = 0
        print("--------------")
        self.clabel.set("Game")
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
      elif G == 2 and fl == 0:
        gB+=1
        #print(fl)
        self.game1label.set(gA)
        self.game2label.set(gB)
        pA = 0
        pB = 0
        print("--------------")
        self.clabel.set("Game")
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
      elif G == 1 and fl == 1:
        pA = 0
        #print(fl)
        pB = 0
        gA = 7
        gB = 6
        fl = 0
        self.game1label.set(gA)
        self.game2label.set(gB)
        self.clabel.set("Game")
        print("--------------")
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
      elif G == 2 and fl == 1:
        pA = 0
        pB = 0
        gB = 7
        #print(fl)
        gA = 6
        fl = 0
        self.game1label.set(gA)
        self.game2label.set(gB)
        print("--------------")
        self.clabel.set("Game")
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0

          
      S = set(gA,gB)
      #print(S)
      if G == 1 or G == 2:
        self.clabel.set("Game")
      elif  pAs == "Adv" :
        self.clabel.set("Adv")
      elif (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
        self.clabel.set("Game Point") 
      elif pBs == "Adv" :
        self.clabel.set("Adv")
      elif(pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
        self.clabel.set("Game Point")
      elif pAs == "40" and pBs == "40":
        self.clabel.set("Deuce")
      else:
        self.clabel.set("")
        #########################
      if Q == 1:
        if pBs == "Adv":
          self.clabel.set("Break Point")
        elif pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30"):
          self.clabel.set("Break Point")
      elif Q == 2:
        if pAs == "Adv":
          self.clabel.set("Break Point")
        elif pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30"):
          self.clabel.set("Break Point")

      if ( gA == 5 and gB <=4) or (gA == 6 and gB == 5):
        if  pAs == "Adv" or (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
          self.clabel.set("Set Point") 
      elif (gA == 6 and gB == 6 and sN != 5):
        if (pA >= 6 and pA-pB>=1) or (pB >= 6 and pB-pA>=1):
          print("----------------------------------------------------------------------------------------------------")
          self.clabel.set("Set Point")
        if pA == 0 and pB == 0:
          self.clabel.set("Tie Break!")
      elif (gA == 5 and gB <=4) or (gB ==6 and gA == 5):
        if pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
          self.clabel.set("Set Point") 
       #-------------------------------------------------------------------------------------------------------------------
    
      if ( gB == 5 and gA <=4) or (gB == 6 and gA == 5):
        if  pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
          self.clabel.set("Set Point") 
      elif (gA == 6 and gB == 6 and sN != 5):
        if (pB >= 6 and pA-pB>=1) or (pB >= 6 and pB-pA>=1):
          print("----------------------------------------------------------------------------------------------------")
          self.clabel.set("Set Point")
        elif pA == 0 and pB == 0:
          self.clabel.set("Tie Break!")
      elif (gB == 5 and gA <=4) or (gB ==6 and gA == 5):
        if pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
          self.clabel.set("Set Point") 





    
      
      print("SA ",sA, "SB" ,sB)  
      if (sA == 2 and (sB == 0 or sB == 1)) or (sA == 2 and sB == 2):
        if ( gA == 5 and gB <=4) or (gA == 6 and gB == 5) or (gA>=6 and (gA - gB)>=1):
          if  pAs == "Adv" or (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6):
          if pA >= 6 and pA-pB>=1:
            print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
      elif (sB == 2 and (sA == 0 or sB == 1)) or (sA == 2 and sB == 2):
        if ( gB == 5 and gA <=4) or (gB == 6 and gA == 5) or (gB>=6 and (gB - gA)>=1):
          if  pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6):
          if pB >= 6 and pB-pA>=1:
            print("999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
         
      
      
      
      
    
    #--------------------------------------------------------------------------------------------------------------------
      if S == 1:
        sA+=1
        #print(sA,sB)
        self.set1label.set(sA)
        self.set2label.set(sB)
        self.clabel.set("Set!")
        scA = scA + str(gA) + "  "
        scB = scB + str(gB) + "  "
        gA = 0
        gB = 0
        fl = 0
        print(gA,gB)
        self.scoreA.set(scA)
        self.scoreB.set(scB)
        if Qs == 1:
          Q = 2
          Qs = 2
          print("QQQQQQQQQQQQQQQSSSSSSSSSSSSSSSSSSSSSSS",Qs)
        elif Qs == 2:
          Q = 1
          Qs = 1
          print("QQQQQQQQQQQQQQQSSSSSSSSSSSSSSSSSSSSSSS",Qs)
        #S = 0
      elif S == 2:
        sB+=1
        #print(sA,sB)
        self.set1label.set(sA)
        self.set2label.set(sB)
        self.clabel.set("Set!")
        scA = scA + gA + "  "
        scB = scB + gB + "  "
        gA = 0
        gB = 0
        fl = 0  
        self.scoreA.set(scA)
        self.scoreB.set(scB)
        print(gA,gB)
        #S = 0
    
      if (sA == 2 and (sB == 0 or sB == 1)) or (sA == 2 and sB == 2):
        if ( gA == 5 and gB <=4) or (gA == 6 and gB == 5) or (gA>=6 and (gA - gB) == 1 and sN == 5):
          if  pAs == "Adv" or (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6):
          if pA >= 6 and pA-pB>=1:
            print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
      if (sB == 2): #and (sA == 0 or sA == 1)) or (sA == 2 and sB == 2):
        if ( gB == 5 and gA <=4) or (gB == 6 and gA == 5) or (gB >= 6 and (gB - gA) == 1 and sN == 5):
          if  pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6 and sN != 5):
          if pB >= 6 and pB-pA>=1:
            print("999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
   
   
    if Q == 1:
        #print("00000000000000000000000000000000000000")
      self.plabel.set(pname1)
      self.serve1label.set("Serve")
      self.serve2label.set("")
      #plabel["fg"] = "green"
    elif Q == 2:
        #print("11111111111111111111111111111111111111")
      self.plabel.set(pname2)
      #plabel["fg"] = "blue"
      self.serve2label.set("Serve")
      self.serve1label.set("")

   
      M = match(sA,sB)
      if M == 1:
        pname1s = pname1 + " is the Winner!"
        self.matchw.set(pname1s)
        self.scoreA.set(scA)
        self.scoreB.set(scB)
      elif M == 2:
        pname2s = pname2 + " is the Winner!"
        self.matchw.set(pname2s)  
        self.scoreA.set(scA)
        self.scoreB.set(scB)
    elif M == 1:
      pname1s = pname1 + " is the Winner!"
      self.matchw.set(pname1s)
      self.point1label.set("")
      self.point2label.set("")
      self.scoreA.set(scA)
      self.scoreB.set(scB)
      #sys.exit(0)
    elif M == 2:
      pname2s = pname2 + " is the Winner!"
      self.matchw.set(pname2s)    
      self.point1label.set("")
      self.point2label.set("")
      self.scoreA.set(scA)
      self.scoreB.set(scB)
      #sys.exit(0)
      
  
  def pl2(self):
    global M
    global gA
    global gB
    global sA, sB
    global pname2,pname1
    global pA,pB
    global pAs,pBs,fl
    global sN
    global Q
    global scA , scB
    global Qs
    sN = sA + sB + 1
    print("SN",sN)
    if M == 0:
      pB=pB+1
      if gA == 6 and gB == 6 and sN == 5:
        fl = 1
      elif gA == 6 and gB == 6 and sN != 5:
        fl = 1
      print("FL",fl)
      pAs , pBs ,G = pointsAssign(pA,pB,fl)
      a = 2   
      print(G)
      print(pAs,pBs)
      #self.plabel2.set(pname2)
      self.plabel1.set(pname2)
      self.point1label.set(pAs)
      self.point2label.set(pBs)
      if G == 1 and fl == 0:
        gA+=1
        #print(fl)
        self.game1label.set(gA)
        self.game2label.set(gB)
        pA = 0
        pB = 0
        print("--------------")
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1

        self.clabel.set("Game")
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
      elif G == 2 and fl == 0:
        gB+=1
        #print(fl)
        self.game1label.set(gA)
        self.game2label.set(gB)
        pA = 0
        pB = 0
        print("--------------")
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        self.clabel.set("Game")
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
      elif G == 1 and fl == 1:
        pA = 0
        pB = 0
       # print(fl)
        gA = 7
        gB = 6
        fl = 0
        print("--------------")
        self.game1label.set(gA)
        self.game2label.set(gB)
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        self.clabel.set("Game")
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
      elif G == 2 and fl == 1:
        pA = 0
        pB = 0
        #print(fl)
        gB = 7
        gA = 6
        fl = 0
        self.clabel.set("Game")
        print("--------------")
        self.game1label.set(gA)
        if Q == 1:
          Q =2
        elif Q == 2:
          Q = 1
        if gA == 6 and gB == 6 and sN == 5:
          fl = 0
        self.game2label.set(gB)
      if G == 1 or G == 2:
        self.clabel.set("Game")
      elif pAs == "Adv" :
        self.clabel.set("Adv")
      elif (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
        self.clabel.set("Game Point") 
      elif pBs == "Adv" :
        self.clabel.set("Adv")    
      elif(pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
        self.clabel.set("Game Point")
      elif pAs == "40" and pBs == "40":
        self.clabel.set("Deuce")
      else:
        self.clabel.set("")
        ############################
      if Q == 1:
        if pBs == "Adv":
          self.clabel.set("Break Point")
        elif pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30"):
          self.clabel.set("Break Point")
      elif Q == 2:
        if pAs == "Adv":
          self.clabel.set("Break Point")
        elif pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30"):
          self.clabel.set("Break Point")

      ###########################3
      if ( gA == 5 and gB <=4) or (gA == 6 and gB == 5):
        if  pAs == "Adv" or (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
          self.clabel.set("Set Point") 
      elif (gA == 6 and gB == 6 and sN != 5):
        if (pA >= 6 and pA-pB>=1) or (pB >= 6 and pB-pA>=1):
          print("----------------------------------------------------------------------------------------------------")
          self.clabel.set("Set Point")
        elif pA == 0 and pB == 0:
          self.clabel.set("Tie Break!")
      elif (gA == 5 and gB <=4) or (gB ==6 and gA == 5):
        if pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
          self.clabel.set("Set Point") 
      if ( gB == 5 and gA <=4) or (gB == 6 and gA == 5):
        if  pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
          self.clabel.set("Set Point") 
      elif (gA == 6 and gB == 6 and sN != 5):
        if (pB >= 6 and pA-pB>=1) or (pB >= 6 and pB-pA>=1):
          print("----------------------------------------------------------------------------------------------------")
          self.clabel.set("Set Point")
        elif pA == 0 and pB == 0:
          self.clabel.set("Tie Break!")
      elif (gB == 5 and gA <=4) or (gB ==6 and gA == 5):
        if pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
          self.clabel.set("Set Point") 
      S = set(gA,gB)
  
  
  
    
       #-------------------------------------------------------------------------------------------------------------------
      
      
      print("SA ",sA, "SB" ,sB)  
      if (sA == 2 and (sB == 0 or sB == 1)) or (sA == 2 and sB == 2):
        if ( gA == 5 and gB <=4) or (gA == 6 and gB == 5) or (gA>=6 and (gA - gB) == 1 and sN == 5):
          if  pAs == "Adv" or (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6):
          if pA >= 6 and pA-pB>=1:
            print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
      if (sB == 2): #and (sA == 0 or sA == 1)) or (sA == 2 and sB == 2):
        if ( gB == 5 and gA <=4) or (gB == 6 and gA == 5) or (gB >= 6 and (gB - gA) == 1 and sN == 5):
          if  pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.clabel.set("Match Point")
        elif (gA == 6 and gB == 6 and sN != 5):
          if pB >= 6 and pB-pA>=1:
            print("999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
         
      
      
      
      
    
    #--------------------------------------------------------------------------------------------------------------------
      #print(S)
      if S == 2:
        sB+=1
        self.set1label.set(sA)
        self.set2label.set(sB)
        self.clabel.set("Set!")
        scA = scA + str(gA) + "  "
        scB = scB + str(gB) + "  "
        gA = 0
        gB = 0
        fl = 0
        print(gA,gB)
        self.scoreA.set(scA)
        self.scoreB.set(scB)
        if Qs == 1:
          Q = 2
          Qs = 2
        elif Qs == 2:
          Q = 1
          Qs = 1
        
        #S = 0
      elif S == 1:
        sA+=1
        self.set1label.set(sA)
        self.set2label.set(sB)
        self.clabel.set("Set!")
        scA = scA + str(gA) + "  "
        scB = scB + str(gB) + "  "
        gA = 0
        gB = 0
        if Qs == 1:
          Q = 2
          Qs = 2
        elif Qs == 2:
          Q = 1
          Qs = 1
        fl = 0
        self.scoreA.set(scA)
        self.scoreB.set(scB)
        print(gA,gB)
       # S = 0
     
     
      if (sA == 2 and (sB == 0 or sB == 1)) or (sA == 2 and sB == 2):
        if ( gA == 5 and gB <=4) or (gA == 6 and gB == 5):
          if  pAs == "Adv" or (pAs == "40" and (pBs == "0" or pBs == "15" or pBs == "30")):
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6):
          if pA >= 6 and pA-pB>=1:
            print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
      elif (sB == 2 and (sA == 0 or sB == 1)) or (sA == 2 and sB == 2):
        if ( gB == 5 and gA <=4) or (gB == 6 and gA == 5):
          if  pBs == "Adv" or (pBs == "40" and (pAs == "0" or pAs == "15" or pAs == "30")):
            self.clabel.set("Match Point") 
        elif (gA == 6 and gB == 6):
          if pB >= 6 and pB-pA>=1:
            print("999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            self.clabel.set("Match Point")
     
     
    if Q == 1:
      # print("00000000000000000000000000000000000000")
      self.plabel.set(pname1)
      self.serve1label.set("Serve")
      self.serve2label.set("")

      #plabel["fg"] = "green"
      
    elif Q == 2:
        #print("11111111111111111111111111111111111111")
      self.plabel.set(pname2)
      #plabel["fg"] = "blue" 
      self.serve2label.set("Serve")
      self.serve1label.set("")

      M = match(sA,sB)
      if M == 1:
        pname1s = pname1 + " is the Winner!"
        self.matchw.set(pname1s)
        self.scoreA.set(scA)
        self.scoreB.set(scB)
      elif M == 2:
        pname2s = pname2 + " is the Winner!"
        self.matchw.set(pname2s)  
        self.scoreA.set(scA)
        self.scoreB.set(scB)
    elif M == 1:
      pname1s = pname1 + " is the Winner!"
      self.matchw.set(pname1s)
      self.point1label.set("")
      self.point2label.set("")
      self.scoreA.set(scA)
      self.scoreB.set(scB)
      #sys.exit(0)
    elif M == 2:
      pname2s = pname2+ " is the Winner!"
      self.matchw.set(pname2s)
      self.point1label.set("")
      self.point2label.set("")
      self.scoreA.set(scA)
      self.scoreB.set(scB)
      #sys.exit(0)    
  
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()   
  
  def createWidgets(self):
    global pname1
    global pname2
    global date
    global time
    global year
    global month
    global day
    global hour
    global min
    global sec
    global Q
    print("QQQ=====",Q)
    localtime = time.localtime(time.time())
    year = localtime[0]
    month = localtime[1]
    day = localtime[2]
    hour = localtime[3]
    min  = localtime[4]
    sec  = localtime[5]
    date = (str(day))+"/"+(str(month))+"/"+(str(year))
    time = "Time: "+(str(hour))+": "+(str(min))

#    root = Tk()
#    self.root.title("Anurag")
    label = Label(self,anchor="w",fg="black",text="             Tennis Match",font=("Freestyle",30))
    label.grid(column=0,row=0,columnspan=8,sticky='EW')
  
    labeld = Label(self,anchor="w",fg="black",text="Date:"+date ,font=("Ariel",10))
    labeld.grid(column=2,row=1,sticky='EW')
  
    labelt = Label(self,anchor="w",fg="black",text=time ,font=("Ariel",10))
    labelt.grid(column=4,row=1,sticky='EW')
  
  # Row 1 Empty Label
    #e1label = Label(self,anchor="w",fg="white")
    #e1label.grid(column=1,row=1,columnspan=2,sticky='EW')
  
  # Row 2 Empty Label
    e2label = Label(self,anchor="w",fg="white")
    e2label.grid(column=1,row=2,columnspan=2,sticky='EW')
    
  # Row 3 Serve, Player Name ,  Set , Game , Points
  ########1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    servelabel = Label(self,anchor="w" ,fg="red",bg = "yellow",text="SERVE",font=("French",10))
    servelabel.grid(column=0 ,row=3,sticky='EW')
  ###############################!11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    playerlabel = Label(self,anchor="w" ,fg="black",text="   Player Name",font=("Times",12))
    playerlabel.grid(column=2,row=3,sticky='EW')
  
  
    setlabel = Label(self,anchor="w" ,fg="black",text="SET",font=("Times",10))
    setlabel.grid(column=5,row=3,sticky='EW')
  
  
    gamelabel = Label(self,anchor="w" ,fg="black",text="GAME",font=("Times",10))
    gamelabel.grid(column=6,row=3,sticky='EW')
  
    pointlabel = Label(self,anchor="w" ,fg="black",text="  Points",font=("Times",10))
    pointlabel.grid(column=7,row=3,sticky='EW')
  
    winlabel = Label(self,anchor="w" ,fg="black",text="  Point Won By",font=("Times",10))
    winlabel.grid(column=9,row=3,sticky='EW')
  
  
  
  #==============================================================================================================================
    # Service Profile

    photo = PhotoImage(file="a.jpg")
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.grid(column=1,row=0)

    nlabel = Label(self,anchor="w",fg="black",text="Serve: ",font=("Helvetica",12))
    nlabel.grid(column=7,row=7,sticky='EW')

    self.plabel = StringVar() 
    plabel = Label(self,anchor="w" ,textvariable=self.plabel, fg = "red" ,font=("Helvetica",12))
    plabel.grid(column=8,row=7,columnspan = 8,sticky='EW')

    #self.serlabel = StringVar() 
    #self.serlabel = StringVar()
    #serlabel = Label(self,anchor="w" ,fg="black", textvariable = self.serlabel ,font=("Times",10))
    #serlabel.grid(column=9,row=7,columnspan = 8,sticky='EW')
    #emlabel = Label(self,anchor="w",fg="white")
    #emlabel.grid(column=2,row=0,sticky='EW')

    #photo1 = PhotoImage(file="b.jpg")
    #label1 = Label(image=photo)
    #label1.image = photo # keep a reference!
    #label1.grid(column=2,row=0)
    
    ##############################################################################################################################3

    
    # Row 4 Player 1
    self.serve1label = StringVar()
    serve1label = Label(self,anchor="w" ,fg="green",textvariable=self.serve1label,font=("Times",10))
    serve1label.grid(column=0,row=4,sticky='EW')
  #===============================================================================================================================
    player1label = Label(self,anchor="w" ,fg="green",text= pname1,font=("Times",12))
    player1label.grid(column=2,row=4,sticky='EW')
  #############################################################################################3
    self.set1label = StringVar()
    set1label = Label(self,anchor="w" ,fg="green",textvariable=self.set1label,font=("Times",10))
    set1label.grid(column=5,row=4,sticky='EW')
################################################################################################
    self.game1label = StringVar() 
    game1label = Label(self,anchor="w" ,fg="green",textvariable=self.game1label,font=("Times",10))
    game1label.grid(column=6,row=4,sticky='EW')
  #############################################################3
    self.point1label = StringVar()
  
    point1label = Label(self,anchor="w" ,fg="green",textvariable=self.point1label,font=("Times",10))
    point1label.grid(column=7,row=4,sticky='EW')
  ##########################################################3#
    POINT1 = Button(self)
    POINT1["text"] = "Player 1"
    POINT1["fg"]   = "green"
    POINT1["command"] =  self.pl1
    POINT1.grid(column=9,row=4)
  
# Row 5 Player 2
    self.serve2label = StringVar()
    serve2label = Label(self,anchor="w" ,textvariable = self.serve2label,fg="blue")
    serve2label.grid(column=0 ,row=5,columnspan=1,sticky='EW')
  
    player2label = Label(self,anchor="w" ,fg="blue",text= pname2,font=("Times",12))
    player2label.grid(column=2,row=5,sticky='EW')
  
  ##################################################
    #self.set2label = StringVar()
    #sets2label = Label(self,anchor="w" ,fg="blue", textvarible = self.sets2label ,font=("Times",10))
    #sets2label.grid(column=5,row=5,sticky='EW')
  ################################################################################3
    self.set2label = StringVar()
    set2label = Label(self,anchor="w" ,fg="blue",textvariable = self.set2label,font=("Times",10))
    set2label.grid(column=5,row=5,sticky='EW')
  
    self.game2label = StringVar()
    game2label = Label(self,anchor="w" ,fg="blue",textvariable = self.game2label,font=("Times",10))
    game2label.grid(column=6,row=5,sticky='EW')
  
  #################################################################################
    self.point2label = StringVar()
    point2label = Label(self,anchor="w" ,fg="blue",textvariable=self.point2label ,font=("Times",10))
    point2label.grid(column=7,row=5,sticky='EW')
  ################################################################################
    POINT2 = Button(self)
    POINT2["text"] = "Player 2"
    POINT2["fg"]   = "blue"
    POINT2["command"] =  self.pl2
    POINT2.grid(column=9,row=5)
  
  # Row 6 Empty Label
    e6label = Label(self,anchor="w",fg="white")
    e6label.grid(column=1,row=6,columnspan=2,sticky='EW')

  # Row 7 Point Won By
  
    wlabel = Label(self,anchor="w",fg="black",text="Point Won By: ",font=("Helvetica",12))
    wlabel.grid(column=0,row=7,sticky='EW')
  
  ##########################################################
    self.plabel1 =StringVar()
  
    plabel1 = Label(self,anchor="w",fg="red", textvariable=self.plabel1,font=("Times",12))
    plabel1.grid(column=2,row=7,columnspan=1,sticky='EW')
  ###########################################################
    #self.plabel2 =StringVar()
  #
    #plabel2 = Label(self,anchor="w",fg="blue", textvariable=self.plabel2,font=("Times",12))
    #plabel2.grid(column=3,row=7,columnspan=5,sticky='EW')
  
  # Row 9 Empty Label
    e8label = Label(self,anchor="w",fg="white")
    e8label.grid(column=1,row=8,sticky='EW')  
  
  # Row 8 Break Point, Game Point, Match Point
    self.clabel = StringVar()
    clabel = Label(self,anchor="w",fg="black",textvariable = self.clabel,font=("Helvetica",15))
    clabel.grid(column=2,row=9,columnspan=5,sticky='EW')
  
  # Row 9 Empty Label
    e8label = Label(self,anchor="w",fg="white")
    e8label.grid(column=1,row=10,sticky='EW')
  # Row 10 Empty Label
    e10label = Label(self,anchor="w",fg="white")
    e10label.grid(column=1,row=12,sticky='EW')
  
  #Row 12 Match Winner
    self.matchw =StringVar()
    matchw = Label(self,anchor="w",fg="red", textvariable=self.matchw,font=("Times",12))
    matchw.grid(column=2,row=14,columnspan=1,sticky='EW')
  
  
  #Row 14 Final Score
    a1label = Label(self,anchor="w" ,fg="black",text= "Score: " ,font=("Times",12))
    a1label.grid(column=1,row=16,sticky='EW')
  
    players1label = Label(self,anchor="w" ,fg="green",text= pname1,font=("Times",12))
    players1label.grid(column=2,row=16,sticky='EW')
    self.scoreA = StringVar()
    scoreA = Label(self,anchor="w",fg="red", textvariable=self.scoreA,font=("Times",12))
    scoreA.grid(column=4,row=16,columnspan=1,sticky='EW')
  # Row 15 Final Score Player B
    players2label = Label(self,anchor="w" ,fg="blue",text= pname2,font=("Times",12))
    players2label.grid(column=2,row=17,sticky='EW')
    self.scoreB = StringVar()
    scoreB = Label(self,anchor="w",fg="red", textvariable=self.scoreB,font=("Times",12))
    scoreB.grid(column=4,row=17,columnspan=1,sticky='EW')
  
  #Row 16 Quit Button
    self.QUIT = Button(self)
    self.QUIT["text"] = "QUIT"
    self.QUIT["fg"]   = "red"
    self.QUIT["command"] =  self.quit
    self.QUIT.grid(column=4,row=19)
    
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createWidgets()
    


root = Tk()
app = Application(master=root)
#app.title('my application')
app.master.title("Tennis")
app.mainloop()
root.destroy()
