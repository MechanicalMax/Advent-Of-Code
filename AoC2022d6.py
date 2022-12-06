import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getMarkerIndex(buffer, charSize):
    containsRepeats = True
    markerIndex = 1

    while(containsRepeats):
        minIndex = 0 if markerIndex - (charSize - 1) < 0 else markerIndex - (charSize - 1)
        recentChars = buffer[minIndex:markerIndex]
        currentChar = buffer[markerIndex]
     
        if currentChar in recentChars:
            markerIndex += recentChars.index(currentChar)
        elif markerIndex > (charSize - 1):
            if len(recentChars) == len(set(recentChars)):
                containsRepeats = False
     
        markerIndex += 1

    return markerIndex

def partA(puz):
    ans = getMarkerIndex(lines[0],4)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = getMarkerIndex(lines[0],14)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)