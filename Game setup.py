import random #needed for each module, will compile all separate modules into a main program file at the end
Goal = 100 #setting goal score
PScore = 0 #player scores to test game
CScore = 0

#Making the point lots
SafeLot = [0,0,2,2,2,2,2,2,2,4,4,4,5,5,5,5,6,6,8,8,10] #high chance to get mid-range (which is still small)
RiskLot = [-10,-8,-6,-4,-4,-4,-4,-4,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,4,4,4,4,4,8,8,8,8,8,15,15,15,15,15,20,20,25] #more chances to lose more points but cahnces to gain more too
GoBigOrGoHomeLot = [-50,-25,25,-10,-10,-10,-10,-10,-10,-10,0,0,0,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,40,40,40,40,40,50,60,80] #more chances to lose more points than RiskLot but max. point reward is higher
