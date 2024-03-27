import random
import time
#import tkinter as tk

#window = tk.Tk()
#intro = tk.Label(text = "The Avatar Game")
#intro.pack()
#window.mainloop()
def introduction1(enteredName):
    #pause for dramatic effect
    print("Water....")
    time.sleep(1)
    print("Earth...")
    time.sleep(1)
    print("Fire...")
    time.sleep(1)
    print("Air...")
    time.sleep(1)
    print("Welcome Avatar ",enteredName,"!\nYou are the chosen Avatar! ... ") 
    time.sleep(2)
    print("You must master all the elements in order to defeat the Fire Nation \n and restore balance to the world!...")
    time.sleep(2)
  
def chooseBending(theChosenElement):
    element = theChosenElement

    if element == "Earth" or element ==  "earth":
        print("You are an Earth Bender")
        time.sleep(2)
    elif element == "Water" or element == "water":
        print("You are a Water Bender")
        time.sleep(2)
    elif element == "Fire" or element == "fire":
        print("You are a Fire Bender")
        time.sleep(2)
    elif element == "Air" or element == "air":
        print("You are an Air Bender")
        time.sleep(2) 
    else:
        print("You are not a bender, Fire Lord Ozai sees you as no Threat")
        exit()
    #Power moves for Waterbending
    waterBending = {"level_1":"Water slap", "level_2": "Water punch","level_3":"Ice freeze"}

    #Power Moves for EarthBending
    earthBending = {"level_1":"Rock slap", "level_2": "Rock wall collision","level_3":"Earth disks"}

    #Power Moves for AirBending
    airBending = {"level_1":"Air push", "level_2": "Air maneuver","level_3":"Air drop"}

    #Power Moves for FireBending
    fireBending = {"level_1": "Fire wall", "level_2": "Fire punch","level_3":"Electricity"}

    #counter for power moves
    powerMoveLevel = 0

    print("You are a Master in the ",element," element!")
    time.sleep(1)

    if element == "Earth" or element == "earth":
        print("You will have to master Water, Fire, and Air")
        time.sleep(1)
        print("Your power moves that you have mastered are: ")
        time.sleep(1)
        for powerMoves in earthBending.values():
            print("\t",powerMoves)
        time.sleep(2)
    elif element == "Water" or element == "water":
        print("You will have to master Earth, Fire, and Air")
        time.sleep(1)
        print("Your power moves that you have mastered are: ")
        time.sleep(1)
        for powerMoves in  waterBending.values():
            print("\t",powerMoves)
        time.sleep(2)
    elif element == "Fire" or element == "fire":
        print("You will have to master Water, Earth, and Air")
        time.sleep(1)
        print("Your power moves that you have mastered are: ")
        time.sleep(1)
        for powerMoves in fireBending.values():
            print("\t",powerMoves)
        time.sleep(2)
    elif element == "Air" or element == "air":
        print("You will have to master Water, Fire, and Earth")
        time.sleep(1)
        print("Your power moves that you have mastered are: ")
        time.sleep(1)
        for powerMoves in airBending.values():
            print("\t",powerMoves)
        time.sleep(2) 
    
    



print("Welcome to the Avatar Game")
name = input("Please Enter your Name: ")
introduction1(name)
#have user input the element they want the Avatar to start with
chosenElement = input("Please choose your chosen element: ")
chooseBending(chosenElement)
#If you put anything besides the options above, the game will end


#Different prompts for when the fire nation attacks 
fireNationAlarms = ["The Fire Nation has tracked you down!","You crossed paths with the Fire Nation!","Oh No! The Fire Nation is here!","Bad Luck is among us, the Fire Nation is here!"]  

print("Let's start the game!")
time.sleep(1)
#Different Locations to travel in the Avatar world, will be random
#Will Continue to work on This
location = ["Omashu","Ba-Sing-Se","Kyoshi Island","Easter Air Temple","Fire Fountain City","Northern Water Tribe","Southern Water Tribe","Abandoned Mine","Southern Air Temple","Angel Falls","Firelight Mountain","Boiling Rock","Cave of 2 Lovers","Ember Island","Mount Roraima","Chin Village","GlowWorm Caves"]
counterForLocation = 0
while counterForLocation < len(location):
    if(counterForLocation == 0):
        locationChosen = random.choice(location)
        
        print("We will start our journey on: ",random.choice(location))
        counterForLocation = counterForLocation + 1
        continue
    else:
        print("We will continue our Journey on: ",random.choice(location))
        counterForLocation = counterForLocation + 1
    
        
    
    

        
    
#We have to make sure you start your training so we have to pick which element to train at first
earthOptions = ["Water","Fire","Air"]
airOptions = ["Water","Fire","Earth"]
fireOptions = ["Water","Earth","Air"]
waterOptions = ["Earth","Fire","Air"]

nextElementToMaster = ""
if(chosenElement == "Earth" or chosenElement == "earth"):
    nextElementToMaster = random.choice(earthOptions)
    print("Your next element to master is : ",nextElementToMaster)
elif(chosenElement == "Air" or chosenElement == "air"):
    nextElementToMaster = random.choice(airOptions)
    print("Your next element to master is: ",nextElementToMaster)
elif(chosenElement == "Water" or chosenElement == "water"):
    nextElementToMaster = random.choice(waterOptions)
    print("Your next element to master is: ",nextElementToMaster)
elif(chosenElement == "Fire" or chosenElement == "fire"):
    nextElementToMaster = random.choice(fireOptions)
    print("Your next element to master is: ",nextElementToMaster)

time.sleep(1)
print("Going through the journey ...!")
time.sleep(1)

fight = random.choice([True,False])
#Fight outcome is to see whether you win the fight with the fight nation, 1 is winning the fight, 0 is fight lost
fightOutcome = random.choice([0,1])

if fight == True:
    print(random.choice(fireNationAlarms))
    if(fightOutcome == 1):
        print("You have won the fight!")
        print("You have mastered a power move!")
        powerMoveLevel = powerMoveLevel + 1
        
        if(nextElementToMaster == "Water"):
            if(powerMoveLevel == 1):
                print("You have mastered the: ",waterBending["level_1"])
            if(powerMoveLevel == 2):
                print("You have mastered the: ",waterBending["level_2"])
            if(powerMoveLevel == 3):
                print("You have mastered the: ",waterBending["level_3"])
            if(powerMoveLevel == 4):
                print("Its time to challenge Master Water Bender Katara!")
                time.sleep(2)
                waterMasterFightOutcome = random.choice([0,1])
                #Winning outCome for Master Fight
                if(waterMasterFightOutcome == 1):
                    print("You have won against Katara!")
                    earthOptions.remove("Water") 
                    fireOptions.remove("Water") 
                    airOptions.remove("Water") 
                else:
                    powerMoveLevel = powerMoveLevel - 1
                    print(powerMoveLevel)
                    print("You have lost to Master Katara, you must to try to master the Water Element again")
        if(nextElementToMaster == "Earth"):
            if(powerMoveLevel == 1):
                print("You have mastered the: ",earthBending["level_1"])
            if(powerMoveLevel == 2):
                print("You have mastered the: ",earthBending["level_2"])
            if(powerMoveLevel == 3):
                print("You have mastered the: ",earthBending["level_3"])
            if(powerMoveLevel == 4):
                earthMaster = random.choice(["Toph","King Bumi"])
                print("Its time to challenge Master Earth Bender ",earthMaster)
                time.sleep(2)
                earthMasterFightOutcome = random.choice([0,1])
                #Winning Outcome for Master Fight
                if(earthMasterFightOutcome == 1):
                    print("You have won against ",earthMaster)
                    waterOptions.remove("Earth")
                    fireOptions.remove("Earth")
                    airOptions.remove("Earth")
                else:
                    powerMoveLevel = powerMoveLevel - 1
                    print(powerMoveLevel)
                    print("You have lost to Master ",earthMaster,", you must try to master the Earth Element again")
        
        if(nextElementToMaster == "Fire"):
            if(powerMoveLevel == 1):
                print("You have mastered the: ",fireBending["level_1"])
            if(powerMoveLevel == 2):
                print("You have mastered the: ",fireBending["level_2"])
            if(powerMoveLevel == 3):
                print("You have mastered the: ",fireBending["level_3"])
            if(powerMoveLevel == 4):
                fireMaster = random.choice(["Prince Zuko","General Iroh"])
                print("Its time to challenge Master Fire Bender ",fireMaster)
                time.sleep(2)
                fireMasterFightOutcome = random.choice([0,1])
                if(fireMasterFightOutcome == 1):
                    print("You have won against ",fireMaster)
                    waterOptions.remove("Fire")
                    earthOptions.remove("Fire")
                    airOptions.remove("Fire")
                else:
                    powerMoveLevel = powerMoveLevel - 1
                    print(powerMoveLevel)
                    print("You have lost to Master ",fireMaster,", you must try to master the Fire Element again")
        if(nextElementToMaster == "Air"):
            if(powerMoveLevel == 1):
                print("You have mastered the: ",airBending["level_1"])
            if(powerMoveLevel == 2):
                print("You have mastered the: ",airBending["level_2"])
            if(powerMoveLevel == 3):
                print("You have mastered the: ",airBending["level_3"])
            if(powerMoveLevel == 4):
                print("Its time to challenge Master Air Bender Aang") 
                time.sleep(2)
                airMasterOutCome = random.choice([0,1])
                if(airMasterOutCome == 1):
                    print("You have won against Master Avatar Aang!")
                    waterOptions.remove("Air")
                    fireOptions.remove("Air")
                    earthOptions.remove("Air")
                else:
                    powerMoveLevel = powerMoveLevel - 1
                    print(powerMoveLevel) 
                    print("You have lost to Master Avatar Aang, you must try to master the Air Element again")       
    else:
        print("You have lost the fight, retreat and gather your strength")
        if(powerMoveLevel > 0):
            powerMoveLevel = powerMoveLevel -1 
            print(powerMoveLevel) 
        else:
            print("Thank the Past Avatars it wasn't too serious!")
            print(powerMoveLevel)
else:
    print("Looks like the Fire Nation didn't track us here!")
    print("Lets practice our power moves!")
    print(powerMoveLevel)

    


   
    
