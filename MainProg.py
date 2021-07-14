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

    def AddToScoreFile(self):
        ScoreFile = open("RawScores.txt","a")
        ScoreFile.write(self.__Name + "-" + str(self.__Turns) + "-" + str(self.__Score) + "\n")
        ScoreFile.close()

class Computer(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    def SetCRPS(self):
        Rps = ["Rock","Paper","Scissors"]
        self.__Rps = random.choice(Rps)

    def GetCRPS(self):
        return (self.__Rps)

#Deciding turns with RPS - tested and fully works without bugs
def PlayRPS(Player,Computer):
    print("Play rock-paper-scissors to decide turn order")
    First = ""
    PWin = False
    CWin = False
    while ((PWin == False) and (CWin == False)):
        Player.SetRPS() #Rps = rock-paper-scissors
        Computer.SetCRPS() #this doesn't run how I want it to
        PRPS = Player.GetRPS()
        CRPS = Computer.GetCRPS()
        print(Player.GetName(),"got: ",PRPS)
        print(Computer.GetName(),"got: ",CRPS)
        
        print("\n") #presentation purposes

        while PRPS == CRPS:
            print(Player.GetName(),"and",Computer.GetName(),"drew so we'll go again\n")
            Player.SetRPS()
            Computer.SetCRPS()
            PRPS = Player.GetRPS()
            CRPS = Computer.GetCRPS()
            print(Player.GetName(),"got: ",PRPS) #testing purposes
            print(Computer.GetName(),"got: ",CRPS)
            print("\n") #presentation purposes

        if ((PRPS == "Rock") and (CRPS == "Scissors")):
            PWin = True
        
        elif ((PRPS == "Scissors") and (CRPS == "Rock")):
            CWin = True

        elif ((PRPS == "Paper") and (CRPS == "Rock")):
            PWin = True

        elif ((PRPS == "Rock") and (CRPS == "Paper")):
            CWin = True 

        elif ((PRPS == "Scissors") and (CRPS == "Paper")):
            PWin = True

        elif ((PRPS == "Paper") and (CRPS == "Scissors")):
            CWin = True 
    
    if PWin == True:
        First = Player
    else:
        First = Computer

    return(First)       

#Menu to decide between playing the game, reading raw score data and reading special wall
Menu = "1. Play the game\n2. Read previous winnners' raw score data\n3. Read the 'Special Wall'"
print(Menu)
Choice = int(input("Enter your choice (0 to exit): "))

while Choice != 0:
    if Choice == 1:
        #Setting up players each game - completed and works
        PName = input("Enter player name: ")
        PName = PName.title()
        CName = input("Enter CPU name: ")
        CName = CName.title()
        CName = CName + "(CPU)"

        Human = Player(PName)
        Comp = Computer(CName)

        #Playing the game - completed and works properly after testing

        Goal = 50 #setting goal score (test with 20)
        PScore = 0 #player scores to test game
        CScore = 0
        GameOver = False

        #Making the point lots
        SafeLot = [0,0,2,2,2,2,2,2,2,4,4,4,5,5,5,5,6,6,8,8,10] #high chance to get mid-range (which is still small)
        RiskLot = [-10,-8,-6,-4,-4,-4,-4,-4,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,4,4,4,4,4,8,8,8,8,8,15,15,15,15,15,20,20,25] #more chances to lose more points but cahnces to gain more too
        GoBigOrGoHomeLot = [-50,-25,25,-10,-10,-10,-10,-10,-10,-10,0,0,0,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,40,40,40,40,40,50,60,80] #more chances to lose more points than RiskLot but max. point reward is higher

        while GameOver == False:
            TurnStarter = PlayRPS(Human,Comp)
            LotList = ["Safe","Risky","Go Big or Go Home"]
            if TurnStarter == Human:
                print(Human.GetName(),"won so they go first")
                LotChoice = int(input("Choose your point lot (1,2,3): "))
                if LotChoice == 1:
                    print("Chosen lot: ",LotList[LotChoice-1])
                    Points = random.choice(SafeLot)
                    print("Points gained: ",Points)
                    Human.UpdateScore(Points)

                elif LotChoice == 2:
                    print("Chosen lot: ",LotList[LotChoice-1])
                    Points = random.choice(RiskLot)
                    print("Points gained: ",Points)
                    Human.UpdateScore(Points)

                else:
                    print("Chosen lot: ",LotList[LotChoice-1])
                    Points = random.choice(GoBigOrGoHomeLot)
                    print("Points gained: ",Points)
                    Human.UpdateScore(Points)

                print("\n") #presentation purposes

                print("Computer's turn")
                LotChoice = random.randint(0,2)
                print(Comp.GetName(),"chose: ",LotList[LotChoice])
                LotChoice = LotChoice + 1

                if LotChoice == 1:
                    Points = random.choice(SafeLot)
                    print("Points gained: ",Points)
                    Comp.UpdateScore(Points)

                elif LotChoice == 2:
                    Points = random.choice(RiskLot)
                    print("Points gained: ",Points)
                    Comp.UpdateScore(Points)

                else:
                    Points = random.choice(GoBigOrGoHomeLot)
                    print("Points gained: ",Points)
                    Comp.UpdateScore(Points)
                
                print("\n") #presentation purposes

            elif TurnStarter == Comp:
                print(Comp.GetName(),"won so they go first")
                LotChoice = random.randint(0,2)
                print(Comp.GetName(),"chose: ",LotList[LotChoice])
                LotChoice = LotChoice + 1

                if LotChoice == 1:
                    Points = random.choice(SafeLot)
                    print("Points gained: ",Points)
                    Comp.UpdateScore(Points)

                elif LotChoice == 2:
                    Points = random.choice(RiskLot)
                    print("Points gained: ",Points)
                    Comp.UpdateScore(Points)

                else:
                    Points = random.choice(GoBigOrGoHomeLot)
                    print("Points gained: ",Points)
                    Comp.UpdateScore(Points)

                print("\n") #presentation purposes

                print("Your turn")
                LotChoice = int(input("Choose your point lot (1,2,3): "))
                if LotChoice == 1:
                    print("Chosen lot: ",LotList[LotChoice-1])
                    Points = random.choice(SafeLot)
                    print("Points gained: ",Points)
                    Human.UpdateScore(Points)

                elif LotChoice == 2:
                    print("Chosen lot: ",LotList[LotChoice-1])
                    Points = random.choice(RiskLot)
                    print("Points gained: ",Points)
                    Human.UpdateScore(Points)

                else:
                    print("Chosen lot: ",LotList[LotChoice-1])
                    Points = random.choice(GoBigOrGoHomeLot)
                    print("Points gained: ",Points,) 
                    Human.UpdateScore(Points)
                
                print("\n") #presentation purposes

            Human.UpdateTurns()
            Comp.UpdateTurns()

            print("End of turn score for ",Human.GetName(),": ",Human.GetScore())
            print("End of turn score for ",Comp.GetName(),": ",Comp.GetScore(),"\n") #presentation purposes

            #Check if game's over to exit while loop + adding winner data to raw score file
            if ((Human.GetScore() >= Goal) and (Human.GetScore() > Comp.GetScore())):
                print(Human.GetName()," won in ",Human.GetTurns(),"turns! Good job!")
                Human.AddToScoreFile()
                GameOver = True

            elif ((Comp.GetScore() >= Goal) and (Comp.GetScore() > Human.GetScore())):
                print(Comp.GetName()," won in ",Comp.GetTurns(),"turns! Good job (I guess)!")
                print("Better luck next time ",Human.GetName()," :)")
                Comp.AddToScoreFile()
                GameOver = True

        #Reading RawScores and adding to Special Wall accordingly

        ScoreFile = open("RawScores.txt","r")

        DataCheck = []

        for line in ScoreFile:
            SplitLine = line.split("-")
            Name = SplitLine[0]
            Turns = SplitLine[1]
            Turns = int(Turns)
            Score = SplitLine[2]
            Score = int(Score.rstrip("\n"))

            PData = []
            PData.append(Name)
            PData.append(Turns)
            PData.append(Score)

            DataCheck.append(PData)

        ScoreFile.close()

        print(DataCheck) #test functionality of reading RawScores

        #Achievements for Special Wall
        MaxScore = ["",0]
        MaxTurns = ["",0]
        MinTurns = ["",0]
        ExactScore = ["",0]
        MaxScore[0] = DataCheck[0][0]
        MaxScore[1] = DataCheck[0][2]
        MaxTurns[0] = DataCheck[0][0]
        MaxTurns[1] = DataCheck[0][1]
        MinTurns[0] = DataCheck[0][0]
        MinTurns[1] = DataCheck[0][1]
        ExactScore[0] = DataCheck[0][0]
        ExactScore[1] = DataCheck[0][2]

        GoalDiff1 = 50 - DataCheck[0][2]

        for i in range(len(DataCheck)):
            GoalDiff2 = 50 - DataCheck[i][2]

            if DataCheck[i][2] > MaxScore[1]: #update MaxScore
                MaxScore[0] = DataCheck[i][0]
                MaxScore[1] = DataCheck[i][2]

            elif DataCheck[i][1] > MaxTurns[1]: #update MaxTurns
                MaxTurns[0] = DataCheck[i][0]
                MaxTurns[1] = DataCheck[i][1]

            elif DataCheck[i][1] < MinTurns[1]: #update MinTurns
                MinTurns[0] = DataCheck[i][0]
                MinTurns[1] = DataCheck[i][1]

            elif 0 <= GoalDiff2 < GoalDiff1: #update ExactScore
                ExactScore[0] = DataCheck[i][0]
                ExactScore[1] = DataCheck[i][2]
                GoalDiff1 = GoalDiff2

            elif GoalDiff2 == 0:
                ExactScore[0] = DataCheck[i][0]
                ExactScore[1] = DataCheck[i][2]
                GoalDiff1 = GoalDiff2

        #Writing acheivements to Special Wall file
        WallFile = open("SpecialWall.txt","w") #Could be more efficient but best I can think of for now
        WallFile.write("'Special' ways people won their games\n\n")
        WallFile.write("Won the Point Lottery: " + MaxScore[0] + " with " + str(MaxScore[1]) + " points\n")
        WallFile.write("The Tortoise from 'The Hare and The Tortoise': " + MaxTurns[0] + " with " + str(MaxTurns[1]) + " turns\n")    
        WallFile.write("I Am Speed: " + MinTurns[0] + " with " + str(MinTurns[1]) + " turns\n")
        WallFile.write("Point Marksman: " + ExactScore[0] + " with a score of " + str(ExactScore[1]) + " points\n")
        WallFile.close()

    elif Choice == 2:
        ScoreFile = open("RawScores.txt","r")

        for line in ScoreFile:
            print(line)

        ScoreFile.close()

    elif Choice == 3:
        #Reading achievements file on terminal
        WallFile = open("SpecialWall.txt","r")

        for line in WallFile:
            print(line)

        WallFile.close()

    Choice = int(input("Enter your new choice (0 to exit): "))

