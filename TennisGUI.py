# -*- coding: iso-8859-1 -*-
from tkinter import *
from sup import*

# Empty Label
#label = Label(self,anchor="w",fg="white")
#label.grid(column=1,row=0,columnspan=2,sticky='EW')

class Application(Frame):
  global a
  a = 0

  def say_hi(self):
    print ("Hi.")
  def pl1(self):
    global a
    a = 1
    print ("Player 1")
    self.plabel1.set("Player 1")
    self.plabel2.set("")
  def pl2(self):
    global a
    a = 2  
    print("Player 2")
    self.plabel2.set("Player 2")
    self.plabel1.set("")


  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()   
	
  def createWidgets(self):
    global a
#    root = Tk()
#    self.root.title("Anurag")
    label = Label(self,anchor="w",fg="black",text="Tennis Match",font=("Helvetica",30))
    label.grid(column=0,row=0,columnspan=5,sticky='EW')
	# Row 1 Empty Label
    e1label = Label(self,anchor="w",fg="white")
    e1label.grid(column=1,row=1,columnspan=2,sticky='EW')
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
	
    player1label = Label(self,anchor="w" ,fg="green",text="   Player 1",font=("Times",12))
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
	
    player2label = Label(self,anchor="w" ,fg="blue",text="   Player 2",font=("Times",12))
    player2label.grid(column=2,row=5,sticky='EW')
	
	
    set2label = Label(self,anchor="w" ,fg="blue",text="SET2",font=("Times",10))
    set2label.grid(column=5,row=5,sticky='EW')
	
    game2label = Label(self,anchor="w" ,fg="blue",text="GAME2",font=("Times",10))
    game2label.grid(column=6,row=5,sticky='EW')
	
    point2label = Label(self,anchor="w" ,fg="blue",text="  Points2",font=("Times",10))
    point2label.grid(column=7,row=5,sticky='EW')
	
    POINT2 = Button(self)
    POINT2["text"] = "Player 2"
    POINT2["fg"]   = "green"
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
    plabel1.grid(column=1,row=7,columnspan=5,sticky='EW')
	
    self.plabel2 =StringVar()
	
    plabel2 = Label(self,anchor="w",fg="blue", textvariable=self.plabel2,font=("Times",12))
    plabel2.grid(column=2,row=7,columnspan=5,sticky='EW')
	
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
app.master.title("Anurag Aladhahalli Sampath")
app.mainloop()
root.destroy()