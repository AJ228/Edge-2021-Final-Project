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

    elif GoalDiff2 < GoalDiff1: #update ExactScore
        ExactScore[0] = DataCheck[i][0]
        ExactScore[1] = DataCheck[i][2]
        GoalDiff1 = GoalDiff2

#Check if code works properly
print(MaxScore)
print(MaxTurns)
print(MinTurns)
print(ExactScore)

#Writing acheivements to Special Wall file
WallFile = open("SpecialWall.txt","w") #Could be more efficient but best I can think of for now
WallFile.write("'Special' ways people won their games\n\n")
WallFile.write("Won the Point Lottery: " + MaxScore[0] + " with " + str(MaxScore[1]) + " points\n")
WallFile.write("The Tortoise from 'The Hare and The Tortoise': " + MaxTurns[0] + " with " + str(MaxTurns[1]) + " turns\n")    
WallFile.write("I Am Speed: " + MinTurns[0] + " with " + str(MinTurns[1]) + " turns\n")
WallFile.write("Point Marksman: " + ExactScore[0] + " with a score of " + str(ExactScore[1]) + " points\n")
WallFile.close()

#Reading achievements file on terminal
WallFile = open("SpecialWall.txt","r")

for line in WallFile:
    print(line)

WallFile.close()

