#Stuck on part A for too long because I didn't realize
#.split() would return a str, not an int. Casting to
#an int fixed the issue.
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def ifContains(minOne, maxOne, minTwo, maxTwo):
    if minOne <= minTwo and maxOne >= maxTwo:
        return True
    elif minOne >= minTwo and maxOne <= maxTwo:
        return True
    return False

def getRangeEnds(line):
    ranges = line.split(',')
    minOne, maxOne = ranges[0].split('-')
    minTwo, maxTwo = ranges[1].split('-')
    return int(minOne), int(maxOne), int(minTwo), int(maxTwo)

def countFullContainments(lns):
    total = 0
    for line in lns:
        minOne, maxOne, minTwo, maxTwo = getRangeEnds(line)
        total += ifContains(minOne, maxOne, minTwo, maxTwo)
    return total

def ifOverlap(minOne, maxOne, minTwo, maxTwo):
    if maxOne < minTwo:
        return False
    elif maxTwo < minOne:
        return False
    else:
        return True

def countAnyOverlap(lns):
    total = 0
    for line in lns:
        minOne, maxOne, minTwo, maxTwo = getRangeEnds(line)
        total += ifOverlap(minOne, maxOne, minTwo, maxTwo)
    return total

def partA(puz):
    ans = countFullContainments(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = countAnyOverlap(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)