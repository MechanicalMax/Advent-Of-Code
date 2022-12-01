import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def sumElements(arr):
    sum = 0
    for ele in arr:
        sum += ele
    return sum

def _sumTopThreeCalCounts():
    maxCounts = [0, 0, 0]
    currentCount = 0
    for line in lines:
        if line:
            currentCount += int(line)
        else:
            for i, max in enumerate(maxCounts):
                if currentCount > max:
                    maxCounts.insert(i, currentCount)
                    maxCounts.pop()
                    break
            currentCount = 0    

    return sumElements(maxCounts)

def _getHighestCalCount():
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
    ans = _getHighestCalCount()
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = _sumTopThreeCalCounts()
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)