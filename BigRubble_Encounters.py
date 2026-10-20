#grab the tkinter GUI

import tkinter as tk
from tkinter import ttk
import random

root=tk.Tk()

#set window properties

root.title("Random Encounter Generator")
 
#window size config
screenWidth=root.winfo_screenwidth()
screenHeight=root.winfo_screenheight()
windowWidth=int(screenWidth/1.5)
windowHeight=int(screenHeight/1.5)
screenXCenter=int(screenWidth/2 - windowWidth/2)
screenYCenter=int(screenHeight/2 - windowHeight/2)
root.geometry(f'{windowWidth}x{windowHeight}+{screenXCenter}+{screenYCenter}')

#configure grids
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=5)

#declare variables

#these are the entries on the Zone List
BiomeList=["Manside", "Huntland", "Big Grazing", "Troll Lands", "Garden"]

#These lists are the monster, complication, and wants lists that the generator uses for the encounter
MobList = [
"Townsfolk",
"Bandits",
"Lunar Patrol",
"Zebra Riders",
"Unicorn Riders",
"Nomads",
"Gnoll Slavers",
"Great Trolls",
"Dark Trolls",
"Orc Raiding Party",
"Cave Trolls",
"Elves",
"Dryad",
"Pixies",
"Runners",
"Dwarfs",
"Ogres",
"Broos",
"Chaos Ooze",
"Dragonsnails",
"Drop Bears",
"Vampire",
"Baboons",
"Dragonewts",
"Gargoyles",
"Bullywug",
"Small Game",
"Special Encounter"
]

WantsList = [
"a conversation",
"a friend",
"a laugh",
"an opportune moment",
"barter",
"directions",
"family",
"food",
"gifts",
"glory",
"healing",
"his missing friend",
"love",
"meat",
"offerings",
"purification",
"sacrifices",
"secrecy",
"shiny things",
"sleep",
"something in your pack",
"something sweet",
"space",
"the area protected",
"to catch its prey",
"to claim territory",
"to eat and run",
"to establish dominance",
"to go faster",
"to go home",
"to hide",
"to know why you are here",
"to protect",
"to take someone unseen",
"to warn others",
"trap",
"warmth",
"water",
"you to leave",
"you to settle a dispute",
"you to stay",
"your name"
]

CompList = ["has not eaten in days",
"the area is incredibly loud",
"lost",
"injured",
"under attack",
"drugged",
"exhausted",
"the terrain is inhospitable",
"enchanted",
"controlled",
"vision is obscured",
"insane",
"disguised",
"terrified",
"cursed",
"fire",
"faking it",
"trapped",
"incredibly loud",
"ambush",
"diseased",
"overburdened",
"asleep",
"pursued",
"darkness",
"competition",
"dirty",
"surprised",
"has others to defend",
"overly strong"
]

#these are the percentage change weights depending on the selected zone.
#Not sure yet If I'm using static or Cumulative Weights. Manside has the only cumWeight list. Yes, haha.)
CumPercentMANSIDE = [45, 50, 59, 73, 74, 76, 76, 76, 77, 78, 78, 78, 78, 78, 78, 83, 84, 86, 87, 87, 87, 88, 88, 88, 88, 89, 98, 100]
MANSIDE = [45, 5, 10, 13, 1, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 5, 1, 2, 1, 0, 0, 1, 0, 0, 0, 1, 10, 2]
HUNTLAND = [6, 6, 3, 4, 0, 4, 1, 1, 5, 4, 3, 0, 0, 0, 0, 8, 3, 9, 4, 5, 2, 2, 2, 0, 4, 0, 20, 4]
BIGGRAZING = [3, 5, 3, 2, 1, 3, 1, 1, 5, 2, 1, 4, 0, 0, 1, 0, 4, 11, 1, 2, 0, 0, 2, 12, 2, 4, 15, 5]
TROLLLANDS = [0, 2, 0, 1, 0, 1, 0, 5, 40, 40, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 2, 10, 0]
GARDEN = [0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 17, 2, 8, 60, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]

#These appear to be style and variables for the final output
Output=ttk.Label(root, padding=20, font=("Verdana", 14), wraplength= (windowWidth*.85))
EncounterText=()
SelectedZone=()    

#Here I am trying to define the weights variable name for the Mob selection
def d100():
        SelectedZone = Zone.curselection()

SelectedZone = {"Manside": MANSIDE, "Huntland": HUNTLAND, "Big Grazing": BIGGRAZING, "Troll Lands": TROLLLANDS, "Garden": GARDEN}

#this code actually runs the die rolls for the selections
def rollEncounter(): #monster only, wandering
    SelectedZone = Zone.curselection
    

    #Mob=(random.choices(MobList, weights=SelectedZone, k=1))
    #Wants=(random.choice(WantsList)).rstrip()
    #Comp=(random.choice(CompList)).rstrip()
    #EncounterText="Encounter is " + str(Mob).strip("[]'") +" that want " + str(Wants) + " but " + str(Comp) + "."
    #Output.config(text=str(EncounterText)) 
    Output.config(text=str(SelectedZone))
    
def returnEncounter(event):
    rollEncounter()

#insert graphical elements

#header Label
#header = ttk.Label(root, text="Big Rubble Encounter", padding=10, font=("Verdana", 12))
#header.grid(
#    column=0, row=0,
#    ipadx=5, ipady=10,
#    sticky=tk.NW
#    )

#Create the Zone selection box
Zone = tk.Listbox(width=25, height=6, selectmode=tk.SINGLE)
Zone.pack(side=tk.LEFT, fill=tk.BOTH)
for item in BiomeList:
    Zone.insert(tk.END, item)
Zone.grid(column=0, row=0, sticky=tk.NW, ipadx=20, ipady=15, pady=15, padx=15)

#button 
d20icon= tk.PhotoImage(file="./d20Button.png")
rollTables = ttk.Button(
    root,
    image=d20icon,
    text="Roll Encounter",
    compound=tk.LEFT,
    command=rollEncounter
    )
rollTables.bind(
    "<Return>",returnEncounter)
rollTables.focus()
rollTables.grid(
    column=1, row=0,
    sticky=tk.NE,
    ipadx=20,
    ipady=10,
    pady=15, padx=15)

#Text Output
Output.grid(column=0, row=2, rowspan=3)


            


#keep this at the bottom for now to keep the window running
root.mainloop()
