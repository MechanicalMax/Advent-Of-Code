import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
puz = getPuzzle.getPuzzleObject(__file__)
from aocd import lines

def getHighestCalCount():
    maxCount = 0
    currentCount = 0
    for line in lines:
        if line:
            currentCount += int(line)
        else:
            if currentCount >= maxCount:
                maxCount = currentCount
            currentCount = 0
    return maxCount

def partA(puz):
    ans = getHighestCalCount()
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'b')

partA(puz)