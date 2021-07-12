import random
class Player():
    def __init__(self,name):
        self.__Name = name
        self.__Turns = 0
        self.__Score = 0
        self.__Rps = ""

    def GetName(self):
        return(self.__Name)

    def UpdateTurns(self):
        self.__Turns = self.__Turns + 1

    def GetTurns(self):
        return(self.__Turns)

    def UpdateScore(self,addition):
        self.__Score = self.__Score + addition

    def GetScore(self):
        return(self.__Score)

    def SetRPS(self):
        self.__Rps = input("Enter RPS choice: ")
        self.__Rps = self.__Rps.title()

    def GetRPS(self):
        return(self.__Rps)
    
class Computer(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    def SetCRPS(self):
        Rps = ["Rock","Paper","Scissors"]
        self.__Rps = random.choice(Rps)

#Deciding turns with RPS - tested and works
def PlayRPS(Player,Computer):
    First = ""
    Winner = ""
    while Winner != ("Player" or "Computer"):
        Player.SetRPS() #Rps = rock-paper-scissors
        Computer.SetCRPS()
        PRPS = Player.GetRPS()
        CRPS = Computer.GetRPS()
        print(Player.GetName(),"got: ",PRPS)
        print(Computer.GetName(),"got: ",CRPS)

        while PRPS == CRPS:
            Player.SetRPS()
            Computer.SetCRPS()
            PRPS = Player.GetRPS()
            CRPS = Computer.GetRPS()
            print(Player.GetName(),"got: ",PRPS) #testing purposes
            print(Computer.GetName(),"got: ",CRPS)

        if PRPS == "Rock" and CRPS == "Scissors":
            Winner = "Player"
        
        elif CRPS == "Rock" and PRPS == "Scissors":
            Winner = "Computer"

        elif PRPS == "Paper" and CRPS == "Rock":
            Winner = "Player"

        elif CRPS == "Paper" and PRPS == "Rock":
            Winner = "Computer" 

        elif PRPS == "Scissors" and CRPS == "Paper":
            Winner = "Player"

        elif CRPS == "Scissors" and PRPS == "Paper":
            Winner = "Computer" 
    if Winner == "Player":
        First = Player
    else:
        First = Computer

    return(First)       

#Setting up players each game - completed and works
PName = input("Enter player name: ")
PName = PName.title()
CName = input("Enter CPU name: ")
CName = CName.title()
CName = CName + "(CPU)"
CID = CName[-4:-1]

Human = Player(PName)
Comp = Computer(CName)

#Playing the game - work in progress

Goal = 100 #setting goal score
PScore = 0 #player scores to test game
CScore = 0
GameOver = False

#Making the point lots
SafeLot = [0,0,2,2,2,2,2,2,2,4,4,4,5,5,5,5,6,6,8,8,10] #high chance to get mid-range (which is still small)
RiskLot = [-10,-8,-6,-4,-4,-4,-4,-4,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,4,4,4,4,4,8,8,8,8,8,15,15,15,15,15,20,20,25] #more chances to lose more points but cahnces to gain more too
GoBigOrGoHomeLot = [-50,-25,25,-10,-10,-10,-10,-10,-10,-10,0,0,0,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,40,40,40,40,40,50,60,80] #more chances to lose more points than RiskLot but max. point reward is higher

while GameOver == False:
    TurnStarter = PlayRPS(Human,Comp)
    if TurnStarter == Human:
        print(Human.GetName(),"won so they go first")

    else:
        print(Comp.GetName(),"won so they go first")  