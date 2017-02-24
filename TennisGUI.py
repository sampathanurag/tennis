# -*- coding: iso-8859-1 -*-
#!/usr/bin/python
import time;



from tkinter import *
from sup import*
from sys import argv
global pname1
global pname2
script  , pname1, pname2 =argv


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
	# Time 
  


  def pl1(self):
    global pname1
    a = 1
    #print (pname1)
    self.plabel1.set(pname1)
    self.plabel2.set("")
  def pl2(self):
    global pname2
    a = 2  
    #print(pname2)
    self.plabel2.set(pname2)
    self.plabel1.set("")

	
	
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
    label = Label(self,anchor="w",fg="black",text="                   Score",font=("Freestyle",30))
    label.grid(column=0,row=0,columnspan=8,sticky='EW')
	
    labeld = Label(self,anchor="w",fg="black",text="Date:"+date ,font=("Ariel",10))
    labeld.grid(column=0,row=1,sticky='EW')
	
    labelt = Label(self,anchor="w",fg="black",text=time ,font=("Ariel",10))
    labelt.grid(column=3,row=1,sticky='EW')
	
	# Row 1 Empty Label
    #e1label = Label(self,anchor="w",fg="white")
    #e1label.grid(column=1,row=1,columnspan=2,sticky='EW')
	
	# Row 2 Empty Label
    e2label = Label(self,anchor="w",fg="white")
    e2label.grid(column=1,row=2,columnspan=2,sticky='EW')
    
	# Row 3 Serve, Player Name ,  Set , Game , Points
	
    servelabel = Label(self,anchor="w" ,fg="red",text="SERVE",font=("French",10))
    servelabel.grid(column=0 ,row=3,columnspan=1,sticky='EW')
	
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
	
	
	# Row 4 Player 1
    serve1label = Label(self,anchor="w" ,bg="green")
    serve1label.grid(column=0 ,row=4,columnspan=1,sticky='EW')
	
    player1label = Label(self,anchor="w" ,fg="green",text= pname1,font=("Times",12))
    player1label.grid(column=2,row=4,sticky='EW')
	
	
    set1label = Label(self,anchor="w" ,fg="green",text="SET1",font=("Times",10))
    set1label.grid(column=5,row=4,sticky='EW')
	
    game1label = Label(self,anchor="w" ,fg="green",text="GAME1",font=("Times",10))
    game1label.grid(column=6,row=4,sticky='EW')
	
    point1label = Label(self,anchor="w" ,fg="green",text="  Points1",font=("Times",10))
    point1label.grid(column=7,row=4,sticky='EW')
	
    POINT1 = Button(self)
    POINT1["text"] = "Player 1"
    POINT1["fg"]   = "green"
    POINT1["command"] =  self.pl1
    POINT1.grid(column=9,row=4)
	
# Row 5 Player 2
    serve2label = Label(self,anchor="w" ,bg="blue")
    serve2label.grid(column=0 ,row=5,columnspan=1,sticky='EW')
	
    player2label = Label(self,anchor="w" ,fg="blue",text= pname2,font=("Times",12))
    player2label.grid(column=2,row=5,sticky='EW')
	
	
    set2label = Label(self,anchor="w" ,fg="blue",text="SET2",font=("Times",10))
    set2label.grid(column=5,row=5,sticky='EW')
	
    game2label = Label(self,anchor="w" ,fg="blue",text="GAME2",font=("Times",10))
    game2label.grid(column=6,row=5,sticky='EW')
	
    point2label = Label(self,anchor="w" ,fg="blue",text="  Points2",font=("Times",10))
    point2label.grid(column=7,row=5,sticky='EW')
	
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
	
	
    self.plabel1 =StringVar()
	
    plabel1 = Label(self,anchor="w",fg="green", textvariable=self.plabel1,font=("Times",12))
    plabel1.grid(column=2,row=7,columnspan=1,sticky='EW')
	
    self.plabel2 =StringVar()
	
    plabel2 = Label(self,anchor="w",fg="blue", textvariable=self.plabel2,font=("Times",12))
    plabel2.grid(column=3,row=7,columnspan=5,sticky='EW')
	
	# Row 9 Empty Label
    e8label = Label(self,anchor="w",fg="white")
    e8label.grid(column=1,row=8,sticky='EW')	
	
	# Row 8 Break Point, Game Point, Match Point
    clabel = Label(self,anchor="w",fg="black",text="Status",font=("Helvetica",15))
    clabel.grid(column=2,row=9,columnspan=5,sticky='EW')
	
	# Row 9 Empty Label
    e8label = Label(self,anchor="w",fg="white")
    e8label.grid(column=1,row=10,sticky='EW')
	# Row 10 Empty Label
    e10label = Label(self,anchor="w",fg="white")
    e10label.grid(column=1,row=10,sticky='EW')
	
	#Row 12 Quit Button
    self.QUIT = Button(self)
    self.QUIT["text"] = "QUIT"
    self.QUIT["fg"]   = "red"
    self.QUIT["command"] =  self.quit
    self.QUIT.grid(column=4,row=15)
		
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()
    


root = Tk()
app = Application(master=root)
#app.title('my application')
app.master.title("Tennis")
app.mainloop()
root.destroy()
