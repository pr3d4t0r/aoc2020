# nums=[0,3,6]
nums=[12,1,16,3,11,0]
# nums = [ 14,8,16,0,1,17, ]
numsSpokenPreviously={}
numsSpoken={}
numsSpokenFirst={}
lastSpokenNum=-1

def updateListsWithSpokenNum(turn, spokenNum):
    if spokenNum in numsSpokenFirst:
        numsSpokenFirst[spokenNum]=False
        numsSpokenPreviously[spokenNum]=numsSpoken[spokenNum]
    else:
        numsSpokenFirst[spokenNum]=True
    numsSpoken[spokenNum]=turn

def speakNum(turn, lastSpokenNum):
    if turn<=len(nums):
        currentNum=nums[turn-1]
    else:
        if lastSpokenNum in numsSpoken:
            if numsSpokenFirst[lastSpokenNum]==True:
                currentNum=0
            else:
                currentNum=numsSpoken[lastSpokenNum] - numsSpokenPreviously[lastSpokenNum]
        else:#we won't be reaching here.
            print("SOMETHING WONG")
            currentNum=0
    #print("turn="+str(turn)+" lastSpokenNum="+str(lastSpokenNum)+" spoken:"+str(currentNum))
    return currentNum

turn=1
while turn<=30000000:
# while turn<=2020:
    spokenNum = speakNum(turn, lastSpokenNum)
    updateListsWithSpokenNum(turn, spokenNum)
    turn=turn+1
    lastSpokenNum = spokenNum
    if (turn%1000000==0):
        print(turn)
        print("sizeOfLists="+str(len(numsSpoken)))
print(turn-1, spokenNum)

