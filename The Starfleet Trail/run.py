import BackendTemp
import random
BackendTemp.start()
BackendTemp.intro()
#plays intro
while BackendTemp.NewShip.parsecs <1000:
    eval(BackendTemp.events[random.randint(0,3)])
    #eval is used because methods in the events list are stored as string.
    BackendTemp.LooseCheck()
    BackendTemp.trek()
    if BackendTemp.NewShip.mystdisease:
        print("Your crew is infected")
        print("You have lost", BackendTemp.NewShip.plagueCounter*10, "crew")
        BackendTemp.NewShip.crew -= BackendTemp.NewShip.plagueCounter*10
        BackendTemp.NewShip.plagueCounter +=1
        #effects of disease as mentioned in BackendTemp.
        if BackendTemp.NewShip.antidote>0:
            print("You use the antidote to cure the infection")
            BackendTemp.NewShip.mystdisease = False
            BackendTemp.NewShip.antidote -=1
            #Antidote is automatically used if available.
    if BackendTemp.LooseCheck() == False:
        print("_______________________________")
        print("Game Over")
        print("_______________________________")
        break
    if BackendTemp.WinCheck() == True:
        print("_______________________________")
        print("Congratulations, You Win!")
        print("_______________________________")
        break