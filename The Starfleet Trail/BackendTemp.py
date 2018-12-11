import random
import time

NewShip = None

def intro():
    #This is the intro
    print("You are going to travel the galaxy in search of new intelligent lifeforms. You have the opportunity to boldly go where no one has gone before!")
    story = ["Try embarking on a voyage across\n" ,
            "30 kiloparsecs of both civilised and\n" ,
            "wild space. Try! Will you navigate\n" ,
            "your ship through perilous asteroid fields,\n" ,
            "or will you face the danger of travelling\n" ,
            "across Klingon space.\n" ,
            "\n" ,
            "How will you make your way across uncharted\n" ,
            "nebulae? Will you pay for an escort to bring\n" ,
            "you safely through it, or will you brave the\n" ,
            "peril and face the mysteries that may lie within.\n" ,
            "\n" ,
            "What about fuel? Will you harvest it from gas\n" ,
            "giants, risking your shuttles to collect it\n" ,
            "from the atmosphere? Beware of the creatures\n" ,
            "that dwell among the clouds!\n" ,
            "\n" ,
            "Should you seek to reach your goal quicker,\n" ,
            "you could go through one of the unstable\n" ,
            "wormholes in the quadrant, but beware, for\n" ,
            "you do not know where you will emerge, and\n" ,
            "without assurances that you may return!\n" ,
            "\n" ,
            "In the Delta Quadrant, you may face the\n" ,
            "indefatigable Borg, or perhaps you would\n" ,
            "rather travel the gamma quadrant, and try\n" ,
            "to evade the Dominion's grasp!\n" ,
            "\n" ,
            "If you do not make it -- You may be set\n" ,
            "upon by Klingon pirates, you may be abducted\n" ,
            "by Romulan Intelligence, you may be assimilated\n",
            "into the Borg Collective, or you may encounter\n" ,
            "a deadly spacefaring entity that destroys your ship!\n" ,
            "Or your crew turns paranoid and violent after\n" ,
            "entering an unusual nebula... Fear not! You may\n" ,
            "Try again and again until you become the most\n" ,
            "seasoned explorer in Starfleet!\n"]
    for line in story:
        print(line)
    #GOAL IS 1000 PARSECS



def start():
    #Where ship object is instantiated
  print("Name your ship")
  Name = input("-->")
    #Is global so it can be accessed outside limited scope
  global NewShip
  NewShip = ship(Name)
  time.sleep(2)
  return NewShip


class ship:
    #Ship object characteristics
    def __init__(self, name):
        self.name = name
        self.shields = 500
        self.fuel = 150
        self.crew = 1000
        self.parsecs = 0
        #A parsec is equal to 3.26 light years.
        #A parsec is defined as the distance at which one astronomical unit subtends an angle of one arcsecond.
        self.mystdisease = False
        self.plagueCounter = 1
        self.antidote = 1
#The Disease is automatically cured if an antidote is available, but for every turn the disease is present, a counter
#goes up by one. This number is multiplied by 10 and subtracted from the crew, resulting in increasing damage to the
#crew's numbers.


#The following are the 4 events that can occur in the game
#Each event can affect the ship's shields, crew, fuel, and distance travelled. If any of the first
#3 reach 0, the game is lost. If distance travelled reaches 1000, the game is won.
def Nebula():
    #All of these work on a luck based system, which determines the possible outcomes that can occur
    luck = random.randint(0, 100)
    print("You stumble across an uncharted nebula. You could attempt to go through it, go around it, or go back to your last position.")
    print("Please choose option 1, 2, or 3")
    option = input("-->")
    if option == "1":
        if luck < 20:
            print("You are ambushed by pirates. You manage to defeat them, but with your shields weak due to the nebula you lose 100 crew and 50 fuel")
            NewShip.crew -= 100
            NewShip.fuel -= 15
            NewShip.parsecs += 50
            NewShip.shields -= 100
            time.sleep(2)
        elif luck < 60 and luck >20:
            print("You are lost in the nebula and are forced to exit at an inconvenient location.")
            NewShip.parsecs -= 100
            time.sleep(2)
        else:
            print("You successfully journey through the nebula")
            NewShip.parsecs +=150
            time.sleep(2)
    elif option == "2":
        print("You travel around the nebula, wasting more fuel than would be considered ideal.")
        NewShip.fuel -= 10
        NewShip.parsecs += 50
        time.sleep(2)
    elif option == "3":
        print("You return to your previous position")
        NewShip.fuel -= 5
        NewShip.parsecs += -50
        time.sleep(2)

def Wormhole():
    luck = random.randint(0, 100)
    print("You make your way to a temporary wormhole. You could use it to further your journey, but due to its unstable nature it could go terribly wrong.")
    print("You can either try your luck and venture into the wormhole, move in closer to study it, or return to your last position.")
    print("Please choose option 1, 2, or 3")
    option = input("-->")
    if option == "1":
        print("You approach the wormhole")
        time.sleep(3)
        if luck < 10:
            print("Your ship becomes stranded in the Delta Quadrant, where you are assimilated by the Borg")
            NewShip.crew -= NewShip.crew+1
            time.sleep(2)
        elif luck > 10 and luck < 40:
            print("You cover a considerable distance, saving fuel and furthering your journey.")
            NewShip.parsecs += 400
            time.sleep(2)
        else:
            print("You emerge having covered a good portion of your journey, but some of your crew has mysteriously disappeared, with no one remembering them even existing.")
            NewShip.parsecs +=300
            NewShip.crew -= 350
            NewShip.shields -= 100
            time.sleep(2)
    elif option == "2":
        if luck <25:
            print("An anomaly occurs onboard your ship, resulting in the spread of an unknown disease.")
            NewShip.mystdisease = True
            time.sleep(2)
        elif luck >25 and luck <50:
            print("You find a cache of fuel and a stranded crew, increasing your fuel reserves and bolstering your crew.")
            NewShip.fuel += 100
            NewShip.crew += 200
            time.sleep(2)
        else:
            print("You find nothing of use in the wormhole and continue with your journey")
            NewShip.fuel -=10
            NewShip.parsecs += 50
            time.sleep(2)
    elif option == "3":
        print("You continue with your journey")
        NewShip.fuel -=10
        NewShip.parsecs += 50
        time.sleep(2)

def Pirates():
    luck = random.randint(0, 100)
    print("You are set upon by pirates. You can either fight them, attempt to escape, or surrender part of your crew and fuel")
    print("Please choose option 1, 2, or 3")
    option = input("-->")
    if option == "1":
        if luck < 25:
            print("You manage to fend off the pirates, but at great cost.")
            NewShip.crew -= 400
            NewShip.shields -= 250
            time.sleep(2)
        elif luck > 25 and luck < 75:
            print("Although there are casualties, you destroy the pirate ships and salvage the wreckage.")
            NewShip.crew -= 250
            NewShip.shields -= 100
            NewShip.fuel += 50
            time.sleep(2)
        else:
            print("You achieve a flawless victory and suffer minimal damage to your shields, and salvage the wreckage for supplies.")
            NewShip.shields -= 50
            NewShip.fuel += 50
            NewShip.antidote += 1
            time.sleep(2)
    elif option == "2":
        if luck <50:
            print("You successfully flee, but take severe damage and suffer a fuel leak.")
            NewShip.crew -= 200
            NewShip.shields -= 150
            NewShip.fuel -= 50
            NewShip.parsecs += 50
            time.sleep(2)
        else:
            print("You successfully evade the pirates.")
            NewShip.fuel -= 10
            NewShip.parsecs += 100
            time.sleep(2)
    elif option == "3":
        print("You surrender half of your fuel and lose part of your crew.")
        NewShip.fuel = NewShip.fuel/2
        NewShip.crew -= 50
        time.sleep(2)

def Derelict():
    luck = random.randint(0, 100)
    print("You stumble upon a derelict vessel. You can either come in closer for a detailed inspection, send a shuttle, or ignore it.")
    print("Please choose option 1, 2, or 3")
    option = input("-->")
    if option == "1":
        if luck < 25:
            print("The derelict ship had succumbed to a plague. Your crew is not infected.")
            NewShip.mystdisease = True
            time.sleep(2)
        elif luck >25 and luck <75:
            print("You find nothing of interest.")
            time.sleep(2)
        else:
            print("The ship was a science vessel, and you salvage its supplies")
            NewShip.antidote += 2
            NewShip.fuel += 50
            NewShip.shields += 250
            time.sleep(2)
    elif option == "2":
        if luck <50:
            print("The shuttle stops responding to your hails. They are assumed lost with all hands.")
            NewShip.crew -= 20
            time.sleep(2)
        else:
            print("Your away team returns with some supplies they scavenged")
            NewShip.antidote += 1
            time.sleep(2)
    elif option == "3":
        print("You decide to move on with your journey")
        NewShip.fuel -= 10
        NewShip.parsecs += 50
        time.sleep(2)

def trek():
    #The trek method prints out the stats of your ship.
    print("__________________________________________________")
    print("You have travelled", NewShip.parsecs, "parsecs")
    print("The %s's shields are at %s capacity." % (NewShip.name,NewShip.shields))
    print("You have", NewShip.crew, "crew.")
    print("You have", NewShip.fuel, "fuel.")
    print("__________________________________________________")

def WinCheck():
    #Every turn, WinCheck() checks if you have reached the 1000 parsec goal.
    if NewShip.parsecs == 1000 or NewShip.parsecs > 1000:
        return True
def LooseCheck():
    #Every turn, LooseCheck() checks is you have lost. If you have, it returns false, which is relevant
    #in the run.py class.
    if NewShip.crew == 0 or NewShip.crew < 0:
        print("Your ship has no crew, you are stranded in space")
        return(False)
    if NewShip.fuel == 0 or NewShip.fuel < 0:
        print("Your ship has run out of fuel and is stranded in space")
        return(False)
    if NewShip.shields == 0 or NewShip.fuel <0:
        print("Your ship's shields have gone offline, making space travel impossible")
        return(False)
events = ["BackendTemp.Nebula()", "BackendTemp.Wormhole()", "BackendTemp.Pirates()", "BackendTemp.Derelict()"]
#events are between quotations because eval will be used later on to call them