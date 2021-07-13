#Reading RawScores and adding to Special Wall accordingly

ScoreFile = open("RawScores.txt","r")
#WallFile = open("SpecialWall.txt","w") #Could be more efficient but best I can think of for now

DataCheck = []

for line in ScoreFile:
    SplitLine = line.split("-")
    Name = SplitLine[0]
    Turns = SplitLine[1]
    Turns = int(Turns)
    Score = SplitLine[2]
    Score = int(MaxScore.rstrip("\n"))

    PData = []
    PData.append(Name)
    PData.append(Turns)
    PData.append(MaxScore)

    DataCheck.append(PData)

ScoreFile.close()

print(DataCheck) #test functionality of reading RawScores

#Achievements for Special Wall
MaxScore = []
MaxTurns = []
MinTurns = []


