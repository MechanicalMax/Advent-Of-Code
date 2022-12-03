import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def sumRepeatPriorities(lns):
    total = 0
    for line in lns:
        total += getPriority(findRepeats(line[len(line)//2:],line[:len(line)//2])[0])
    return total

def findRepeats(first, second):
    repeats = []
    for element in first:
        if element in second:
            repeats.append(element)
    return repeats

def getPriority(letter):
    if(letter.isupper()):
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def sumGroupPriorities(lns):
    total = 0
    lineCounter = 0
    shortLine = ''
    otherLines = []

    for line in lns:
        if lineCounter == 0:
            shortLine = line
        else:
            if len(line) < len(shortLine):
                otherLines.append(shortLine)
                shortLine = line
            else:
                otherLines.append(line)

            if lineCounter == 2:
                firstTwoLinesRepeats = findRepeats(shortLine,otherLines[0])
                repeat = findRepeats(firstTwoLinesRepeats, otherLines[1])[0]
                total += getPriority(repeat)

                lineCounter = -1
                shortLine = ''
                otherLines = []
        
        lineCounter += 1

    return total

def partA(puz):
    ans = sumRepeatPriorities(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = sumGroupPriorities(lines)
    submit.safeSubmit(puz, ans, 'b')

#print(sumGroupPriorities(puz.example_data.splitlines()))

#partA(puz)
partB(puz)