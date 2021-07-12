import random
#Setting up players each game - completed and works
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
        Rps = ["Rock","Paper","Scissors"]
        self.__Rps = random.choice(Rps)

    def GetRPS(self):
        return(self.__Rps)
    

class Computer(Player):
    def __init__(self,name):
        Player.__init__(self,name)

#Playing the game - work in progress
def PlayRPS(Player,Computer):
    PRPS = Player.SetRPS() #Rps = rock-paper-scissors
    CRPS = random.choice(Rps)
    
    

Goal = 100 #setting goal score
PScore = 0 #player scores to test game
CScore = 0
GameOver = False

#Making the point lots
SafeLot = [0,0,2,2,2,2,2,2,2,4,4,4,5,5,5,5,6,6,8,8,10] #high chance to get mid-range (which is still small)
RiskLot = [-10,-8,-6,-4,-4,-4,-4,-4,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,4,4,4,4,4,8,8,8,8,8,15,15,15,15,15,20,20,25] #more chances to lose more points but cahnces to gain more too
GoBigOrGoHomeLot = [-50,-25,25,-10,-10,-10,-10,-10,-10,-10,0,0,0,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,40,40,40,40,40,50,60,80] #more chances to lose more points than RiskLot but max. point reward is higher

#while GameOver == False:
    