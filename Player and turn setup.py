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
        Rps = ["Rock","Paper","Scissors"]
        self.__Rps = random.choice(Rps)

    def GetRPS(self):
        return(self.__Rps)
    

class Computer(Player):
    def __init__(self,name):
        Player.__init__(self,name)

#Test codes    
PName = input("Enter player name: ")
PName = PName.title()
CName = input("Enter CPU name: ")
CName = CName.title()
CName = CName + "(CPU)"
CID = CName[-4:-1]

Human = Player(PName)
Comp = Computer(CName)

print(Human.GetName())
Human.UpdateTurns()
print(Human.GetName() + " turn count: ",Human.GetTurns())
Human.UpdateScore(3)
print("Human score: ",Human.GetScore())
Human.SetRPS()
print("Human got: ",Human.GetRPS())
      
print(Comp.GetName())
Comp.UpdateTurns()
print(Comp.GetName() + " turn count: ",Comp.GetTurns())
Comp.UpdateScore(3)
print("CPU score: ",Comp.GetScore())
Comp.SetRPS()
print("CPU got: ",Comp.GetRPS())
print(CID)
