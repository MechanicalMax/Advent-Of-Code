#Carefully check conditions and test functions on their own
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

DirectionVectors = {
    'U': [0,1],
    'D': [0,-1],
    'L': [-1,0],
    'R': [1,0]
}

def equalVectors(position, tailPos):
    return position[0] == tailPos[0] and position[1] == tailPos[1]

def checkIfVisited(coveredSpaces, tailPos):
    newPosition = True
    for position in coveredSpaces:
        if(equalVectors(position, tailPos)):
            newPosition = False
    
    if(newPosition):
        coveredSpaces.append(tailPos.copy())

    return coveredSpaces

def updateTail(headPos, tailPos):
    if headPos[0] - tailPos[0] > 1:
        tailPos[0] += 1
        if headPos[1] > tailPos[1]:
            tailPos[1] += 1
        elif headPos[1] < tailPos[1]:
            tailPos[1] -= 1
    elif headPos[0] - tailPos[0] < -1:
        tailPos[0] -= 1
        if headPos[1] > tailPos[1]:
            tailPos[1] += 1
        elif headPos[1] < tailPos[1]:
            tailPos[1] -= 1
    
    if headPos[1] - tailPos[1] > 1:
        tailPos[1] += 1
        if headPos[0] > tailPos[0]:
            tailPos[0] += 1
        elif headPos[0] < tailPos[0]:
            tailPos[0] -= 1
    elif headPos[1] - tailPos[1] < -1:
        tailPos[1] -= 1
        if headPos[0] > tailPos[0]:
            tailPos[0] += 1
        elif headPos[0] < tailPos[0]:
            tailPos[0] -= 1

def updateRope(posKnots, instruction, coveredSpaces):
    direction = DirectionVectors[instruction[0]]
    magnitude = int(instruction[2:])

    for step in range(magnitude):
        posKnots[0] = [posKnots[0][0]+direction[0],posKnots[0][1]+direction[1]]
        for knot in range(len(posKnots)-1):
            tailStart = posKnots[knot+1].copy()
            updateTail(posKnots[knot], posKnots[knot+1])
            if(equalVectors(tailStart,posKnots[knot+1])):
                break
        coveredSpaces = checkIfVisited(coveredSpaces, posKnots[len(posKnots)-1])

    return posKnots, coveredSpaces

def sumTailPositions(lns, knots):
    tailCoveredPositions = []
    ropeKnotPositions = []
    for knot in range(knots):
        ropeKnotPositions.append([0,0])

    for instruction in lns:
        ropeKnotPositions, tailCoveredPositions = updateRope(ropeKnotPositions, instruction, tailCoveredPositions)

    return len(tailCoveredPositions)

def partA(puz):
    ans = sumTailPositions(lines, 2)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = sumTailPositions(lines, 10)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)