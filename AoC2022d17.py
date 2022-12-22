import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

rocks = [
    [(0,0), (1,0), (2,0), (3,0)],

    [(0,1), (1,0), (1,1), (1,2), (2,1)],

    [(0,0), (1,0), (2,0), (2,1), (2,2)],

    [(0,0), (0,1), (0,2), (0,3)],

    [(0,0), (0,1), (1,0), (1,1)]
]

def hitSolid(rockNum, x, y, solidRocks):
    for offset in rocks[rockNum]:
        position = (x + offset[0], y + offset[1])
        if 0 <= position[0] < 7:
            if position[1] in solidRocks[position[0]]:
                return True
        else:
            return True
    return False

def calculateHeightAfterRocks(jetPattern, maxRocks=2022):
    relativeFloor = [0 for _ in range(0, 7)]
    floor = [0 for _ in range(0, 7)]
    solidRocks = [[0] for _ in range(0, 7)]
    cache = {}
    additionalHeight = 0
    moveIndex = 0
    rockNum = 0
    height = 0

    while rockNum < maxRocks:
        rockIndex = rockNum % len(rocks)
        rockX, rockY = 2, max(floor) + 4
        canMove = True
        
        while(canMove):
            currentMove = jetPattern[moveIndex]
            moveIndex = (moveIndex+1)%len(jetPattern)

            #Move along x
            potentialX = rockX + 1 - 2 * (currentMove == '<')
            if(not hitSolid(rockIndex, potentialX, rockY, solidRocks)):
                rockX = potentialX

            #Move along y
            potentialY = rockY - 1
            if(not hitSolid(rockIndex, rockX, potentialY, solidRocks)):
                rockY = potentialY
            else:
                canMove = False

        #Rest
        #Add rock border to solid rocks
        for offset in rocks[rockIndex]:
            position = (rockX + offset[0], rockY + offset[1])
            solidRocks[position[0]].append(position[1])

        #Get floor
        for x in range(len(floor)):
            floor[x] = max(solidRocks[x])

        #Get Relative Floor
        minY = min(floor)
        for floorI, floorVal in enumerate(floor):
            relativeFloor[floorI] = floorVal - minY

        #Add to cache
        info = (rockIndex, moveIndex, tuple(relativeFloor))
        if info not in cache:
            cache[info] = (height, rockNum)
            #Add to height
            height += max(floor) - height
        else:
            initialHeight, initialRockNum = cache[info]
            deltaHeight = height - initialHeight
            deltaRocks = rockNum - initialRockNum
            remainingCycles = (maxRocks - rockNum) // deltaRocks
            additionalHeight = remainingCycles * deltaHeight
            remainingRocks = maxRocks - rockNum - remainingCycles * deltaRocks
            rockNum = maxRocks - remainingRocks
            cache = {}
        rockNum +=1

    return height + additionalHeight

def partA(puz):
    ans = calculateHeightAfterRocks(lines[0].strip())
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = calculateHeightAfterRocks(lines[0].strip(), 1000000000000)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)